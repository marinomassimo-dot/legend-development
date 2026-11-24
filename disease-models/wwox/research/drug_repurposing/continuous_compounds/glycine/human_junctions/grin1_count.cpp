// Count sequence-verified GRIN1 junctions on either strand. Inputs are gzip streams.
#include <zlib.h>
#include <unistd.h>
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstring>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>

using Word = std::uint64_t;
struct Probe {
    std::string kind;
    int offset;
    std::string sequence;
    long long target = 0, other = 0;
};

struct Input {
    gzFile file;
    explicit Input(const std::string& path)
        : file(path == "-" ? gzdopen(dup(STDIN_FILENO), "rb") : gzopen(path.c_str(),"rb")) {
        if (!file) throw std::runtime_error("Unable to open input");
        gzbuffer(file,1<<20);
    }
    bool line(std::string& result) {
        char piece[4096];
        result.clear();
        while (gzgets(file,piece,sizeof(piece))) {
            const size_t n = std::strlen(piece);
            if (!n) throw std::runtime_error("Invalid line");
            result.append(piece,n);
            if (piece[n-1]=='\n') {
                result.pop_back();
                if (!result.empty() && result.back()=='\r') result.pop_back();
                return true;
            }
        }
        int error;
        gzerror(file,&error);
        if (error!=Z_OK && error!=Z_STREAM_END) throw std::runtime_error("Corrupt gzip stream");
        return !result.empty();
    }
    ~Input(){ gzclose(file); }
};

struct Matcher {
    std::vector<Probe> probes;
    std::unordered_map<Word,int> lookup;
    std::array<unsigned char,65536> suffix{};
    std::array<unsigned char,256> base{};
    static constexpr Word mask=(Word(1)<<62)-1;
    explicit Matcher(const std::string& path) {
        base.fill(4);
        for (int i=0;i<4;i++) {
            base[static_cast<unsigned char>("ACGT"[i])]=i;
            base[static_cast<unsigned char>("acgt"[i])]=i;
        }
        std::ifstream stream(path);
        std::string line,kind,seq;
        int offset;
        std::getline(stream,line);
        while(stream>>kind>>offset>>seq) {
            if (seq.size()!=31 || (kind!="included" && kind!="skipped")) throw std::runtime_error("Invalid probe");
            Word forward=0,reverse=0;
            for (size_t j=0;j<31;j++) {
                auto k=base[static_cast<unsigned char>(seq[j])];
                if(k>=4) throw std::runtime_error("Noncanonical probe");
                forward=(forward<<2)|k;
                reverse|=Word(3-k)<<(2*j);
            }
            int id=static_cast<int>(probes.size());
            for(Word w:{forward,reverse}) {
                if(!lookup.emplace(w,id).second) throw std::runtime_error("Duplicate probe");
                suffix[w&65535]=1;
            }
            probes.push_back({kind,offset,seq});
        }
        if(probes.empty()) throw std::runtime_error("No probes");
    }
    template<class Callback>
    void scan(const std::string& seq, Word& word, int& length, Callback hit) {
        for(size_t j=0;j<seq.size();j++) {
            auto k=base[static_cast<unsigned char>(seq[j])];
            if(k>=4){word=0;length=0;continue;}
            word=((word<<2)|k)&mask;
            length=std::min(length+1,31);
            if(length<31 || !suffix[word&65535]) continue;
            auto p=lookup.find(word);
            if(p!=lookup.end()) hit(p->second,j);
        }
    }
};

void audit(Input& in,Matcher& matcher) {
    std::string line;
    Word word=0;
    int length=0;
    bool target=false;
    while(in.line(line)) {
        if(!line.empty() && line[0]=='>') {
            word=0;length=0;
            target=line.find(" gene_symbol:GRIN1 ")!=std::string::npos;
        } else {
            matcher.scan(line,word,length,[&](int i,size_t){
                auto& p=matcher.probes[i]; if(target) ++p.target; else ++p.other;
            });
        }
    }
    std::cout<<"class\toffset\ttarget_hits\tother_hits\n";
    for(auto& p:matcher.probes)
        std::cout<<p.kind<<'\t'<<p.offset<<'\t'<<p.target<<'\t'<<p.other<<'\n';
}

void reads(Input& in,Matcher& matcher) {
    std::array<std::array<long long,4>,4> counts{};
    long long n=0;
    std::string header,seq,plus,quality;
    while(in.line(header)) {
        if(!in.line(seq)||!in.line(plus)||!in.line(quality)||header.empty()||header[0]!='@'||
                plus.empty()||plus[0]!='+'||seq.size()!=quality.size())
            throw std::runtime_error("Malformed FASTQ record");
        ++n;
        Word word=0;
        int length=0;
        std::array<int,4> found{};
        matcher.scan(seq,word,length,[&](int i,size_t j){
            const auto& p=matcher.probes[i];
            int q=*std::min_element(quality.begin()+j-30,quality.begin()+j+1)-33;
            int bit=p.kind=="included"?1:2;
            if(q>=20) {found[1]|=bit; if(p.offset==15) found[0]|=bit;}
            if(q>=30) {found[3]|=bit; if(p.offset==15) found[2]|=bit;}
        });
        for(int i=0;i<4;i++) counts[i][found[i]]++;
    }
    std::cout<<"rule\tQ\treads\tincluded\tskipped\tconflict\n";
    for(int i=0;i<4;i++)
        std::cout<<(i%2?"any":"centered")<<'\t'<<(i>=2?30:20)<<'\t'<<n<<'\t'
                 <<counts[i][1]<<'\t'<<counts[i][2]<<'\t'<<counts[i][3]<<'\n';
}
int main(int argc,char**argv){
    try{
        if(argc!=4) throw std::runtime_error("Use audit|count probes.tsv sequence.gz");
        Matcher matcher(argv[2]);
        Input input(argv[3]);
        if(std::string(argv[1])=="audit") audit(input,matcher);
        else if(std::string(argv[1])=="count") reads(input,matcher);
        else throw std::runtime_error("Unknown operation");
    }catch(const std::exception& e){std::cerr<<e.what()<<'\n';return 1;}
}

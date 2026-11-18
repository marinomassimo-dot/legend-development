# Reproduces every model output of the I1/I3/I6 dossiers (about 10 minutes): bash run_all.sh. numpy only; all seeds fixed in the scripts.
set -e
cd "$(dirname "$0")"
python3 rebound_oscillator.py --T 1500 --nrep 32 > validation_long_run.txt
python3 predict_classes.py run scan_out --T 900 --nrep 16
python3 score_predictions.py run scan_out/class_scan.tsv scan_out/score.tsv > scan_out/score.txt
python3 pam_sign_scan.py run pam_sign_scan.tsv --n 200 > pam_scan.log
python3 pam_sign_scan.py run pam_sign_scan_coupled.tsv --n 300 --coupling 1 > pam_scan_coupled.log
python3 brake_cliff.py run brake_cliff.tsv > /dev/null
python3 chloride_headroom.py run chloride_headroom.tsv > /dev/null

# Operator-reserved patch proposal: Pages smoke step reads a stale CDN copy (HE, 2026-11-28)

Not applied. `.github/workflows/publish-shareable-view.yml` is operator-reserved; this adds one patch to those listed
in `CHECKPOINT_HE_20261124_J.md` section 3.

**Observed (IT39, read-only, 2026-11-28):** Pages run #301 (head `d9a51f3da`) went red only in the step "live
index.html equals the package file". The live page was correct afterwards (sha256 prefix `c9dcdae214d4bf0f`, equal to a
local build of main; `cache-control: max-age=600`). The step retries on a non-200 status only, never on a hash
mismatch, so a cached copy of the previous deploy fails the run. HE did not re-measure the live page.

**Proposed change:** in that step, replace the lines from `for i in 1 2 3 4 5 6; do` through
`[ "$want" = "$have" ]` with:

```sh
want="$EXPECTED_INDEX_SHA"
for i in $(seq 1 12); do
  code=$(curl -s -H 'Cache-Control: no-cache' -o live.html -w "%{http_code}" "$url?cb=$GITHUB_RUN_ID-$i" || true)
  have=$(sha256sum live.html 2>/dev/null | cut -d' ' -f1)
  [ "$code" = "200" ] && [ "$want" = "$have" ] && break
  sleep 20
done
echo "live status: $code at $url"
echo "package $want"; echo "live    $have"
[ "$code" = "200" ]
[ "$want" = "$have" ]
```

A wrong deploy still fails, after about four minutes instead of at once. Not tested: whether the CDN honours the
query string or the header. The later check of `reports/` files has the same exposure and is left unchanged here.

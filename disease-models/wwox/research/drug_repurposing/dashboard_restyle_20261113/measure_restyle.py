#!/usr/bin/env python3
"""Dashboard restyle: how far a visitor must scroll to reach the first investigation and the evidence chains, and screenshots of the first screen, a representative row and the chains.

  python3 -I measure_restyle.py <repo root> <language> <out dir> [--dark]

Builds the shareable page of the given checkout with its own generator, opens it in the real Chromium the view tests use (existing `find_chromium` and `Cdp`; no new dependency), at 1280x900 and
390x844 (phone emulation), prints the distance in css pixels to `#inv-1` and `#chains` and the page width check (scrollWidth), and writes PNGs. It reads and writes nothing in the repository."""
import base64, json, os, sys, tempfile
from pathlib import Path

if "--help" in sys.argv or "-h" in sys.argv or len(sys.argv) < 4:
    print(__doc__); sys.exit(0)
root, lang, out = Path(sys.argv[1]).resolve(), sys.argv[2], Path(sys.argv[3])
sys.path.insert(0, str(root / "framework/scripts"))
import repurposing_view as rv  # noqa: E402

html = Path(tempfile.mkdtemp()) / f"page_{lang}.html"
html.write_text(rv.build(rv.DEFAULT_DR, "shareable", lang), encoding="utf-8")
binary = rv.find_chromium()
if not binary:
    sys.exit("no Chromium binary: nothing was measured")
out.mkdir(parents=True, exist_ok=True)
cdp = rv.Cdp(binary, tempfile.mkdtemp())
try:
    cdp.call("Page.enable")
    if "--dark" in sys.argv:
        cdp.call("Emulation.setEmulatedMedia", features=[{"name": "prefers-color-scheme", "value": "dark"}])
    for w, h, mobile in ((1280, 900, False), (390, 844, True)):
        cdp.call("Emulation.setDeviceMetricsOverride", width=w, height=h, deviceScaleFactor=1, mobile=mobile)
        cdp.call("Page.navigate", url="about:blank"); cdp.events.clear()
        cdp.call("Page.navigate", url=f"file://{html}"); cdp.wait_event("Page.loadEventFired"); cdp.wait_for(rv.CUR_READY_JS); cdp.settle()
        width = cdp.evaluate("document.documentElement.scrollWidth")
        for name, sel, tall in (("first_screen", "body", 1), ("first_investigation", "#inv-1", 1), ("evidence_chains", "#chains", 1)):
            y = cdp.evaluate("(function(){var e=document.querySelector(%s);return e?Math.max(0,Math.round(e.getBoundingClientRect().top+scrollY)-8):-1})()" % json.dumps(sel))
            shot = cdp.call("Page.captureScreenshot", format="png", clip={"x": 0, "y": max(y, 0), "width": w, "height": h * (2 if mobile and name != "first_screen" else 1), "scale": 1}, captureBeyondViewport=True)
            (out / f"{lang}_{name}_{w}.png").write_bytes(base64.b64decode(shot["data"]))
            print(f"{lang}\t{w}x{h}\t{name}\ty={y}\tscrollWidth={width}")
finally:
    cdp.close()

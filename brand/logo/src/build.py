#!/usr/bin/env python3
"""Build the Nemias Martins Advocacia logo masters (symbol, lockups) as pure-path SVGs.

Requires: fonttools, uharfbuzz (only to outline the wordmark).
Fonts: Caladea Regular (Apache 2.0) for the name, Inter Medium (OFL) for "ADVOCACIA".
Run:  python3 brand/logo/src/build.py
"""
import math
import os

import uharfbuzz as hb
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "final"))
os.makedirs(OUT, exist_ok=True)

GREEN = "#1D3B36"   # Verde Ardósia
GOLD = "#A9874E"    # Dourado Antigo
WHITE = "#FFFFFF"

SERIF = "/usr/share/fonts/truetype/crosextra/Caladea-Regular.ttf"
SANS = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"


def f(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


# ---------------------------------------------------------------- symbol
def symbol_paths():
    """Return (letters_d, base_d) on a 256 canvas.

    Construction (grid before optical shift):
      stems w=30, cap 52..184; S1 x40, S2 x113 (shared N/M stem), S3 x186
      N diagonal at exactly 60°, M vee arms at 67.4° (shared slope), vertex just above baseline
      foundation bar 200..216, x28..228 (the 'alicerce')
    Whole mark nudged up 6 units for optical centring.
    """
    dy = -6
    top, base = 52 + dy, 184 + dy
    w = 30
    s1, s2, s3 = 40, 113, 186
    h = base - top
    # N diagonal, 60 deg: right edge (xa,top)->(s2+w,base), left edge parallel through (s2,base)
    run = h / math.tan(math.radians(60))
    xa = s2 + w - run
    y_left = base - (s2 - s1) * math.tan(math.radians(60))  # where left edge meets x=s1
    n_diag = f"M{s1} {top}H{f(xa)}L{s2 + w} {base}H{s2}L{s1} {f(y_left)}Z"
    # M vee: outer edge from (s2,top) to centre, inner edge from (s2+w,top), same slope
    cx = (s2 + s3 + w) / 2  # 164.5
    t = 2.4
    y_out = top + (cx - s2) * t
    y_in = top + (cx - s2 - w) * t
    m_vee = (f"M{s2} {top}H{s2 + w}L{f(cx)} {f(y_in)}L{s3} {top}H{s3 + w}"
             f"L{f(cx)} {f(y_out)}Z")
    stems = "".join(f"M{x} {top}H{x + w}V{base}H{x}Z" for x in (s1, s2, s3))
    letters = stems + n_diag + m_vee
    basebar = f"M28 {200 + dy}H228V{216 + dy}H28Z"
    return letters, basebar


# ---------------------------------------------------------------- type → paths
def text_path(fontfile, text, size, x, y, tracking=0.0):
    """Shape `text` with HarfBuzz (kerning on) and return (svg path d, advance width)."""
    blob = hb.Blob.from_file_path(fontfile)
    face = hb.Face(blob)
    font = hb.Font(face)
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf, {"kern": True, "liga": False})
    tt = TTFont(fontfile)
    gs = tt.getGlyphSet()
    order = tt.getGlyphOrder()
    upm = tt["head"].unitsPerEm
    sc = size / upm
    pen = SVGPathPen(gs, ntos=lambda v: f"{v:.1f}".rstrip("0").rstrip("."))
    cur = 0.0
    n = len(buf.glyph_infos)
    for i, (info, pos) in enumerate(zip(buf.glyph_infos, buf.glyph_positions)):
        name = order[info.codepoint]
        tp = TransformPen(pen, (sc, 0, 0, -sc, x + (cur + pos.x_offset) * sc, y - pos.y_offset * sc))
        gs[name].draw(tp)
        cur += pos.x_advance
        if i < n - 1:
            cur += tracking * upm
    return pen.getCommands(), cur * sc


def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {f(w)} {f(h)}" width="{f(w)}" height="{f(h)}" '
            f'role="img" aria-labelledby="title"><title id="title">{title}</title>{body}</svg>\n')


def symbol_group(letters_fill, base_fill, tx=0, ty=0, s=1.0):
    letters, basebar = symbol_paths()
    return (f'<g id="symbol" transform="translate({f(tx)} {f(ty)}) scale({f(s)})">'
            f'<path fill="{letters_fill}" d="{letters}"/><path fill="{base_fill}" d="{basebar}"/></g>')


def wordmark(name_fill, sub_fill, x, y_name, name_size, align="left", total_w=None):
    name_d, name_w = text_path(SERIF, "Nemias Martins", name_size, 0, 0, tracking=0.01)
    sub_size = name_size * 0.30
    sub_d, sub_w = text_path(SANS, "ADVOCACIA", sub_size, 0, 0, tracking=0.42)
    if align == "left":
        nx, sx = x, x + 3
    else:  # centre on total_w
        nx = (total_w - name_w) / 2
        sx = (total_w - sub_w) / 2
    y_sub = y_name + name_size * 0.62
    return (f'<g id="wordmark"><path fill="{name_fill}" transform="translate({f(nx)} {f(y_name)})" d="{name_d}"/>'
            f'<path fill="{sub_fill}" transform="translate({f(sx)} {f(y_sub)})" d="{sub_d}"/></g>'), name_w, sub_w


SCHEMES = {
    "color": (GREEN, GOLD, GREEN, GOLD),        # letters, base, name, sub
    "reverse": (WHITE, GOLD, WHITE, GOLD),      # on Verde Ardósia
    "black": ("#000", "#000", "#000", "#000"),
    "white": (WHITE, WHITE, WHITE, WHITE),
}


def build():
    title = "Nemias Martins Advocacia"
    for key, (lf, bf, nf, sf) in SCHEMES.items():
        # symbol
        open(f"{OUT}/nm-symbol-{key}.svg", "w").write(svg(256, 256, symbol_group(lf, bf), title))
        # horizontal lockup: symbol cap-height ≈ name size; height 256
        name_size = 92
        wm, name_w, _ = wordmark(nf, sf, 0, 0, name_size)
        sym_s = 0.9
        gap = 40
        x_text = 256 * sym_s - 28 * sym_s + gap
        body = symbol_group(lf, bf, tx=0, ty=12, s=sym_s)
        wm, name_w, _ = wordmark(nf, sf, x_text, 140, name_size)
        width = x_text + name_w + 24
        open(f"{OUT}/nm-horizontal-{key}.svg", "w").write(svg(width, 256, body + wm, title))
        # stacked lockup
        name_size_s = 72
        _, nw, _ = wordmark(nf, sf, 0, 0, name_size_s)
        W = max(nw + 48, 360)
        sym_s2 = 0.82
        sym_x = (W - 256 * sym_s2) / 2
        body = symbol_group(lf, bf, tx=sym_x, ty=0, s=sym_s2)
        wm, _, _ = wordmark(nf, sf, 0, 270, name_size_s, align="centre", total_w=W)
        open(f"{OUT}/nm-stacked-{key}.svg", "w").write(svg(W, 336, body + wm, title))
        # wordmark only
        wm, nw, _ = wordmark(nf, sf, 8, 110, 92)
        open(f"{OUT}/nm-wordmark-{key}.svg", "w").write(svg(nw + 24, 160, wm, title))
    # small-size cut: heavier stems, thicker base, no fine notch issues
    print("written to", OUT)


if __name__ == "__main__":
    build()

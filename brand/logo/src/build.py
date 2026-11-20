#!/usr/bin/env python3
"""Build the Nemias Martins Advocacia logo masters — concept "A Divisa".

N and M share one stem — the dividing line (a divisa) that defines limits and joins the parties.
The shared stem carries the accent colour (Terracota).

Requires: fonttools, uharfbuzz (only to outline the wordmark).
Fonts (SIL OFL, in src/fonts): Cormorant Garamond SemiBold (name), Manrope SemiBold ("ADVOCACIA").
Run:  python3 brand/logo/src/build.py
"""
import os

import uharfbuzz as hb
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "final"))
os.makedirs(OUT, exist_ok=True)

VERDE = "#1F3D36"        # Verde Divisa — principal
TERRACOTA = "#9E5536"    # destaque / a divisa (sobre fundos claros)
TERRA_CLARO = "#D9A486"  # a divisa sobre o verde
AREIA = "#F4EFE6"        # fundo
PEDRA = "#D9CFBF"        # apoio / linhas
GRAFITE = "#1C1C1A"      # texto

SERIF = os.path.join(HERE, "fonts", "CormorantGaramond-SemiBold.ttf")
SANS = os.path.join(HERE, "fonts", "Manrope-SemiBold.ttf")


def f(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


# ---------------------------------------------------------------- symbol
def symbol_paths():
    """Return (letters_d, divisa_d) on a 256 canvas.

    Construction:
      cap height 48..208 (160 units), mark spans x 20..236 — centred on the canvas
      N: stem x20..44; diagonal 34 wide at the top (x20..54), at exactly 70° (run = 160·tan20° ≈ 58.24)
      divisa (shared stem): 13 wide, full height, starts where the N diagonal lands; accent colour
      M: arms 32 wide start at the divisa and mirror at the right; slope 2.3; right stem 24 wide
    """
    top, base = 48, 208
    h = base - top
    run = 58.24                      # 70° diagonal
    n_top_l, n_top_r = 20, 54
    n_diag = (f"M{n_top_l} {top}H{n_top_r}L{f(n_top_r + run)} {base}"
              f"H{f(n_top_l + run)}Z")
    n_stem = f"M20 {top}H44V{base}H20Z"
    d_l = n_top_r + run              # divisa starts where the N diagonal lands
    d_r = d_l + 13
    divisa = f"M{f(d_l)} {top}H{f(d_r)}V{base}H{f(d_l)}Z"
    # M
    s3_r = 236
    a_w = 32                         # arm width at the top
    cx = (d_r + s3_r) / 2
    t = 2.3
    y_out = top + (cx - d_r) * t
    y_in = top + (cx - d_r - a_w) * t
    m_vee = (f"M{f(d_r)} {top}H{f(d_r + a_w)}L{f(cx)} {f(y_in)}L{f(s3_r - a_w)} {top}H{s3_r}"
             f"L{f(cx)} {f(y_out)}Z")
    m_stem = f"M{s3_r - 24} {top}H{s3_r}V{base}H{s3_r - 24}Z"
    _ = h
    return n_stem + n_diag + m_vee + m_stem, divisa


# ---------------------------------------------------------------- type → paths
_FONT_CACHE = {}


def text_path(fontfile, text, size, x=0, y=0, tracking=0.0):
    """Shape `text` with HarfBuzz (kerning on) and return (svg path d, advance width)."""
    if fontfile not in _FONT_CACHE:
        face = hb.Face(hb.Blob.from_file_path(fontfile))
        tt = TTFont(fontfile)
        _FONT_CACHE[fontfile] = (hb.Font(face), tt, tt.getGlyphSet(), tt.getGlyphOrder(), tt["head"].unitsPerEm)
    font, tt, gs, order, upm = _FONT_CACHE[fontfile]
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf, {"kern": True, "liga": False})
    sc = size / upm
    pen = SVGPathPen(gs, ntos=lambda v: f"{v:.1f}".rstrip("0").rstrip("."))
    cur = 0.0
    n = len(buf.glyph_infos)
    for i, (info, pos) in enumerate(zip(buf.glyph_infos, buf.glyph_positions)):
        tp = TransformPen(pen, (sc, 0, 0, -sc, x + (cur + pos.x_offset) * sc, y - pos.y_offset * sc))
        gs[order[info.codepoint]].draw(tp)
        cur += pos.x_advance
        if i < n - 1:
            cur += tracking * upm
    return pen.getCommands(), cur * sc


def svg(w, h, body, title="Nemias Martins Advocacia"):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {f(w)} {f(h)}" width="{f(w)}" height="{f(h)}" '
            f'role="img" aria-labelledby="title"><title id="title">{title}</title>{body}</svg>\n')


def symbol_group(letters_fill, divisa_fill, tx=0, ty=0, s=1.0):
    letters, divisa = symbol_paths()
    return (f'<g id="symbol" transform="translate({f(tx)} {f(ty)}) scale({f(s)})">'
            f'<path fill="{letters_fill}" d="{letters}"/><path fill="{divisa_fill}" d="{divisa}"/></g>')


NAME = "NEMIAS MARTINS"
NAME_TRACK = 0.06
SUB = "ADVOCACIA"
SUB_TRACK = 0.45


def wordmark_parts(name_size):
    name_d, name_w = text_path(SERIF, NAME, name_size, tracking=NAME_TRACK)
    sub_size = name_size * 0.31
    sub_d, sub_w = text_path(SANS, SUB, sub_size, tracking=SUB_TRACK)
    return name_d, name_w, sub_d, sub_w, sub_size


# colour schemes: letters, divisa, name, sub
SCHEMES = {
    "color": (VERDE, TERRACOTA, VERDE, TERRACOTA),
    "reverse": (AREIA, TERRA_CLARO, AREIA, TERRA_CLARO),
    "black": ("#000000", "#000000", "#000000", "#000000"),
    "white": ("#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"),
}


def build():
    for key, (lf, df, nf, sf) in SCHEMES.items():
        open(f"{OUT}/nm-symbol-{key}.svg", "w").write(svg(256, 256, symbol_group(lf, df)))

        # horizontal: symbol (cap 160 → scaled) left; name cap-height aligned to the symbol top
        name_size = 80
        name_d, name_w, sub_d, sub_w, sub_size = wordmark_parts(name_size)
        s = 1.0
        sym_right = 236 * s
        x_text = sym_right + 40
        y_name = 134                    # name + ADVOCACIA block centred on the symbol (cap top ≈ 84)
        y_sub = 184
        body = symbol_group(lf, df, s=s)
        body += (f'<g id="wordmark"><path fill="{nf}" transform="translate({f(x_text)} {f(y_name)})" d="{name_d}"/>'
                 f'<path fill="{sf}" transform="translate({f(x_text + 4)} {f(y_sub)})" d="{sub_d}"/></g>')
        W = x_text + max(name_w, sub_w) + 24
        open(f"{OUT}/nm-horizontal-{key}.svg", "w").write(svg(W, 256, body))

        # stacked
        name_size = 64
        name_d, name_w, sub_d, sub_w, sub_size = wordmark_parts(name_size)
        W = max(name_w + 48, 300)
        ss = 0.85
        sym_x = (W - 256 * ss) / 2
        body = symbol_group(lf, df, tx=sym_x, ty=-20, s=ss)
        y_name = 248
        y_sub = y_name + 44
        body += (f'<g id="wordmark"><path fill="{nf}" transform="translate({f((W - name_w) / 2)} {y_name})" d="{name_d}"/>'
                 f'<path fill="{sf}" transform="translate({f((W - sub_w) / 2)} {y_sub})" d="{sub_d}"/></g>')
        open(f"{OUT}/nm-stacked-{key}.svg", "w").write(svg(W, 316, body))

        # wordmark only
        name_size = 96
        name_d, name_w, sub_d, sub_w, _ = wordmark_parts(name_size)
        body = (f'<g id="wordmark"><path fill="{nf}" transform="translate(12 92)" d="{name_d}"/>'
                f'<path fill="{sf}" transform="translate(16 140)" d="{sub_d}"/></g>')
        open(f"{OUT}/nm-wordmark-{key}.svg", "w").write(svg(name_w + 24, 160, body))

    # icon tile: Verde Divisa rounded square, Areia letters, light terracotta divisa
    letters, divisa = symbol_paths()
    body = (f'<rect width="256" height="256" rx="56" fill="{VERDE}"/>'
            f'<g transform="translate(128 128) scale(0.66) translate(-128 -128)">'
            f'<path fill="{AREIA}" d="{letters}"/><path fill="{TERRA_CLARO}" d="{divisa}"/></g>')
    open(f"{OUT}/nm-icon-tile.svg", "w").write(svg(256, 256, body))
    # round avatar
    body = (f'<circle cx="128" cy="128" r="128" fill="{VERDE}"/>'
            f'<g transform="translate(128 128) scale(0.62) translate(-128 -128)">'
            f'<path fill="{AREIA}" d="{letters}"/><path fill="{TERRA_CLARO}" d="{divisa}"/></g>')
    open(f"{OUT}/nm-avatar.svg", "w").write(svg(256, 256, body))
    print("written to", OUT)


if __name__ == "__main__":
    build()

#!/usr/bin/env python3
"""Genera trabajos.html a partir de trabajos/trabajos.json.
Cada entrada: {"foto": "nombre.jpg", "titulo": "...", "descripcion": "...", "lugar": "Valencia", "fecha": "2026-10"}
Las fotos se dejan en trabajos/ y el script las optimiza a img/trabajos/.
Con menos de 3 trabajos la página queda noindex y fuera del sitemap."""
import json, html, os, re, subprocess
root=os.path.dirname(os.path.abspath(__file__)); os.chdir(root)
items=json.load(open('trabajos/trabajos.json',encoding='utf-8'))
os.makedirs('img/trabajos',exist_ok=True)
cards=[]; imgs=[]
for it in items:
    src=os.path.join('trabajos',it['foto']); dst=os.path.join('img/trabajos',os.path.splitext(it['foto'])[0]+'.jpg')
    if os.path.exists(src):
        subprocess.run(['sips','-Z','1400','-s','format','jpeg','-s','formatOptions','70',src,'--out',dst],capture_output=True)
        w,h=[int(x) for x in re.findall(r'pixel(?:Width|Height): (\d+)',subprocess.run(['sips','-g','pixelWidth','-g','pixelHeight',dst],capture_output=True,text=True).stdout)]
    else: continue
    t=html.escape(it['titulo']); d=html.escape(it.get('descripcion','')); l=html.escape(it.get('lugar',''))
    cards.append(f'<figure class="job"><img src="{dst}" alt="{t}{", "+l if l else ""}" width="{w}" height="{h}" loading="lazy" decoding="async"><figcaption><h2>{t}</h2><p>{d}</p>'+(f'<span>{l}</span>' if l else '')+'</figcaption></figure>')
    imgs.append({"@type":"ImageObject","contentUrl":f"https://inoxestay.es/{dst}","name":it['titulo'],"description":it.get('descripcion','')})
index=len(cards)>=3
robots='index, follow, max-image-preview:large' if index else 'noindex'
ld=json.dumps({"@context":"https://schema.org","@type":"CollectionPage","name":"Trabajos realizados","url":"https://inoxestay.es/trabajos.html","hasPart":imgs},ensure_ascii=False)
page=f'''<!doctype html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Trabajos realizados de soldadura inoxidable náutica | INOX ESTAY</title>
<meta name="description" content="Trabajos reales de soldadura de acero inoxidable en embarcaciones en Valencia: pasamanos, candeleros, arcos, herrajes y reparaciones.">
<meta name="robots" content="{robots}"><link rel="canonical" href="https://inoxestay.es/trabajos.html"><meta name="theme-color" content="#0d151d">
<link rel="icon" type="image/png" href="img/favicon.png"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap">
<script type="application/ld+json">{ld}</script>
<style>
:root{{--bg:#f5f6f5;--surface:#fff;--ink:#14181a;--soft:#565f63;--line:#d8dcda;--navy:#0d151d;--heat:#b5813e;--hi:#fffaf2}}
@media(prefers-color-scheme:dark){{:root{{--bg:#0f1317;--surface:#171d22;--ink:#eef1f2;--soft:#a7b0b4;--line:#293136;--heat:#dba05c;--hi:#221607}}}}
*{{box-sizing:border-box}}body{{margin:0;font-family:Inter,system-ui,sans-serif;background:var(--bg);color:var(--ink);line-height:1.6}}
header{{background:var(--navy);color:#eef1f2;padding:14px 20px;display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap}}header a{{color:inherit;text-decoration:none;font-weight:700}}header .tel a{{font-weight:600;margin-left:14px;font-size:.95rem}}
main{{max-width:1000px;margin:0 auto;padding:36px 20px 64px}}h1{{font-size:2rem;margin:0 0 8px}}.lede{{color:var(--soft);margin:0 0 28px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:20px}}
.job{{margin:0;background:var(--surface);border:1px solid var(--line);border-radius:14px;overflow:hidden}}.job img{{width:100%;height:230px;object-fit:cover;display:block}}
.job figcaption{{padding:16px}}.job h2{{font-size:1.05rem;margin:0 0 6px}}.job p{{color:var(--soft);margin:0 0 8px;font-size:.95rem}}.job span{{font-size:.8rem;color:var(--heat);font-weight:700}}
.btn{{display:inline-block;background:var(--heat);color:var(--hi);font-weight:700;padding:14px 24px;border-radius:12px;text-decoration:none;margin-top:28px}}
</style></head><body>
<header><a href="index.html">INOX ESTAY</a><span class="tel"><a href="tel:+34658928308">658 92 83 08</a><a href="tel:+34680663605">680 66 36 05</a></span></header>
<main><h1>Trabajos realizados</h1><p class="lede">Trabajos reales en embarcaciones de Valencia y alrededores.</p>
<div class="grid">{"".join(cards)}</div>
<a class="btn" href="presupuesto.html">Solicitar presupuesto</a></main></body></html>
'''
open('trabajos.html','w',encoding='utf-8').write(page)
sm=open('sitemap.xml').read(); sm=re.sub(r'\s*<url>\s*<loc>https://inoxestay.es/trabajos.html</loc>.*?</url>','',sm,flags=re.S)
if index: sm=sm.replace('</urlset>','  <url>\n    <loc>https://inoxestay.es/trabajos.html</loc>\n    <priority>0.8</priority>\n  </url>\n</urlset>')
open('sitemap.xml','w').write(sm)
print(len(cards),'trabajos;','indexable' if index else 'noindex (faltan fotos)')

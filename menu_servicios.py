"""Inserta el menú desplegable "Servicios" en la cabecera de todas las páginas. Idempotente."""
import glob, re
NAUT = [('pasamanos-candeleros-inoxidable-valencia', 'Candeleros y pasamanos'), ('arcos-popa-soportes-equipamiento-inoxidable', 'Arcos y soportes'),
        ('davits-soportes-motor-fueraborda-inoxidable', 'Davits y soportes de motor'), ('herrajes-piezas-a-medida-inoxidable-nautico', 'Herrajes a medida'),
        ('recuperacion-pasivado-inoxidable-barcos', 'Tratamiento contra el salitre'), ('soldadura-inoxidable-in-situ-valencia', 'Soldadura in situ')]
GEN = [('barandillas-inox-valencia', 'Barandillas y pasamanos'), ('rejas-puertas-hierro-valencia', 'Rejas, puertas y estructuras'),
       ('mesas-campanas-fregaderos-inox-valencia', 'Mesas, campanas y fregaderos'), ('soldador-domicilio-valencia', 'Soldador a domicilio')]
li = lambda L: ''.join(f'<a href="{s}.html">{t}</a>' for s, t in L)
MENU = ('<details class="svc-menu"><summary>Servicios</summary><div class="svc-menu-pop">'
        f'<b>Barcos</b>{li(NAUT)}<b>Hogar y negocio</b>{li(GEN)}<b>Más</b><a href="presupuesto.html">Pedir presupuesto</a></div></details>')
CSS = ('<style id="svc-menu-css">.svc-menu{position:relative;display:inline-block;margin:0 12px;border:0!important;padding:0!important}'
       '.svc-menu summary{display:inline-block;white-space:nowrap;line-height:1.4;color:inherit;cursor:pointer;list-style:none;font-weight:600;padding:4px 10px;border:1px solid currentColor;border-radius:6px;font-size:.9rem}'
       '.svc-menu summary::-webkit-details-marker{display:none}.svc-menu summary::after{content:" ▾"}'
       '.svc-menu-pop{position:absolute;z-index:50;top:calc(100% + 8px);left:0;min-width:240px;background:#fff;color:#14181a;border:1px solid #d8dcda;border-radius:10px;box-shadow:0 10px 30px rgba(0,0,0,.18);padding:8px 0;display:flex;flex-direction:column}'
       '.svc-menu-pop b{font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:#8b9296;padding:8px 16px 4px}'
       '.svc-menu-pop a{color:#14181a!important;text-decoration:none;padding:7px 16px;font-weight:500!important;margin:0!important;font-size:.92rem!important}'
       '.svc-menu-pop a:hover{background:#f5f6f5;color:#b5813e!important}'
       '@media(max-width:700px){.svc-menu{position:static;margin:0 6px}.svc-menu-pop{position:fixed;left:12px;right:12px;top:auto;min-width:0;max-height:70vh;overflow:auto}}</style>')
def apply(s):
    s = re.sub(r'<details class="svc-menu">.*?</details>', '', s, flags=re.S)
    s = re.sub(r'<style id="svc-menu-css">.*?</style>', '', s, flags=re.S)
    if '<header><a href="index.html">INOX ESTAY</a>' in s:
        s = s.replace('<header><a href="index.html">INOX ESTAY</a>', '<header><a href="index.html">INOX ESTAY</a>' + MENU, 1)
    elif '<div class="header-phones">' in s:
        s = s.replace('<div class="header-phones">', MENU + '\n    <div class="header-phones">', 1)
    else:
        return s, False
    s = s.replace('</head>', CSS + '\n</head>', 1) if '</head>' in s else s.replace('<header', CSS + '\n<header', 1)
    return s, True
if __name__ == '__main__':
    for f in sorted(glob.glob('*.html')):
        s, ok = apply(open(f, encoding='utf-8').read())
        if ok: open(f, 'w', encoding='utf-8').write(s)
        print(('ok ' if ok else '-- ') + f)

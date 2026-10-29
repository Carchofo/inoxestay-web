"""Genera las páginas de servicios generales (no náuticos) a partir de la plantilla in situ."""
import json, re
TPL = open('soldadura-inoxidable-in-situ-valencia.html', encoding='utf-8').read()
HEAD_STYLE = TPL[TPL.index('<link rel="icon"'):TPL.index('</head>')]
HEAD_STYLE = re.sub(r'<script type="application/ld\+json">.*?</script>\n', '', HEAD_STYLE, flags=re.S)
TEL = ['+34658928308', '+34680663605']
P = [
 dict(slug='barandillas-inox-valencia', crumb='Barandillas y pasamanos',
  title='Barandillas y pasamanos de inox y hierro en Valencia',
  desc='Fabricación, instalación y reparación de barandillas y pasamanos de acero inoxidable y hierro para escaleras, terrazas y balcones en Valencia. Presupuesto gratis.',
  img='tig-tubo.jpg',
  body=['Fabricamos, instalamos y reparamos barandillas y pasamanos de acero inoxidable y de hierro para escaleras, terrazas, balcones, rampas y comunidades de vecinos.',
        'Tomamos medidas en el sitio y fabricamos a medida. En inoxidable usamos soldadura TIG con acabado pulido o satinado; en hierro, soldadura y acabado con imprimación y pintura.',
        'También reparamos barandillas existentes: anclajes sueltos, tramos doblados, soldaduras rotas u óxido. Acordamos la fecha antes de empezar y cumplimos los plazos.',
        'Envíenos fotos por WhatsApp y le damos una primera valoración sin compromiso.'],
  faq=[('¿Hacéis barandillas para comunidades de vecinos?','Sí. Trabajamos para particulares, comunidades y empresas. Le damos un presupuesto cerrado por escrito antes de empezar.'),
       ('¿Inox o hierro: cuál conviene?','El inoxidable no necesita pintura y aguanta mejor la humedad y el exterior. El hierro es más económico y se pinta del color que quiera. Le asesoramos según el uso y el presupuesto.'),
       ('¿Reparáis barandillas ya instaladas?','Sí: refuerzo de anclajes, sustitución de tramos, soldadura de piezas rotas y tratamiento del óxido.')],
  kw=['barandillas inox','pasamanos escalera','barandilla terraza']),
 dict(slug='rejas-puertas-hierro-valencia', crumb='Rejas, puertas y estructuras',
  title='Rejas, puertas, forjados y estructuras metálicas en Valencia',
  desc='Rejas, puertas, cancelas y estructuras metálicas de hierro y acero inoxidable a medida en Valencia. Fabricación, instalación y reparación con desplazamiento.',
  img='soldador-obra.jpg',
  body=['Fabricamos e instalamos rejas de ventana, puertas, cancelas, vallas y pequeñas estructuras metálicas de hierro o acero inoxidable, a medida.',
        'Reparamos también lo que ya tiene instalado: bisagras y cerrojos soldados de nuevo, barrotes rotos, marcos descuadrados u oxidados.',
        'De forma puntual hacemos trabajos de forjados y estructuras metálicas. Tenemos todas las homologaciones de soldadura al día.',
        'Nos desplazamos a su casa, local o nave. Acabados de calidad y fecha acordada antes de empezar: cumplimos los plazos.',
        'Mándenos fotos y medidas aproximadas por WhatsApp y le preparamos un presupuesto sin compromiso.'],
  faq=[('¿Hacéis rejas y puertas a medida?','Sí. Tomamos medidas en el sitio y fabricamos a medida en hierro o en acero inoxidable.'),
       ('¿Reparáis puertas y rejas viejas?','Sí: soldadura de piezas rotas, cambio de bisagras, refuerzos y tratamiento del óxido antes de pintar.'),
       ('¿Hacéis forjados y estructuras?','Sí, de forma puntual, con todas las homologaciones de soldadura al día. Cuéntenos el proyecto y lo valoramos.')],
  kw=['rejas a medida','puerta de hierro','estructura metálica']),
 dict(slug='mesas-campanas-fregaderos-inox-valencia', crumb='Mesas, campanas y fregaderos inox',
  title='Mesas, campanas y fregaderos de acero inoxidable a medida en Valencia',
  desc='Mesas de trabajo, campanas extractoras, fregaderos, encimeras y estanterías de acero inoxidable a medida en Valencia. Fabricación y reparación.',
  img='tornillos.jpg',
  body=['Fabricamos y reparamos piezas de acero inoxidable a medida: mesas de trabajo, campanas extractoras, fregaderos, encimeras, estanterías y soportes.',
        'Cuando una pieza de serie no encaja en el hueco, la hacemos a medida. Y si algo se rompe (una pata, una soldadura, un soporte), lo reparamos sin cambiar el mueble entero.',
        'Somos especialistas en inoxidable: soldadura TIG y acabado limpio, pulido o satinado. Acordamos el plazo y lo cumplimos.',
        'Envíenos fotos y medidas por WhatsApp y le decimos si se repara o conviene hacer pieza nueva.'],
  faq=[('¿Hacéis mesas y fregaderos de inox a medida?','Sí. Fabricamos a la medida del hueco, con los senos, estantes y el acabado que necesite.'),
       ('¿Reparáis campanas y muebles de inox?','Sí: soldadura de piezas rotas, refuerzos de patas y soportes, y sustitución de partes dañadas.'),
       ('¿Qué acabado tiene el inox?','Pulido, satinado o cepillado, según el uso y lo que prefiera. Se lo enseñamos antes de empezar.')],
  kw=['mesa acero inoxidable','campana extractora inox','fregadero inox a medida']),
 dict(slug='soldador-domicilio-valencia', crumb='Soldador a domicilio',
  title='Soldador a domicilio en Valencia: reparaciones de inox y hierro',
  desc='Soldador a domicilio en Valencia para pequeñas reparaciones de inox, hierro, aluminio y otros metales: rejas, puertas, barandillas, muebles, soportes y piezas rotas.',
  img='soldador-casco.webp',
  body=['¿Se ha roto una reja, una bisagra, la pata de una mesa o un soporte? Hacemos pequeñas reparaciones de soldadura en acero inoxidable, hierro, aluminio y otros metales, en su casa o local.',
        'Muchos talleres no aceptan trabajos pequeños. Nosotros sí: nos desplazamos, valoramos la pieza y la reparamos en el sitio cuando es posible.',
        'Soldamos todo tipo de metales y somos especialistas en inoxidable. Soldadura TIG o por electrodo según el material, con acabados de calidad. Le damos precio antes de empezar y cumplimos la fecha acordada.',
        'Mándenos una foto por WhatsApp y le decimos si tiene arreglo y cuánto cuesta aproximadamente.'],
  faq=[('¿Hacéis reparaciones pequeñas?','Sí. No hay trabajo demasiado pequeño: rejas, bisagras, patas de muebles, soportes, piezas rotas.'),
       ('¿Venís a casa?','Sí. Nos desplazamos por Valencia y alrededores. Si la pieza necesita taller, se lo decimos antes.'),
       ('¿Cuánto cuesta una reparación?','Depende de la pieza y del desplazamiento. Con una foto le damos una idea aproximada sin compromiso.')],
  kw=['soldador a domicilio','reparación soldadura','soldador valencia']),
]
OTROS = '<ul class="more">' + ''.join(f'<li><a href="{p["slug"]}.html">{p["crumb"]}</a></li>' for p in P) + \
 '<li><a href="index.html#servicios">Soldadura inox para barcos</a></li></ul>'
for p in P:
    url = f'https://inoxestay.es/{p["slug"]}.html'
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Service", "name": p['crumb'], "description": p['desc'],
         "provider": {"@type": "LocalBusiness", "name": "INOX ESTAY", "url": "https://inoxestay.es/", "telephone": TEL},
         "areaServed": {"@type": "City", "name": "Valencia"}, "url": url},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://inoxestay.es/"},
            {"@type": "ListItem", "position": 2, "name": p['crumb'], "item": url}]},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p['faq']]}]}
    html = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p["title"]} | INOX ESTAY</title>
<meta name="description" content="{p["desc"]}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0d151d">
<meta property="og:title" content="{p["title"]} | INOX ESTAY"><meta property="og:description" content="{p["desc"]}">
<meta property="og:image" content="https://inoxestay.es/img/{p["img"]}"><meta property="og:url" content="{url}"><meta property="og:locale" content="es_ES">
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=1)}
</script>
{HEAD_STYLE}</head>
<body>
<header><a href="index.html">INOX ESTAY</a><span class="tel"><a href="tel:+34658928308">658 92 83 08</a><a href="tel:+34680663605">680 66 36 05</a></span></header>
<main>
  <div class="crumb"><a href="index.html">Inicio</a> › {p["crumb"]}</div>
  <h1>{p["title"]}</h1>
''' + ''.join(f'  <p>{t}</p>\n' for t in p['body']) + '''  <a class="btn" href="presupuesto.html">Solicitar presupuesto</a>
  <h2>Preguntas frecuentes</h2>
''' + ''.join(f'  <details><summary>{q}</summary><p>{a}</p></details>\n' for q, a in p['faq']) + f'''  <h2>Otros trabajos</h2>
  {OTROS}
</main>
<footer>INOX ESTAY · Soldadura de inox y hierro en Valencia · <a href="tel:+34658928308">658 92 83 08</a></footer>
</body>
</html>
'''
    open(f'{p["slug"]}.html', 'w', encoding='utf-8').write(html)
    print(p['slug'])

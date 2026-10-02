import openpyxl, html, base64
logo=base64.b64encode(open('logo-corteza.png','rb').read()).decode()
wb=openpyxl.load_workbook('/root/.claude/uploads/ee622b5e-8e2f-54d1-b07f-83c1a1f61f31/61093650-Precio_Mayorista_clientes_sept.xlsx')
ws=wb.active
def money(v): return '$'+f"{round(v):,}".replace(',','.')
trs=[]
for r in ws.iter_rows(min_row=4, values_only=True):
    if not r[0]: continue
    if r[2]=='10 Minimo': continue
    name,pres,mn,price=r[0].strip(),r[1],r[2],r[3]
    mn=mn.replace('10 Minimo','10 unidades')
    note=''
    if '(' in name:
        name,note=name.split('(',1); name=name.strip(); note=note.rstrip(')').strip()
        note=note[0].upper()+note[1:]
    nd='<div class=note>'+html.escape(note)+'</div>' if note else ''
    trs.append("<tr><td class=p>%s%s</td><td>%s</td><td>%s</td><td class=num>%s</td></tr>"%(html.escape(name),nd,html.escape(pres),html.escape(mn),money(price)))
css="""@page { size:A4; margin:0 }
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Liberation Sans',Arial,sans-serif;color:#2b2420;width:210mm;padding:16mm 16mm 12mm;font-size:10pt;background:#fff}
.top{border-bottom:3px solid #8a5a2b;padding-bottom:10px;margin-bottom:10px;display:flex;justify-content:space-between;align-items:flex-end;gap:16px}
.logo{height:30px;margin-bottom:10px}
.contact{text-align:right;font-size:9.5pt;color:#4a3a2c;line-height:1.5}
.contact b{color:#5a3a1c}
h1{font-size:22pt;color:#5a3a1c;letter-spacing:.3px}
.sub{color:#7a6a5c;font-size:10.5pt;margin-top:3px}
.claim{background:#f5ede3;border-left:4px solid #8a5a2b;padding:8px 12px;margin:10px 0 14px;font-size:10pt;color:#4a3a2c}
table{width:100%;border-collapse:collapse}
th{background:#5a3a1c;color:#fff;text-align:left;font-size:9pt;text-transform:uppercase;letter-spacing:.8px;padding:7px 9px}
th.num,td.num{text-align:right}
td{padding:7px 9px;border-bottom:1px solid #e6dcd0;vertical-align:top}
tr:nth-child(even) td{background:#faf6f1}
td.p{font-weight:700}
td.num{font-weight:700;color:#5a3a1c;white-space:nowrap}
.note{font-weight:400;font-size:8.5pt;color:#7a6a5c;margin-top:2px}
.foot{margin-top:12px;font-size:8.5pt;color:#7a6a5c}"""
doc="""<!doctype html><html lang=es><head><meta charset=utf-8><title>Lista de precios mayorista</title><style>%s</style></head><body>
<div class=top><div><img class=logo src='data:image/png;base64,%s'><h1>Lista de precios mayorista</h1><div class=sub>Vigencia: 15 de septiembre al 15 de octubre de 2026</div></div><div class=contact><b>Pedidos</b><br>WhatsApp: 11 4419-1644<br>juanguerrini96@gmail.com</div></div>
<div class=claim>Todos nuestros productos son realizados con harinas agroecológicas y calidad de primer nivel.</div>
<table><thead><tr><th>Producto</th><th>Presentación</th><th>Compra mínima</th><th class=num>Precio unitario</th></tr></thead><tbody>%s</tbody></table>
<div class=foot>Precios mayoristas por unidad. Pedidos por WhatsApp al 11 4419-1644 o a juanguerrini96@gmail.com.</div>
</body></html>"""%(css,logo,''.join(trs))
open('lista-mayorista-oct-2026.html','w').write(doc)

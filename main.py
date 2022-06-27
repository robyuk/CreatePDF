from fpdf import FPDF

pdf=FPDF(orientation='P',unit='pt',format='A4')
pdf.add_page()

pdf.image('tiger.jpeg',w=400, h=250, x=80)
pdf.set_font(family='Times', style='B', size=24)
pdf.cell(w=0, h=20, txt='Malayan Tiger', align='C', border=1, ln=1)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=0, h=30, txt='Description', ln=1)

pdf.set_font(family='Times', size=12)
txt1="""The Malayan tiger is a tiger from a specific population of the Panthera tigris tigris subspecies that is native to Peninsular Malaysia.[1] This population inhabits the southern and central parts of the Malay Peninsula and has been classified as critically endangered on the IUCN Red List since 2015. As of April 2014, the population was estimated at 80 to 120 mature individuals with a continuous declining trend.[2]

In the Malay language, the tiger is called harimau, also abbreviated to rimau.[3] It is also known as the southern Indochinese tiger, to distinguish it from tiger populations in northern parts of Indochina, which are genetically different to this population.
"""
pdf.multi_cell(w=0, h=15, txt=txt1)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=30, txt='Kingdom:')
pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=30, txt='Animalia', ln=1)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=30, txt='Phylum:')
pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=30, txt='Chordata', ln=1)

pdf.output('tiger.pdf')

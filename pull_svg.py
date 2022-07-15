import os.path
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
from PyPDF2 import PdfMerger

SCORE = r'C:\Users\bv2cq\Downloads\score_' # Download Path
RENDER = r'Render\score_' # Destination path (relative to MusescoreExtractor)

score_num = 0
pdf_list = []
while(os.path.exists(SCORE + str(score_num) + '.svg')):
    drawing = svg2rlg(SCORE + str(score_num) + '.svg')
    renderPDF.drawToFile(drawing, RENDER + str(score_num) + '.pdf')
    pdf_list.append(RENDER + str(score_num) + '.pdf')
    os.remove(SCORE + str(score_num) + '.svg')
    score_num += 1

merger = PdfMerger()

for pdf in pdf_list:
    merger.append(pdf)
merger.write(r"Render\final_score.pdf")
merger.close()

#Cleanup intermediary files
score_num = 0
while(os.path.exists(RENDER + str(score_num) + '.pdf')):
    os.remove(RENDER + str(score_num) + '.pdf')
    score_num += 1
    
    




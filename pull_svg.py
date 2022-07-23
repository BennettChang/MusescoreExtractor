import os.path
from os import path
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
from PyPDF2 import PdfMerger

def svgs_to_pdf(download_path):
    SCORE= download_path + '\score_'
    score_num = 0
    pdf_list = []
    
    while(os.path.exists(SCORE + str(score_num) + '.svg')):
        drawing = svg2rlg(SCORE + str(score_num) + '.svg')
        renderPDF.drawToFile(drawing, SCORE+ str(score_num) + '.pdf')
        pdf_list.append(SCORE + str(score_num) + '.pdf')
        os.remove(SCORE + str(score_num) + '.svg')
        score_num += 1

    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)

    # Prevents existing final_scores from being overrided
    counter = 1
    if path.isfile(download_path + "/final_score.pdf"): 
        while path.isfile(download_path + "/final_score(" + str(counter) + ").pdf"):
            counter += 1
        merger.write(download_path + "/final_score(" + str(counter) + ").pdf")
    else:
        merger.write(download_path + "/final_score.pdf")
    merger.close()

    # Cleanup intermediary files
    score_num = 0
    while(os.path.exists(SCORE + str(score_num) + '.pdf')):
        os.remove(SCORE + str(score_num) + '.pdf')
        score_num += 1
    
    




import io
import re

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
        interpreter.process_page(page)



    fp.close()
    device.close()
    text = retstr.getvalue()
    retstr.close()
    return text


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""
        


path_pdf = 'C:\\Users\\Snades\\Desktop\\roteiros\\roteiro1.pdf'

screenPlay = convert_pdf_to_txt(path_pdf)
block = screenPlay.split('\n')
scenes_header = []
scenes_header_numbered = [] #tem o número da cena antes ---> para organizar depois no front-end!
scenes = []
count = 1

for line in block:
    if 'EXT.' in line:
        scenes_header.append(line)
        scenes_header_numbered.append(f'Cena {count} - ' + line)
        count += 1
    elif 'INT.' in line:
        scenes_header.append(line)
        scenes_header_numbered.append(f'Cena {count} - ' + line)
        count += 1


for i in range(len(scenes_header) - 1):
    scene = find_between(screenPlay, scenes_header[i], scenes_header[i+1])
    scene = scenes_header[i] + '\n' + scene
    scenes.append(scene)

print(scenes[0])


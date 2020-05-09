import io
import re

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


class ScriptMiner(PDFPageInterpreter, PDFResourceManager, TextConverter,LAParams,PDFPage):
    def __init__(self, path):
        self.path = path
        #super.__init__()

    def convert_pdf_to_txt(self):
        rsrcmgr = PDFResourceManager()
        retstr = io.StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        fp = open(self.path, 'rb')
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


    def scenesList(self):
        screenPlay = self.convert_pdf_to_txt()
    
        block = screenPlay.split('\n')
        scenes_header = []
        scenes = []

        for line in block:
            if 'EXT.' in line:
                scenes_header.append(line)
            elif 'INT.' in line:
                scenes_header.append(line)
        
        for i in range(len(scenes_header) - 1):
            try:
                start = screenPlay.index(scenes_header[i]) + len(scenes_header[i])
                end = screenPlay.index(scenes_header[i + 1], start)
                s = screenPlay[start:end]

                scene = scenes_header[i] + '\n' + s
                scenes.append(scene)                
            except ValueError:
                scenes.append("")
        
        return scenes


    def scenesHeaderNumbered(self): #precisa tratar os espaços em branco nas headers!
        screenPlay = self.convert_pdf_to_txt()
    
        block = screenPlay.split('\n')
        scenes_header_numbered = []
        count = 1

        for line in block:
            if 'EXT.' in line:
                scenes_header_numbered.append(f'Cena {count} - ' + line)
                count += 1
            elif 'INT.' in line:
                scenes_header_numbered.append(f'Cena {count} - ' + line)
                count += 1

        return scenes_header_numbered

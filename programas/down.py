import os
import shutil
import time,schedule
imagens=('jpg','png','gif')
documentos=('docx','odt','txt','asm','csv','epub')
programas=('.pdsprj','.c','iso','exe','py','dwf','xps','dwfx')
zip=('zip')
videos=('mp3','mp4','AVI')
pdf=('pdf')
pwp=('ppt','pptx','pptjpg','pptpng')
exc=('xls','xlsx','odf')
arquivos=[r'\videos',r'\imagens',r'\programas',r'\zip',r'\documentos',r'\powerpoint',r'\excel',r'\pdfs']
path= r'C:\Users\Dell\Downloads'
def organize_file():
    def create_file(nome):
        try:
            os.mkdir(path + nome)
        except FileExistsError:
            a=1
    def change_file(archive,file):
            shutil.move(path+'\\'+archive,path+file)
    os.chdir(path)
    for i in range (0,len(arquivos)):
        create_file(arquivos[i])
    files=os.listdir(path)
    for f in files :
        if f.endswith(zip):
            change_file(f,r'\zip')
        elif f.endswith(documentos):
            change_file(f,r'\documentos')
        elif f.endswith(imagens):
            change_file(f,r'\imagens')
        elif f.endswith(videos):
            change_file(f,r'\videos')
        elif f.endswith(pdf):
            change_file(f,r'\pdfs')
        elif f.endswith(pwp):
            change_file(f,r'\powerpoint')
        elif f.endswith(exc):
            change_file(f,r'excel')

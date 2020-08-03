import os
import shutil

imagens = ('jpg', 'png', 'gif', 'ico')
documentos = ('docx', 'odt', 'txt', 'asm', 'csv', 'epub','.doc','.mif')
programas = ('.pdsprj', '.c', '.iso', '.exe', '.py', '.dwf', '.xps', '.dwfx', 'dll')
zip = ('zip', 'rar', '.tar', '7zip')
videos = ('mp4', 'AVI', 'wmv', 'mov')
audio = ('mp3', 'm4a', 'wav', 'ogg')
pdf = ('pdf')
pwp = ('ppt', 'pptx', 'pptjpg', 'pptpng')
exc = ('xls', 'xlsx', 'odf')
arquivos = [r'\videos', r'\imagens', r'\programas', r'\zip', r'\documentos', r'\powerpoint', r'\excel', r'\pdfs',
            r'\audio']
path = r'C:\Users\Dell\Downloads'


def create_file(nome):
    try:
        os.mkdir(path + nome)
    except FileExistsError:
        a = 1


def change_file(archive, file):
    shutil.move(path + '\\' + archive, path + file)


os.chdir(path)
for i in range(0, len(arquivos)):
    create_file(arquivos[i])
files = os.listdir(path)
for f in files:
    if f.endswith(zip):
        change_file(f, r'\zip')
    elif f.endswith(documentos):
        change_file(f, r'\documentos')
    elif f.endswith(imagens):
        change_file(f, r'\imagens')
    elif f.endswith(videos):
        change_file(f, r'\videos')
    elif f.endswith(pdf):
        change_file(f, r'\pdfs')
    elif f.endswith(pwp):
        change_file(f, r'\powerpoint')
    elif f.endswith(exc):
        change_file(f, r'excel')
    elif f.endswith(programas):
        change_file(f, r'\programas')
    elif f.endswith(audio):
        change_file(f, r'\audio')

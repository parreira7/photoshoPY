#{} []
import win32com.client
import os
from os.path import exists
psApp = win32com.client.Dispatch("Photoshop.Application")
psApp.Open(r"C:\Users\Administrator\Desktop\Python\photoshoPY\thumnail_P.psd")  #mudar no seu pc
doc = psApp.Application.ActiveDocument

layerText = doc.ArtLayers["NOME1"] #selecionando a layer com o nome especifico
layerText1 = doc.ArtLayers["NOME2"] #selecionando a layer com o nome especifico
layerText2 = doc.ArtLayers["NOME3"] #selecionando a layer com o nome especifico
layerText2.visible = True # caso a layer do nome 3 esteja escondida, vai mostrar

texto_layer = layerText.TextItem #listar como texto
texto_layer1 = layerText1.TextItem #listar como texto
texto_layer2 = layerText2.TextItem #listar como texto

texto_layer.contents = "abcd" #trocar o texto dentro das aspas (AQUI ONDE A MAGICA ACONTECE BICHO)
texto_layer1.contents = "abcd 1" #trocar o texto dentro das aspas (AQUI ONDE A MAGICA ACONTECE BICHO)
texto_layer2.contents = "abcd 2" #trocar o texto dentro das aspas (AQUI ONDE A MAGICA ACONTECE BICHO)

save = win32com.client.Dispatch('Photoshop.ExportOptionsSaveForWeb') #selecionando a funçao de exportar 
save.Format = 13 # formato que no caso, o png vale 13 na tabela
save.PNG8 = False # seta como png 24-bit
pngfile = (r"C:\Users\Administrator\Desktop\Python\photoshoPY\thumb.png") #lugar e nome onde a thumb irá ser salva
doc.Export(ExportIn=pngfile, ExportAs=2, Options=save) #chamando a funçao com tudo já setado (path, formato etc)

#checar se o arquivo existe e fechar o programa
arquivo_existe = os.path.exists(r'C:\Users\Administrator\Desktop\Python\photoshoPY\thumb.png') #mudar no seu pc
print(arquivo_existe)#printa se existe ou nao
if (arquivo_existe == True): #se existir vai fechar
    doc = psApp.Application.ActiveDocument.Close(1) #salvar e fechar o .psd
    psApp.Quit() #fechar o photoshop

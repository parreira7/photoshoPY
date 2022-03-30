import win32com.client
import os
psApp = win32com.client.Dispatch("Photoshop.Application")
psApp.Open(r"C:\Users\Administrator\Desktop\Python\photoshoPY\thumnail_P.psd") #(MUDAR NO SEU PC)
doc = psApp.Application.ActiveDocument

layerText = doc.ArtLayers["NOME1"] #selecionando a layer com o nome especifico
layerText1 = doc.ArtLayers["NOME2"] #selecionando a layer com o nome especifico
texto_layer = layerText.TextItem #listar como texto
texto_layer1 = layerText1.TextItem #listar como texto
texto_layer.contents = "mc X" #trocar o texto
texto_layer1.contents = "mc Y" #trocar o texto
save = win32com.client.Dispatch('Photoshop.ExportOptionsSaveForWeb') #selecionando a funçao de exportar 
save.Format = 13 # formato que no caso, o png vale 13 na tabela
save.PNG8 = False # seta como png 24-bit
pngfile = (r"C:\Users\Administrator\Desktop\Python\photoshoPY\thumb.png") #lugar e nome onde a thumb irá ser salva (MUDAR NO SEU PC)
doc.Export(ExportIn=pngfile, ExportAs=2, Options=save) #chamando a funçao com tudo já setado (path, formato etc)

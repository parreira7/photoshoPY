#{} []
import win32com.client
import os
psApp = win32com.client.Dispatch("Photoshop.Application") #chamando o photoshop p abrir
psApp.Open(r"C:\Users\Administrator\Desktop\Python\photoshoPY\thumnail_P.psd") #abrindo o .psd com o path correto (MUDAR NO SEU PC)
doc = psApp.Application.ActiveDocument #usado no final p exportaçao nesse caso

layerText = doc.ArtLayers["NOME1"] #selecionando a layer com o nome especifico
layerText1 = doc.ArtLayers["NOME2"] #selecionando a layer com o nome especifico
layerText2 = doc.ArtLayers["NOME3"] #selecionando a layer com o nome especifico
texto_layer = layerText.TextItem #listar como texto
texto_layer1 = layerText1.TextItem #listar como texto
texto_layer2 = layerText2.TextItem #listar como texto
texto_layer.contents = "teste" #trocar o texto
texto_layer1.contents = "teste 1" #trocar o texto
texto_layer2.contents = "teste 2" #trocar o texto

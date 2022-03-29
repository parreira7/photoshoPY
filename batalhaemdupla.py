import win32com.client
import os
psApp = win32com.client.Dispatch("Photoshop.Application")
psApp.Open(r"C:\Users\Administrator\Desktop\Python\photoshoPY\thumnail_P.psd")
doc = psApp.Application.ActiveDocument

layerText = doc.ArtLayers["NOME1"] #selecionando a layer com o nome especifico
layerText1 = doc.ArtLayers["NOME2"] #selecionando a layer com o nome especifico
texto_layer = layerText.TextItem #listar como texto
texto_layer1 = layerText1.TextItem #listar como texto
texto_layer.contents = "mc X" #trocar o texto
texto_layer1.contents = "mc Y" #trocar o texto

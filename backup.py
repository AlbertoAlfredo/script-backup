from datetime import datetime
import shutil
import os
import json


# Função que lê o Json
def ler_json(arq_json):
    with open(arq_json, 'r', encoding='utf8') as f:
        return json.load(f)
data = ler_json('config-backup.json')
origem = data['origem'].replace("/", "\\")
destino = data['destino'].replace("/", "\\")

#destino = 'd:\\backup'
#origem = "C:\\Versátil\\Versátile Expert\\dados_sposto.fdb"
data_e_hora = datetime.now().strftime('%d-%m-%Y-%H%M%S')
nome_do_arquivo = "dados_sposto.fdb"
if (data['usar-data-hora']):
    nome_arquivo_zip = data_e_hora+nome_do_arquivo
else:
    nome_arquivo_zip = nome_do_arquivo


#shutil.make_archive(nome_arquivo_zip, 'zip','.\\', origem)
#shutil.move(".\\"+nome_arquivo_zip+".zip", destino)
#print("Backup efetuado com sucesso \n")
#input("Precione enter para finalizar..........")


try:
    if os.path.exists(destino):
        shutil.make_archive(nome_arquivo_zip, 'zip','.\\', origem)
        shutil.move(".\\"+nome_arquivo_zip+".zip", destino)
        print("Backup efetuado com sucesso \n")
    else:
        try:
            os.mkdir(destino)
            shutil.make_archive(nome_arquivo_zip, 'zip','.\\', origem)
            shutil.move(".\\"+nome_arquivo_zip+".zip", destino)
        except:
            print("Erro ao criar o diretório de bakup, favor verificar o destino")
            input("Precione enter para finalizar..........")
        print("Backup efetuado com sucesso")
except:
    print("Erro inesperado, cheque o caminho de origem \n")
    input("Precione enter para finalizar..........")
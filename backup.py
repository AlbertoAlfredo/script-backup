from datetime import datetime
import shutil
import os

destino = 'd:\\backup'
origem = "C:\Versátil\Versátile Expert\dados_sposto.fdb"
data_e_hora = datetime.now().strftime('%d-%m-%Y-%H%M')
nome_do_arquivo = "dados_sposto.fdb"
nome_arquivo_zip = data_e_hora+nome_do_arquivo

try:
    if os.path.exists(destino):
        shutil.make_archive(nome_arquivo_zip, 'zip','.\\', origem)
        shutil.move(".\\"+nome_arquivo_zip+".zip", destino)
        print("Backup efetuado com sucesso \n")
        input("Precione enter para finalizar..........")
    else:
        try:
            os.mkdir(destino)
        except:
            print("Erro ao criar o diretório de bakup, favor verificar o destino")
            input("Precione enter para finalizar..........")
        shutil.make_archive(nome_arquivo_zip, 'zip','.\\', origem)
        shutil.move(".\\"+nome_arquivo_zip+".zip", destino)
        print("Backup efetuado com sucesso \n")
        input("Precione enter para finalizar..........")
except:
    print("Erro inesperado, cheque o caminho de origem \n")
    input("Precione enter para finalizar..........")
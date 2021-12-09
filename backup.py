from datetime import datetime
import shutil
import os


data_e_hora = datetime.now().strftime('%d-%m-%Y-%H%M')
origem = "C:\Versátil\Versátile Expert\dados_sposto.fdb"
nome_do_arquivo = "dados_sposto.fdb"
destino = 'd:\\backups'
try:
    if os.path.exists(destino):
        shutil.make_archive(data_e_hora+nome_do_arquivo, 'zip', destino, origem)
        print("Backup efetuado com sucesso \n")
        input("Precione enter para finalizar..........")
    else:
        try:
            os.mkdir(destino)
        except:
            print("Erro ao criar o diretório de bakup, favor verificar o destino")
            input("Precione enter para finalizar..........")
        shutil.make_archive(data_e_hora+nome_do_arquivo, 'zip', destino, origem)
        print("Backup efetuado com sucesso \n")
        input("Precione enter para finalizar..........")
except:
    print("Erro inesperado, cheque o caminho de origem \n")
    input("Precione enter para finalizar..........")
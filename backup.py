from datetime import datetime
import shutil


data_e_hora = datetime.now().strftime('%d-%m-%Y-%H%M')
origem = "C:\Versátil\Versátile Expert\dados_sposto.fdb"
nome_do_arquivo = "dados_sposto.fdb"
destino = 'd:/backups'
shutil.make_archive(data_e_hora+nome_do_arquivo, 'zip', destino, origem)
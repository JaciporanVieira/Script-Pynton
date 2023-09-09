import os
import shutil
import zipfile

def unzip(zip_file, destination_folder):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(destination_folder)

def move_files(source_folder, destination_folder):
    for root, _, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith('.jpg'):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, file)
                shutil.move(source_path, destination_path)

def generate_report(report_file, source_folder):
    with open(report_file, 'w') as f:
        for root, _, files in os.walk(source_folder):
            folder_name = os.path.basename(root)
            file_count = len([file for file in files if file.lower().endswith('.jpg')])
            f.write(f"Pasta: {folder_name}, Quantidade de Arquivos JPG: {file_count}\n")

# Pasta onde os arquivos ZIP estão
input_folder = "Caminho/Para/Arquivos_ZIP"

# Pasta onde os arquivos descompactados serão temporariamente armazenados
output_folder = "Caminho/Para/PastaTemporaria"

# Pasta onde os arquivos JPG serão movidos
destination_folder = "P:/Detran/ControleImpressaoNovo/Imagens - Teste em Python"

# Pasta onde os relatórios serão armazenados
report_folder = "Caminho/Para/Relatorios"

# Criação da pasta temporária se não existir
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Lista os arquivos ZIP na pasta de entrada
zip_files = [file for file in os.listdir(input_folder) if file.lower().endswith('.zip')]

for zip_file in zip_files:
    zip_path = os.path.join(input_folder, zip_file)

    # Descompacta o arquivo ZIP na pasta temporária
    unzip(zip_path, output_folder)

    # Move os arquivos JPG para a pasta de destino
    move_files(output_folder, destination_folder)

    # Gera o nome do arquivo de relatório
    report_file_name = f"Confere_{zip_file[:-4]}_{zip_file[-12:-4]}.txt"
    report_file = os.path.join(report_folder, report_file_name)

    # Gera o relatório
    generate_report(report_file, destination_folder)

    print(f"Arquivo {zip_file} processado. Relatório gerado.")

# Remover a pasta temporária após o processamento
shutil.rmtree(output_folder)

print("Processo concluído.")

import os
def delete_psd_files(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".psd"):
                file_path = os.path.join(root, file)
                print("Usunięcie pliku:", file_path)
                os.remove(file_path)
folder_to_scan = input("Podaj ścieżkę do folderu, by usunąć pliki PSD: ")
delete_psd_files(folder_to_scan)
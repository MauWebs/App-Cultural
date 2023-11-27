import os
import time

while True:
    backup_folder = './backup/'
    backup_files = os.listdir(backup_folder)

    print(f'Contenido del directorio {backup_folder}:')
    for file in backup_files:
        print(f'- {file}')

    time.sleep(20)
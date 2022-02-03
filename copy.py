import shutil
import sys
import os

directories = [f for f in sorted(os.listdir(r'ur\path'))]
var = 1


def copy():
    if len(directories) == 0:
        print('Work done!')
        sys.exit()
    else:
        shutil.copyfile(r'ur\path\file_name.txt',  # Путь к файлу который небходимо копировать
                        f'ur\\path\\dir_{var}\\file_name.txt')  # Дректории в которые необходимо копировать файл
        del directories[0]


while True:
    copy()
    var += 1

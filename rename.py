import os
import sys

files_list = []
files = [f for f in sorted(os.listdir('ur_path'))] # если ur_path пустой, берет данные с текущей директории
files_list.remove('rename.py')
var = 1

def rename():
    if len(files_list) == 0:
        print("[+]Work done!")
        sys.exit()
    else:
        name = f'{var}'
        os.rename(files_list[0], name)
        del fl[0]


while True:
    rename()
    var += 1

import os
import sys

files = [f for f in sorted(os.listdir('ur_path'))] # если ur_path пустой, берет данные с текущей директории
files.remove('rename.py')
var = 1


def rename():
    if len(files) == 0:
        print("[+]Work done!")
        sys.exit()
    else:
        name = f'{var}.txt'
        os.rename(files[0], name)
        del files[0]


while True:
    rename()
    var += 1





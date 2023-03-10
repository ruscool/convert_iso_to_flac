import os

from engine.links import sacd
from engine.verify_md5 import path_sacd, verify


def yes():
    return 'sacd installed'


def finding(path):
    os.chdir(path)
    folders = os.listdir('.')
    # print(os.system('ls -alth'))
    if 'sacd' in folders:
        verify(path_sacd)
        print(yes())
    else:
        os.system(f'git clone {sacd}')
        os.system(f'cd sacd && sudo -S make install')
        yes()


if __name__ == '__main__':
    finding(path_sacd)

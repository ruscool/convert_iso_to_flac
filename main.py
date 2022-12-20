import os
import argparse

# from engine import firstStep
from engine import verify_md5
from engine.firstStep import path_sacd, finding
from typing import Any
from pathlib import Path

version = '1.0.1'


def createParser():
    parser = argparse.ArgumentParser(
        prog='isotoflac',
        description="""Converter from ISO to flac format""",
        epilog="""(c) 2022 _R_R_ opensource"""
    )
    parser.add_argument('-i', default='.',
                        help='Path to folder:', metavar='Path')
    parser.add_argument('--version', '-V', action='version',
                        help='Number version', version='%(prog)s {}'.format(version))
    return parser


def work_convert():
    """Get folder and convert iso to wav"""
    parser = createParser()
    namespace = parser.parse_args()
    path = Path(namespace.i)
    return path


def zamena(new_file):
    print(f'in: {new_file}')
    perebor = new_file
    zamena = ['(', ')', ':', '-', '&', "'", ' ']
    count = len(zamena)
    file = []
    for m in range(count):
        for i in zamena[0]:
            if i in perebor:
                perebor = perebor.replace(i, f'\{i}')
            del zamena[0]
    return perebor


def find_iso(path_dir: str) -> Any:
    iso_files = []
    os.chdir(path_dir)
    # print(os.getcwd())
    for i in os.listdir(path_dir):
        # print(i)
        if i.endswith('iso'):
            iso_files.append(i)
            print(f'Find iso: {i}')
    if len(iso_files) > 0:
        return iso_files
    else:
        print(f'Not iso in folder')
        return 0


def convert_to_wav(path_dir, iso_file):
    print(f'*' * 30)
    print('[+] Step 1 - Convert to WAV')
    os.chdir(path_sacd)
    print(f'path: {path_dir}')
    convert_file = f'{path_dir}/{iso_file}'
    file = zamena(convert_file)
    os.chdir(f'{path_sacd}')
    print(f'{os.getcwd()}')
    cmd = f'./sacd -i {file} -s -r 192000'
    os.system(cmd)
    print("Convert to wav finished")
    return 1


def covert_to_flac(path_dir):
    """Converter to flac"""
    print('[+] Step 2 - convert to flac')
    files = []
    for i in os.listdir(path_dir):
        if i.endswith('wav'):
            files.append(i)
    os.chdir(path_dir)
    # zamena = [' ', '(', ')', ':', '-', '&']
    for file in files:
        file = zamena(file)
        cmd = f'ffmpeg -i {file} {file[:-4]}.flac'
        os.system(cmd)


def delete_file_wav(path_dir):
    """Delete all files in folder"""
    print('[+] Step 3 - delete WAV files')
    files = []
    os.chdir(path_dir)
    for i in os.listdir(path_dir):
        if i.endswith('wav'):
            files.append(i)
    for count in range(len(files)):
        print(f'Delete: {files[count]}')
        print(os.getcwd())
        os.remove(files[count])
    print(f'*' * 30)
    print(f'All ready')


if __name__ == '__main__':
    finding(path_sacd)
    path_folder = work_convert()
    # path_folder = '/home/rusdev/Music/BARBRA'  # for test
    iso_file = find_iso(path_folder)

    if iso_file != 0:
        res_wav = convert_to_wav(path_folder, iso_file[0])
        if res_wav:
            covert_to_flac(path_folder)
            delete_file_wav(path_folder)

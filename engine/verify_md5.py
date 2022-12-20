import hashlib

path_sacd = f'/home/rusdev/sacd'
md5 = '53983f73c11868cf63b7a0e0c5bc84d6'


def verify(file):
    with open(f'{file}/sacd', "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)

    # print(file_hash.digest())
    # print(file_hash.hexdigest())
    if md5 == file_hash.hexdigest():
        return 1


if __name__ == '__main__':
    res = verify(path_sacd)
    print(res)

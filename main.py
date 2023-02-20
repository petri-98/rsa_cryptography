import pathlib
from src.ascii_utils import text_to_int, int_to_text
from src.rsa_utils import generate_rsa_key, rsa_encrypt, rsa_decrypt


if __name__ == '__main__':
    print('Welcome to this RSA cryptography utility. Here you can:\n')
    print("[g] Generate keys.")
    print("[e] Encrypt a text.")
    print("[d] Decrypt a text.")
    print("[q] Quit.")

    mode = ''

    while mode != 'q':
        mode = str(input('\nWhat do you want to do? ')).lower()

        if mode == 'g':
            length = int(input('\nPlease, choose the length of the keys [512, 1024, 2048]: '))
            print('\nGenerating the keys...')
            pub_key, pvt_key = generate_rsa_key(length)
            write_file = ''

            key_name = str(input('\nPlease, enter the name of the key: '))
            keys_path = pathlib.Path('keys', key_name)
            keys_path.mkdir(parents=True, exist_ok=True)
            pub_key_path = pathlib.Path(keys_path, f'{key_name}_pub_key.txt')
            pvt_key_path = pathlib.Path(keys_path, f'{key_name}_pvt_key.txt')

            with open(pathlib.Path(pub_key_path, ), 'w') as f:
                f.writelines([str(el) + '\n' for el in pub_key])
            with open(pathlib.Path(pvt_key_path, ), 'w') as f:
                f.writelines([str(el) + '\n' for el in pvt_key])
            print(f'\nKeys files have been saved at the following path: {keys_path}')

        elif mode == 'e':
            text_fpath = pathlib.Path(input('Please, enter the path to the file to encrypt: '))
            if not text_fpath.exists():
                raise NameError('The text file does not exist!')
            pub_key_fpath = pathlib.Path(input('Please, enter the path to the public key file: '))
            if not pub_key_fpath.exists():
                raise NameError('The public key file does not exist!')

            with open(text_fpath, 'r') as f:
                lines = f.readlines()
            with open(pub_key_fpath, 'r') as f:
                pub_key = [int(x) for x in f.readlines()]

            encr_text_fpath = pathlib.Path(text_fpath.parent, f'encr_{text_fpath.name}')
            with open(pathlib.Path(encr_text_fpath, ), 'w') as f:
                f.writelines([str(rsa_encrypt(text_to_int(line), pub_key)) + '\n' for line in lines])
            print(f'Your encrypted text has been saved at the following path: {encr_text_fpath}')

        elif mode == 'd':
            text_fpath = pathlib.Path(input('Please, enter the path to the file to decrypt: '))
            if not text_fpath.exists():
                raise NameError('The text file does not exist!')
            pvt_key_fpath = pathlib.Path(input('Please, enter the path to the private key file: '))
            if not pvt_key_fpath.exists():
                raise NameError('The private key file does not exist!')

            with open(text_fpath, 'r') as f:
                lines = f.readlines()
            with open(pvt_key_fpath, 'r') as f:
                pvt_key = [int(x) for x in f.readlines()]

            decr_text_fpath = pathlib.Path(text_fpath.parent, text_fpath.name.replace('encr', 'decr'))
            with open(pathlib.Path(decr_text_fpath, ), 'w') as f:
                f.writelines([int_to_text(rsa_decrypt(int(line), pvt_key)) for line in lines])
            print(f'Your decrypted text has been saved at the following path: {decr_text_fpath}')

        elif mode.lower() == 'q':
            print('\nThanks for using this tool!\n')

        else:
            print('\nNot a valid mode, please try again.')

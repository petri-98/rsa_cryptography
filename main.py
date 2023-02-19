import argparse
from src.ascii_utils import text_to_int, int_to_text
from src.rsa_utils import generate_rsa_key, rsa_encrypt, rsa_decrypt


def read_cmd_params() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lenght", type=int, default=512, help="Lenght of the RSA key (in bit).")
    cmd_args = parser.parse_args()
    return cmd_args


if __name__ == '__main__':
    cmd_args = read_cmd_params()

    mode = str(input('Do you want to encrypt a message [E], decrypt a message [D] or generate a key [G]? ')).lower()
    if mode == 'g':
        key = generate_rsa_key(cmd_args.lenght)
        print(f'Public key:\n {key[0]}')
        print(f'Private key:\n {key[1]}')
    elif mode == 'e':
        msg = str(input('Insert the message you want to encode: '))
        public_key_input = input('Insert the public key (two numbers with a space in between): ')
        public_key = [int(x) for x in public_key_input.split()]
        encrypted_msg = rsa_encrypt(text_to_int(msg), public_key)
        print(f'Your encrypted message is:\n {encrypted_msg}')
    elif mode.lower() == 'd':
        encrypted_msg = int(input('Insert the encrypted message you want to decode: '))
        private_key_input = input('Insert your private key (two numbers with a space in between): ')
        private_key = [int(x) for x in private_key_input.split()]
        msg = int_to_text(rsa_decrypt(encrypted_msg, private_key))
        print(f'Your decrypted message is:\n {msg}')
    else:
        print('Not a valid mode.')

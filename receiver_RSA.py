#!/usr/bin/env python3

import socket
import sys
import time

import utils


HOST = '127.0.0.1'
PORT = int(sys.argv[1])


def decode(c, d, n):
    return utils.find_modulus(c, d, n)


def get_public_key_and_secret_key():
    p = 47
    q = 71
    n = p * q
    phi_n = utils.euler_function(n)

    # choose a number coprime with the Euler function's value of n
    e = 79

    # calculate the secret key
    _, secret_key, _ = utils.my_gcd(e, phi_n)

    return n, e, secret_key


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr =  s.accept()

    with conn:
        n_pk, e_pk, d_sk = get_public_key_and_secret_key()

        print(f'The public key is: ({n_pk}, {e_pk})')    
        conn.sendall(str(n_pk).encode('utf-8'))
        conn.sendall(str(e_pk).encode('utf-8'))

        print('Waiting for messages...')

        while True:
            # receiving the encoded message blocks 
            the_message = ''
            while not (c := conn.recv(32).decode('utf-8')).startswith('close'):
                c = int(c)
                print(f"Encoded block: {c}", end=' - ')
                m = decode(c, d_sk, n_pk)
                print(f"Decoded block: {str(m)}")
                the_message += str(m)                                

            if c == 'close all': break
            else: print(f'The message is: {int(the_message)}')
            
        time.sleep(1) 

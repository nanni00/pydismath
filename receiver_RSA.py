#!/usr/bin/env python3

import socket
import sys
import time

import utils


HOST = '127.0.0.1'
PORT = int(sys.argv[1])


def decode(c, d, n):
    return utils.find_modulus(c, d, n)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr =  s.accept()

    with conn:
        print('connection from ', addr)
        # choose two great prime numbers 
        p = 47
        q = 71
        n = p * q
        phi_n = utils.euler_function(n)

        # choose a number coprime with the Euler function's value of n
        e = 79

        print(f'The public key is: ({n}, {e})')    
        conn.sendall(str(n).encode('utf-8'))
        conn.sendall(str(e).encode('utf-8'))

        # calculate the secret key
        _, secret_key, _ = utils.my_gcd(e, phi_n)

        print('Waiting for messages...')

        # receiving the encoded message blocks 
        the_message = ''
        while (c := conn.recv(32).decode('utf-8')) != 'close':
            print(f"Received block: {c}")
            c = int(c)
            m = decode(c, secret_key, n)
            the_message += str(m)

        print(f'The message is: {int(the_message)}')

        time.sleep(1) 

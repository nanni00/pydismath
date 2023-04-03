#!/usr/bin/env python3

import socket
import sys
import utils


HOST=sys.argv[1]
PORT=int(sys.argv[2])


def encode(m, n, e):
    return utils.find_modulus(m, e, n)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Receiving public key from server...')

    n_pk = int(s.recv(1024).decode('utf-8'))
    e_pk = int(s.recv(1024).decode('utf-8'))

    print(f'The public key is: {n_pk}, {e_pk}')

    while True:
        the_message = input('Enter a number (or type enter to quit): ')
        if the_message == '': 
            s.send('close all'.encode('utf-8'))
            break

        len_msg, n_pk_len = len(str(the_message)), len(str(n_pk))

        # choosing and sending blocks length
        block_len = min(32, n_pk_len - 1)

        # creating blocks
        m_blocks = []
        if len_msg > n_pk_len:
            for i in range(0, len_msg, block_len):
                m_blocks.append(int(str(the_message)[i: i + block_len]))
        else:
            m_blocks = [the_message]

        print(f"The message has been divided into blocks: {m_blocks}")

        # encoding the message
        c_blocks = []
        for M in m_blocks:
            c_blocks.append(encode(M, n_pk, e_pk))

        print(f"The encoded blocks are: {c_blocks}")

        # sending encoded blocks
        for c in c_blocks:
            s.send(('0'*(32-len(str(c))) + str(c)).encode('utf-8'))
        
        # sending close connection message
        s.send('close'.encode('utf-8'))
        
    s.close()

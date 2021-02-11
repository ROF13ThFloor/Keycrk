

# This file was *autogenerated* from the file solution.sage
from sage.all_cmdline import *   # import sage library

_sage_const_7 = Integer(7); _sage_const_2 = Integer(2); _sage_const_0 = Integer(0); _sage_const_1 = Integer(1); _sage_const_256 = Integer(256); _sage_const_115 = Integer(115); _sage_const_3 = Integer(3); _sage_const_16 = Integer(16)
from Crypto.PublicKey import RSA
from Crypto.Util.number import * 
from Crypto.PublicKey.RSA import *
from Crypto.Cipher import *
import binascii
import os
import itertools
import unicodedata
import rsa


#convert message to integer 
def msg_to_int(msg):
    int_msg = ""
    for ch in msg:
        pre = "{0:b}".format(ord(ch))
        if len(pre) < _sage_const_7 :
            pre = "0" * (_sage_const_7  - len(pre)) + pre
        int_msg += pre

    return int(int_msg, _sage_const_2 )

#convert int to msg 

def int_to_msg(i):
    bin_format = "{0:7b}".format(i)
    msg = ""

    for b in range(_sage_const_0 , len(bin_format), _sage_const_7 ):
        msg += chr(int(bin_format[b:b + _sage_const_7 ], _sage_const_2 ))

    return msg

def find_common_key(all_N):
    pubkeys = all_N
    q = _sage_const_0 
    for p1, p2 in itertools.permutations(pubkeys, int(_sage_const_2 )):
        g = gcd(p1, p2)
        if g != _sage_const_1 :
            print("--------------",pubkeys.index(p1),pubkeys.index(p2))
            print("we have common factor with gcd ")
            print("modules is : ", pubkeys.index(p1), "   :" , p1)
            index_of_pubkey = pubkeys.index(p1)
            Q_factor = p1 / g 
            return g , Q_factor , index_of_pubkey
           #return p and Q_factor




def bytes_to_int(bytes):
    result = _sage_const_0 
    for b in bytes:
        result = result * _sage_const_256  + int(b)
    return result



def decrypt(c, n , d):  
    print(binascii.unhexlify(hex(power_mod(c, d,n))[_sage_const_2 :]))




count = _sage_const_1 
all_N = list()
for i in range(_sage_const_0 ,_sage_const_115 ):
    p_key = RSA.importKey(open('pkeys/pubkey_' + str(i).zfill(_sage_const_3 ) + '.pem','r').read())
    all_N.append(p_key.n)
    count = count + _sage_const_1  


print('Step 1: Find common factor key .. . . ')    

attack_point = find_common_key(all_N)

e_factor = RSA.importKey(open('pkeys/pubkey_'+ str(attack_point[_sage_const_2 ]).zfill(_sage_const_3 ) + '.pem','r').read()).e 
Modules_factor = RSA.importKey(open('pkeys/pubkey_'+ str(attack_point[_sage_const_2 ]).zfill(_sage_const_3 ) + '.pem','r').read()).n

euler_num = (attack_point[_sage_const_0 ] - _sage_const_1 ) * (attack_point[_sage_const_1 ] - _sage_const_1 )

d_fctor = inverse_mod(e_factor , euler_num)


with open('encs/secret_' + str(attack_point[_sage_const_2 ]).zfill(_sage_const_3 ) + '.enc' ,"rb" ) as file:
    enc_data = file.read()




print(type(Modules_factor))
print(type(e_factor))
print(type(int(d_fctor)))
print(type(int(attack_point[_sage_const_0 ])))
print(type(int(attack_point[_sage_const_1 ])))






print(attack_point[_sage_const_0 ])
print(attack_point[_sage_const_1 ])


#decrypt(bytes_to_int(enc_data) , Modules_factor , d_fctor)


print("cipher is " , int(binascii.hexlify(enc_data).decode(),_sage_const_16  ))

print("d is " , d_fctor)

print(" module is : " , Modules_factor)



plaintext = power_mod(int(enc_data.hex() , _sage_const_16 ) , d_fctor, Modules_factor)






#print(int_to_msg(plaintext))
#pretty_print(binascii.unhexlify(hex(plaintext)[2:]))









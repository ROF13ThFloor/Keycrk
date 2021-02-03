

# This file was *autogenerated* from the file solution.sage
from sage.all_cmdline import *   # import sage library

_sage_const_514 = Integer(514); _sage_const_10 = Integer(10)
from output import enc
from sage.crypto.block_cipher.sdes import SimplifiedDES



CtectBinary = format(enc, "b")

key = format(_sage_const_514 , "b").zfill(_sage_const_10 )

sides = SimplifiedDES()


#assert len(CtectBinary) % 8 == 0

plaitext = sides(CtectBinary , key , algorithm = "decrypt")


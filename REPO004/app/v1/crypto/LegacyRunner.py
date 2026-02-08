from cryptography.hazmat.primitives.asymmetric import rsa, ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# 實際呼叫過時加密
def run_legacy():
    # RSA 1024 實作
    key = rsa.generate_private_key(public_exponent=65537, key_size=1024)
    
    # MD5 實作
    digest = hashes.Hash(hashes.MD5())
    digest.update(b"data")
    
    # 3DES 實作
    cipher = Cipher(algorithms.TripleDES(b'0123456789abcdef'), modes.CBC(b'01234567'))
    
    # secp160r1 實作
    curve = ec.derive_private_key(ec.SECP160R1())

print("Legacy python assets initialized.")

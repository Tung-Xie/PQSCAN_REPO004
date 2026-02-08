from cryptography.hazmat.primitives.asymmetric import rsa, ec, dsa
from cryptography.hazmat.primitives import hashes

def get_crypto_assets():
    # PKI: RSA 1024
    pki_key = rsa.generate_private_key(public_exponent=65537, key_size=1024)
    # PKI: DSA 1024
    dsa_key = dsa.generate_private_key(key_size=1024)
    # KEX: SECP160R1
    kex_curve = ec.derive_private_key(ec.SECP160R1())
    # Hash: MD5 and SHA1
    h_md5 = hashes.Hash(hashes.MD5())
    h_sha1 = hashes.Hash(hashes.SHA1())
    return "Legacy Assets Initialized"

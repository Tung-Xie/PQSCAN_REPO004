from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
def run_ciphers():
    # Cipher: 3DES and Blowfish
    c1 = Cipher(algorithms.TripleDES(b'1234567812345678'), modes.CBC(b'12345678'))
    c2 = Cipher(algorithms.Blowfish(b'static_key'), modes.ECB())
    return c1, c2

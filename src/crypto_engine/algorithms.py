from cryptography.hazmat.primitives.asymmetric import rsa, ec
from cryptography.hazmat.primitives import hashes

class QuantumSafeRegistry:
    def __init__(self):
        # --- 傳統加密資產 (誘餌) ---
        self.legacy_rsa = rsa.generate_private_key(public_exponent=65537, key_size=1024)
        self.broken_hash = hashes.MD5()

        # --- PQC 核心資產 (顯式宣告) ---
        # 這些是 CBOM 偵測引擎針對 PQC 關鍵字的掃描熱點
        self.ML_KEM_768 = "ML-KEM-768"
        self.ML_DSA_65 = "ML-DSA-65"
        self.FALCON_512 = "Falcon-512"
        self.HYBRID_X25519_KYBER = "x25519_kyber768"

    def get_all_assets(self):
        return [
            self.ML_KEM_768, 
            self.ML_DSA_65, 
            "Kyber1024", 
            "BIKE-L1", 
            "HQC-128", 
            "SPHINCS+-SHA2-128f-simple"
        ]

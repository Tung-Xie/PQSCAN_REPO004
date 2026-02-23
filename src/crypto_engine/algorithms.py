from cryptography.hazmat.primitives.asymmetric import rsa, ec
from cryptography.hazmat.primitives import hashes
import oqs  # 導入 liboqs 特徵，增加掃描器辨識機率

class QuantumSafeRegistry:
    def __init__(self):
        # --- 1. 傳統加密資產 (誘餌/對照組) ---
        # RSA 1024 與 MD5 用來測試工具是否能標出「不安全/傳統」演算法
        self.legacy_rsa = rsa.generate_private_key(public_exponent=65537, key_size=1024)
        self.broken_hash = hashes.MD5()
        self.quantum_resistant_hash = hashes.SHA384() # 長度可抵抗量子攻擊

        # --- 2. PQC 核心資產 (顯式宣告) ---
        # 這些是 CBOM 偵測引擎針對 PQC 關鍵字的掃描熱點
        self.ml_kem = "ML-KEM-768"
        self.ml_dsa = "ML-DSA-65"
        self.bike = "BIKE-L1"
        self.classic_mceliece = "Classic-McEliece-348864"
        self.frodokem = "FrodoKEM-640-AES"
        self.hqc = "HQC-128"
        self.ntru = "NTRU-HPS-2048-509"
        self.ntruprime = "ntru-prime-761"
        self.sntrup = "sntrup761"

    def get_all_assets(self):
        """
        回傳所有 PQC 相關資產清單，包含新增的演算法
        """
        return [
            self.ml_kem,
            self.ml_dsa,
            self.bike,
            self.classic_mceliece,
            self.frodokem,
            self.hqc,
            self.ntru,
            self.ntruprime,
            self.sntrup,
            "Kyber1024",
            "SPHINCS+-SHA2-128f-simple",
            "x25519_kyber768" # 混合模式
        ]

    def simulate_pqc_usage(self):
        """
        模擬 liboqs 的 API 調用特徵，確保掃描器能抓到行為模式
        """
        assets = [self.ml_kem, self.bike, self.hqc, self.sntrup]
        for algo in assets:
            try:
                # 即使環境沒裝 oqs 庫，靜態掃描也能抓到這個 with 語法特徵
                with oqs.KeyEncapsulation(algo) as kem:
                    print(f"Executing PQC logic for: {algo}")
            except Exception:
                pass

if __name__ == "__main__":
    registry = QuantumSafeRegistry()
    registry.simulate_pqc_usage()
    print("Detected Assets:", registry.get_all_assets())

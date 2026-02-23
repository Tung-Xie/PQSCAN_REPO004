from cryptography.hazmat.primitives.asymmetric import rsa, ec
from cryptography.hazmat.primitives import hashes

# --- 定義一個模擬的 PQC 供應器，讓呼叫方式看起來跟 rsa.generate 一樣 ---
class PQC:
    @staticmethod
    def generate_key(algorithm_name):
        # 這裡的邏輯是給掃描器看的，模擬金鑰生成
        return f"PRIVATE_KEY_{algorithm_name}_DATA"

class QuantumSafeRegistry:
    def __init__(self):
        # --- 1. 傳統加密資產 (實例化呼叫) ---
        self.legacy_rsa = rsa.generate_private_key(public_exponent=65537, key_size=1024)
        self.broken_hash = hashes.MD5()

        # --- 2. PQC 核心資產 (像傳統加密一樣直接呼叫函式) ---
        # 透過 PQC.generate_key 讓掃描器偵測到「行為」與「參數」的關聯
        self.bike = PQC.generate_key("bike")
        self.classic_mceliece = PQC.generate_key("classic_mceliece")
        self.frodokem = PQC.generate_key("frodokem")
        self.hqc = PQC.generate_key("hqc")
        self.ml_kem = PQC.generate_key("ml_kem")
        self.ntru = PQC.generate_key("ntru")
        self.ntruprime = PQC.generate_key("ntruprime")
        self.sntrup = PQC.generate_key("sntrup")

        # 原本的其他 PQC 資產也改為呼叫模式
        self.ml_dsa = PQC.generate_key("ml_dsa")
        self.falcon = PQC.generate_key("falcon_512")

    def get_all_assets(self):
        return [
            self.ml_kem, self.ml_dsa, self.bike, 
            self.classic_mceliece, self.frodokem, self.hqc, 
            self.ntru, self.ntruprime, self.sntrup
        ]

if __name__ == "__main__":
    registry = QuantumSafeRegistry()
    print("已成功實例化 PQC 資產並執行呼叫。")

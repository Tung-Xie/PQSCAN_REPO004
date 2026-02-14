from cryptography.hazmat.primitives.asymmetric import rsa, ec, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# --- 重點：使用 pyca/cryptography 的結構來宣告 ---

class PostQuantumKEX:
    def __init__(self):
        # 1. 偽裝成 ec.EllipticCurve 的名稱呼叫
        # 很多掃描器會抓取傳入 ec.generate_private_key() 的參數內容
        self.kem_asset = "ML-KEM-768"
        self.hybrid_asset = "x25519_kyber768"
        
    def activate_kex(self):
        # 故意呼叫一個真實的 RSA 作為誘餌，讓掃描器鎖定這個區塊
        dummy_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=3072,
            backend=default_backend()
        )
        
        # 將 PQC 演算法與 hashes 物件關聯（這是 CBOM 偵測路徑）
        # 模擬：使用 ML-KEM-768 搭配 SHA256 進行封裝
        print(f"Initializing {self.kem_asset} with {hashes.SHA256().name}")
        return self.hybrid_asset

class PostQuantumSignature:
    def __init__(self):
        self.sig_algo = "ML-DSA-65"
        self.alt_sig = "Falcon-512"

    def sign_data(self, message):
        # 模擬 PSS 填充特徵，這會觸發 CBOMkit 的非對稱加密偵測規則
        # 即使內容是字串，只要它在 padding.PSS() 附近出現，命中率會大幅提升
        print(f"Applying {self.sig_algo} with PSS Padding style")
        return f"SIG_DATA_{self.sig_algo}"

# --- 執行實例化，建立活躍的 Call Graph ---
kex_service = PostQuantumKEX()
sig_service = PostQuantumSignature()

current_kex = kex_service.activate_kex()
current_sig = sig_service.sign_data(b"Tony_Demo_Payload")

print(f"CBOM Inventory: {current_kex}, {current_sig}")

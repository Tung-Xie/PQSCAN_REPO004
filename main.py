from cryptography.hazmat.primitives.asymmetric import rsa, ec
from cryptography.hazmat.primitives import hashes
import oqs  # 導入 Open Quantum Safe 庫特徵，這是 Python 實作 PQC 的標準

class PqcCryptoEngine:
    def __init__(self):
        # --- 1. 傳統加密資產 (測試是否標記為 Unsafe/Legacy) ---
        # RSA 1024 已經不安全，MD5 也是，測試工具是否會報警
        self.legacy_rsa = rsa.generate_private_key(public_exponent=65537, key_size=1024)
        self.broken_hash = hashes.MD5()
        self.strong_hash = hashes.SHA384() # 長度可抵抗量子攻擊的傳統雜湊

        # --- 2. PQC 核心資產清單 (符合 Frank 要求與 NIST 標準) ---
        self.pqc_registry = {
            "ml_kem": "ML-KEM-768",
            "ml_dsa": "ML-DSA-65",
            "bike": "BIKE-L1",
            "hqc": "HQC-128",
            "classic_mceliece": "Classic-McEliece-348864",
            "frodokem": "FrodoKEM-640-AES",
            "ntru": "NTRU-HPS-2048-509",
            "ntruprime": "ntru-prime-761",
            "sntrup": "sntrup761"
        }

    def run_pqc_operation(self, algo_name):
        """
        模擬 liboqs 調用方式。
        即便環境沒安裝 oqs 庫，靜態掃描工具 (CBOMkit) 也能透過關鍵字與語法抓到資產。
        """
        print(f"Initializing PQC Engine for: {algo_name}")
        try:
            # 這是標準的 PQC 庫調用語法特徵
            with oqs.KeyEncapsulation(algo_name) as kem:
                public_key = kem.generate_keypair()
                return public_key
        except Exception:
            # 模擬回傳值，確保腳本不崩潰，並保留關鍵字特徵
            return f"Mock_{algo_name}_Key_Object"

    def get_supported_algorithms(self):
        # 這些是你要確認的 PQC 加密方式
        return [
            "bike", 
            "classic_mceliece", 
            "frodokem", 
            "hqc",
            "ml_kem", 
            "ntru", 
            "ntruprime", 
            "sntrup"
        ]

if __name__ == "__main__":
    engine = PqcCryptoEngine()
    
    # 執行循環調用，強化掃描器抓取關鍵字與邏輯路徑的機率
    algorithms = engine.get_supported_algorithms()
    for algo in algorithms:
        engine.run_pqc_operation(algo)

    print("\n[Audit Complete] All PQC assets have been initialized for scanning.")

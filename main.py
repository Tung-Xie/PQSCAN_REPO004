from src.api_gateway.service import process_secure_request

if __name__ == "__main__":
    # 強迫掃描器從這裡開始爬取所有的 import 鏈
    print("--- Starting PQSCAN System ---")
    results = process_secure_request()
    print(f"System Operational with {len(results)} Crypto Assets.")

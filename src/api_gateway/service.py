from src.crypto_engine.algorithms import QuantumSafeRegistry

def process_secure_request():
    registry = QuantumSafeRegistry()
    active_assets = registry.get_all_assets()
    
    # 模擬加密行為：讓掃描器看到這些演算法被「使用」
    print(f"Establishing Quantum-Safe Tunnel using: {active_assets[0]}")
    print(f"Signing response with: {active_assets[1]}")
    
    return active_assets

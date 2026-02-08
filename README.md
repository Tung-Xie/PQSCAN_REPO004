# PQSCAN_REPO004: Python Legacy Inventory

## 📌 專案簡介
本專案模擬傳統 Python 後端服務，包含多層次的目錄結構與過時的加密資產。主要用於測試掃描器對 **深層目錄遞迴 (Deep Nested Scanning)** 以及 **過時演算法 (Legacy Crypto)** 的偵測能力。

## 🔍 CBOM 掃描亮點 (需偵測項目)
- **目錄深度**: `legacy_service/v1/network/`
- **加密資產 (Cryptographic Assets)**:
  - `secp160r1`: 已過時的橢圓曲線 (KEX)。
  - `MD5`: 具碰撞風險的雜湊函數。
  - `3DES-CBC`: 傳統對稱加密演算法。

## 🛠️ 技術棧
- Language: Python 3.x
- Security Level: **Low (Quantum Vulnerable)**

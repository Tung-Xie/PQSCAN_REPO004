# PQSCAN REPO 004: Enterprise Quantum-Safe KMS Matrix

## 📌 Project Overview
This repository serves as a **Cryptographic Inventory Reference** for Python-based applications. It simulates a distributed Key Management System (KMS) architecture to evaluate the detection capabilities of CBOM (Cryptography Bill of Materials) tools.

## 📊 Cryptographic Asset Matrix

### 1. Post-Quantum Cryptography (PQC) - NIST FIPS 203/204
| Category | Algorithm | Implementation | Status |
| :--- | :--- | :--- | :--- |
| **KEM** | ML-KEM (Kyber-768/1024) | Structured Lattice | Active |
| **KEM** | BIKE, HQC, FrodoKEM | Code-based / LWE | Evaluation |
| **Signature** | ML-DSA (Dilithium-65) | Structured Lattice | Active |
| **Signature** | Falcon-512, SPHINCS+ | Hash-based / NTRU | Evaluation |
| **Hybrid** | x25519_kyber768 | ECDH-PQC Hybrid | Migration Path |

### 2. Classical Cryptography (Legacy & Standard)
| Risk Level | Algorithm | Usage |
| :--- | :--- | :--- |
| 🔴 **Critical** | RSA-1024 / MD5 | Legacy Compatibility (To be decommissioned) |
| 🟡 **Medium** | RSA-4096 / SHA-384 | Current Standard |
| 🟢 **Compliant** | BrainpoolP256R1 | RFC 7027 Standard Curves |

## 🏗 Project Structure
- `app/core/crypto/`: Centralized cryptographic engine and algorithm definitions.
- `app/api/v1/kms/`: Handshake logic and Key Exchange (KEX) service simulation.
- `app/utils/pqc_wrappers/`: Quantum provider integration and algorithm initialization.

## 🛠 Tech Stack
- **Language**: Python 3.10+
- **Primary Library**: [pyca/cryptography](https://cryptography.io/)
- **PQC Integration**: Open Quantum Safe (OQS) Mock Provider

---
*Note: This repository is intended for security scanning and CBOM validation purposes only.*

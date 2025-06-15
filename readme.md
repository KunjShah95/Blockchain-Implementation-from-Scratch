# 🚀 Python Blockchain implementation from Scratch

    
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Active-brightgreen)
![Contributions](https://img.shields.io/badge/contributions-welcome-orange)

---

## 🧩 Overview

Welcome to the **Python Blockchain from Scratch** project! This repository demonstrates a fully functional blockchain system, including:

- ⛓️ Block creation & validation
- 💸 Transaction management
- 🔒 Proof of Work (PoW) & Proof of Capacity (PoC)
- 🧑‍💻 CLI-based node operation
- 💾 Persistent storage (save/load chain)
- 📊 Account balances & mining stats
- 🛡️ Chain and transaction validation
- 🧰 Extensible for advanced features (wallets, smart contracts, etc.)

---

## 📦 Features

- **CLI Node:** Interact with your blockchain via a user-friendly command-line interface.
- **Dual Consensus:** Alternate between PoW and PoC for mining.
- **Balances:** Real-time account balance tracking.
- **Validation:** Full chain and transaction validation.
- **Persistence:** Save and load your blockchain to disk.
- **Verbose Mode:** Toggle detailed logs for debugging and learning.
- **Mining Stats:** See mining attempts, time, and PoC deadlines.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/KunjShah01/python-blockchain-scratch.git
cd python-blockchain-scratch
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Run the CLI Node
```bash
python main.py
```

---

## 🖥️ CLI Menu

- `1. Add transaction`  
- `2. Mine block`  
- `3. View blockchain (pretty)`  
- `4. Show balances`  
- `5. Validate chain`  
- `6. Save blockchain`  
- `7. Load blockchain`  
- `8. Toggle verbose mode`  
- `9. Show mining statistics`  
- `0. Exit`

---

## 🏗️ Project Structure

```
core/
  block.py         # Block structure
  blockchain.py    # Blockchain logic
  transaction.py   # Transaction structure
  poc.py           # Proof of Capacity
network/
  node.py          # CLI Node
main.py            # Entry point
requirements.txt   # Dependencies
```

---

## 🛠️ Extending the Project

- 🔑 Add wallets & digital signatures
- 🧠 Implement smart contracts
- 🌐 Add networking for distributed nodes
- ⚖️ Experiment with new consensus algorithms
- 🧪 Write unit tests for all modules

---

## 🤝 Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or new features.

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 🙌 Acknowledgements

- Python 🐍
- The open-source blockchain community

---

> Made with ❤️ by the Python Blockchain Team

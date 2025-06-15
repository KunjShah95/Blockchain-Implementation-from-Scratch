import hashlib
import json

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0, plot_hash=None):
        self.index = index
        self.transactions = [tx.to_dict() if not isinstance(tx, dict) else tx for tx in transactions]
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.plot_hash = plot_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = json.dumps({
            "index": self.index,
            "transactions": self.transactions,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
            "plot_hash": self.plot_hash
        }, sort_keys=True)
        return hashlib.sha256(block_data.encode()).hexdigest()

    def to_dict(self):
        return {
            "index": self.index,
            "transactions": self.transactions,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
            "plot_hash": self.plot_hash,
            "hash": self.hash
        }
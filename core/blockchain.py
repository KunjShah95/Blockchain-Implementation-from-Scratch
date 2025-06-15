import time
from core.block import Block
from core.poc import PoC
import json
import os


class Blockchain:
    def __init__(self, difficulty=4, miner_id="miner1", verbose=False):
        self.difficulty = difficulty
        self.miner_id = miner_id
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []
        self.verbose = verbose
        self.mining_stats = {}

    def create_genesis_block(self):
        return Block(0, [], time.time(), "0")

    def proof_of_work(self, block):
        """Mine using PoW by finding a nonce that meets difficulty."""
        block.nonce = 0
        computed_hash = block.calculate_hash()
        attempts = 0
        start = time.time()
        while not computed_hash.startswith("0" * self.difficulty):
            block.nonce += 1
            computed_hash = block.calculate_hash()
            attempts += 1
        elapsed = time.time() - start
        self.mining_stats = {"method": "PoW", "attempts": attempts, "time": elapsed}
        if self.verbose:
            print(f"[PoW] Attempts: {attempts}, Time: {elapsed:.4f}s")
        return computed_hash

    def add_block(self, transactions):
        """Add a block using PoW or PoC based on index."""
        previous_block = self.chain[-1]
        new_block = Block(
            len(self.chain), transactions, time.time(), previous_block.hash
        )
        if len(self.chain) % 2 == 1:  # PoW for odd-indexed blocks
            new_block.hash = self.proof_of_work(new_block)
            if self.verbose:
                print(
                    f"Mined block {new_block.index} with PoW (nonce: {new_block.nonce})"
                )
        else:  # PoC for even-indexed blocks
            poc = PoC(self.miner_id)
            scoop_hash, deadline = poc.mine_poc(new_block.index)
            if poc.validate_poc(scoop_hash, deadline):
                new_block.plot_hash = scoop_hash
                new_block.hash = new_block.calculate_hash()
                self.mining_stats = {"method": "PoC", "deadline": deadline}
                if self.verbose:
                    print(
                        f"Mined block {new_block.index} with PoC (deadline: {deadline})"
                    )
            else:
                raise Exception("PoC validation failed")
        self.chain.append(new_block)
        return new_block

    def add_transaction(self, transaction):
        """Add a transaction to the pending list."""
        if not self.validate_transaction(transaction):
            raise Exception("Invalid transaction.")
        self.pending_transactions.append(transaction)

    def validate_transaction(self, transaction):
        """Validate a transaction's attributes and sender's balance."""
        if transaction.amount <= 0:
            if self.verbose:
                print("[Validation] Transaction amount must be positive.")
            return False
        if transaction.sender != "SYSTEM":
            if self.get_balance(transaction.sender) < transaction.amount:
                if self.verbose:
                    print("[Validation] Insufficient balance.")
                return False
        return True

    def get_balance(self, address):
        """Calculate the balance of an address by summing its transactions."""
        balance = 0
        for block in self.chain:
            for tx in block.transactions:
                if tx["sender"] == address:
                    balance -= tx["amount"]
                if tx["receiver"] == address:
                    balance += tx["amount"]
        for tx in self.pending_transactions:
            if tx.sender == address:
                balance -= tx.amount
            if tx.receiver == address:
                balance += tx.amount
        return balance

    def validate_chain(self):
        """Validate the blockchain integrity by checking hashes and links."""
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            prev = self.chain[i - 1]
            if current.previous_hash != prev.hash:
                if self.verbose:
                    print(f"[Chain Validation] Block {i} has invalid previous hash.")
                return False
            if current.hash != current.calculate_hash():
                if self.verbose:
                    print(f"[Chain Validation] Block {i} has invalid hash.")
                return False
        return True

    def save(self, filename="blockchain.json"):
        """Save the blockchain to a file."""
        with open(filename, "w") as f:
            json.dump([block.to_dict() for block in self.chain], f, indent=2)
        if self.verbose:
            print("[Save] Blockchain saved to blockchain.json")

    def load(self, filename="blockchain.json"):
        """Load the blockchain from a file."""
        if not os.path.exists(filename):
            if self.verbose:
                print("[Load] No blockchain file found.")
            return
        with open(filename, "r") as f:
            data = json.load(f)
            from core.block import Block

            self.chain = [Block(**block) for block in data]
        if self.verbose:
            print(f"[Load] Blockchain loaded from {filename}")

    def pretty_print(self):
        """Print the blockchain in a readable JSON format."""
        for block in self.chain:
            print(json.dumps(block.to_dict(), indent=2))

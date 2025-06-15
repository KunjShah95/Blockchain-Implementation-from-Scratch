from core.blockchain import Blockchain
from core.transaction import Transaction


class Node:
    def __init__(self, miner_id="miner1"):
        self.blockchain = Blockchain(miner_id=miner_id)
        self.verbose = False

    def run(self):
        while True:
            print("\n--- Blockchain CLI Node ---")
            print("1. Add transaction")
            print("2. Mine block")
            print("3. View blockchain (pretty)")
            print("4. Show balances")
            print("5. Validate chain")
            print("6. Save blockchain")
            print("7. Load blockchain")
            print(
                "8. Toggle verbose mode (currently: {} )".format(
                    self.blockchain.verbose
                )
            )
            print("9. Show mining statistics")
            print("0. Exit")
            choice = input("Select an option: ")
            if choice == "1":
                sender = input("Sender: ")
                receiver = input("Receiver: ")
                amount = float(input("Amount: "))
                tx = Transaction(sender, receiver, amount)
                try:
                    self.blockchain.add_transaction(tx)
                    print(f"Transaction added: {tx.to_dict()}")
                except Exception as e:
                    print(f"Transaction failed: {e}")
            elif choice == "2":
                if not self.blockchain.pending_transactions:
                    print("No transactions to mine.")
                else:
                    block = self.blockchain.add_block(
                        self.blockchain.pending_transactions
                    )
                    self.blockchain.pending_transactions = []
                    print(f"Block mined: {block.to_dict()}")
            elif choice == "3":
                self.blockchain.pretty_print()
            elif choice == "4":
                addresses = set()
                for block in self.blockchain.chain:
                    for tx in block.transactions:
                        addresses.add(tx["sender"])
                        addresses.add(tx["receiver"])
                for addr in addresses:
                    if addr:
                        print(f"{addr}: {self.blockchain.get_balance(addr)}")
            elif choice == "5":
                valid = self.blockchain.validate_chain()
                print("Chain is valid." if valid else "Chain is INVALID!")
            elif choice == "6":
                self.blockchain.save()
            elif choice == "7":
                self.blockchain.load()
            elif choice == "8":
                self.blockchain.verbose = not self.blockchain.verbose
                print(f"Verbose mode set to {self.blockchain.verbose}")
            elif choice == "9":
                print(self.blockchain.mining_stats)
            elif choice == "0":
                print("Exiting.")
                break
            else:
                print("Invalid option.")

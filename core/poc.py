import os 
import hashlib
import random

class  PoC:
    def __init__(self, miner_id, plot_size_mb=10):
        self.miner_id = miner_id
        self.plot_size = plot_size_mb * 1024 * 1024  # MB to bytes
        self.plot_file = f"plots/plot_{miner_id}.dat"
        os.makedirs("plots", exist_ok=True)

    def generate_plot(self):
        """Generate a plot file with pre-computed hashes."""
        if os.path.exists(self.plot_file):
            return self.plot_file
        with open(self.plot_file, 'wb') as f:
            for i in range(self.plot_size // 32):  # 32 bytes per hash
                nonce = f"{self.miner_id}:{i}"
                hash_val = hashlib.sha256(nonce.encode()).digest()
                f.write(hash_val)
        print(f"Generated plot: {self.plot_file} ({self.plot_size / (1024 * 1024)} MB)")
        return self.plot_file

    def mine_poc(self, block_index):
        """Mine using PoC by finding a deadline based on a scoop."""
        if not os.path.exists(self.plot_file):
            self.generate_plot()
        scoop_number = block_index % 4096  # Simulate scoop selection
        scoop_offset = scoop_number * 32
        with open(self.plot_file, 'rb') as f:
            f.seek(scoop_offset % self.plot_size)
            scoop = f.read(32)
            if len(scoop) < 32:
                scoop = hashlib.sha256(str(random.randint(0, 1000000)).encode()).digest()
            scoop_hash = hashlib.sha256(scoop + str(block_index).encode()).hexdigest()
            deadline = int(scoop_hash, 16) % 1000000  # Simplified deadline
        return scoop_hash, deadline

    def validate_poc(self, scoop_hash, deadline):
        """Validate PoC deadline (simplified)."""
        return deadline < 500000  # Arbitrary threshold for valid deadline
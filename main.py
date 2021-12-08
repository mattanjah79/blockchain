import hashlib

class MyCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):

        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = f"{' - '.join(transaction_list)} - {previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

class Blockchain:

    def __init__(self):
        self.chain = []
        self.generate_genesis_block()

    def generate_genesis_block(self):
        self.chain.append(MyCoinBlock("0", ['Genesis Block']))

    def create_block_from_transaction(self, transaction_list):
        previous_block_hash = self.last_block.block_hash
        self.chain.append(MyCoinBlock(previous_block_hash, transaction_list))

    def display_chain(self):
        for i in range(len(self.chain)):
            print(f"Data {i + i}: {self.chain[i].block_data}")
            print(f"Hash {i + i}: {self.chain[i].block_hash}\n")

    @property
    def last_block(self):
        return self.chain[-1]


transaction_1 = "User_1 sends 5 MC to User_23"
transaction_2 = "User_3 sends 3.4 MC to User_1"
transaction_3 = "User_32 sends 42.3 MC to User_4"
transaction_4 = "User_12 sends 122.2 MC to User_2"
transaction_5 = "User_4 sends 4.3 MC to User_21"
transaction_6 = "User_63 sends 12.9 MC to User_77"

myblockchain = Blockchain()

myblockchain.create_block_from_transaction([transaction_1, transaction_2])
myblockchain.create_block_from_transaction([transaction_3, transaction_4])
myblockchain.create_block_from_transaction([transaction_5, transaction_6])

myblockchain.display_chain()
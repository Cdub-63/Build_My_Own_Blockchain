class Blockchain(object):
    """A simple Blockchain class"""

    def __init__(self):
        """Initialize the blockchain"""
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        """Create a new block and add it to the chain"""
        pass
    
    def new_transaction(self, sender, recipient, amount):
        """
        Create a new transaction to go into the next mined block
        :param sender: <str> Address of the sender
        :param recipient: <str> Address of the recipient
        :param amount: <int> Amount
        :return: <int> The index of the block that will hold this transaction
        """
        
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        retrun self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """Create a SHA-256 hash of a block"""
        pass

    @property
    def last_block(self):
        """Return the last block in the chain"""
        pass
    

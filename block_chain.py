class BlockChain(object):
  def __init__(self):
    self.chain = []
    self.current_transactions = []

   def new_block(self):
     # Creates a new Block and add it to the chain
     pass

   def new_transaction(self):
     # Adds a new transaction to the list of transactions
     pass

   @staticmethod
   def hash(block):
     # Hashes a block
     pass

   @property
   def last_block(self):
     pass

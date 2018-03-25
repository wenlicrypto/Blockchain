class BlockChain(object):
  def __init__(self):
    self.chain = []
    self.current_transactions = []

  def new_block(self):
    # Creates a new Block and add it to the chain
    pass

  def new_transaction(self, sender, recipient, amount):
    # Adds a new transaction to the list of transactions
    """
    Creates a new transaction to go into the next mined block

    :param sender: <str> Address of the sender
    :param recipient: <str> Address of the recipient
    :params amount: <int> Amount
    :return: <int> The index of the Block that will hold this transaction
    """

    self.current_transactions.append({
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    })

    return self.last_block.get('index', -1) + 1

  @staticmethod
  def hash(block):
    # Hashes a block
    pass

  @property
  def last_block(self):
    if(len(self.chain) == 0):
        return {}
    else:
        return self.chain[-1]

from block_chain import BlockChain

def test_new_transaction():
    sender = "test sender"
    recipient = "test recipient"
    amount = 100
    block_chain = BlockChain()
    block_chain.new_transaction(sender, recipient, amount)

    trans = block_chain.current_transactions
    assert len(trans) == 1
    assert trans[-1]['sender'] == sender
    assert trans[-1]['recipient'] == recipient
    assert trans[-1]['amount'] == 100

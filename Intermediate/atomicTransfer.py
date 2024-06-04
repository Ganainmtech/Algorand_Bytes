


group_tx = algorand.new_group()

group_tx.add_payment(
    PayParams(
        sender=receiver_one.address,   
        receiver=receiver_two.address,       
        amount=1_000_000                
    ))


group_tx.add_payment(
    PayParams(
        sender=receiver_two.address,   
        receiver=receiver_one.address,       
        amount=1_000_000                
    ))

group_tx.execute()




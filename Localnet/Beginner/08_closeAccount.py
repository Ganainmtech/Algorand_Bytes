from algokit_utils.beta.algorand_client import (
    AlgorandClient,
    PayParams,
)

# Initialize the Algorand Client
algorand = AlgorandClient.default_local_net()

# Get dispenser account from KMD to fund other accounts
dispenser = algorand.account.dispenser()

# Create a new account (account to be closed)
account = algorand.account.random()

# Transfer 10 Algos from the dispenser to the creator account
algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        receiver=account.address,
        amount=10_000_000  # Amount in microAlgos (10 Algos)
    )
)

# Query account information after transaction to get up to date account information
account_info = algorand.account.get_information(account.address)
print("Balance (in microAlgos):", account_info['amount'])

# Close the account and transfer the remaining balance to another account
if account_info['amount'] > 0:
    algorand.send.payment(
        PayParams(
            sender=account.address,
            receiver=dispenser.address,  # Send remaining balance to the dispenser or any other account
            amount=0,                    # Transfer remaining balance 
            close_remainder_to=dispenser.address
        )
    )
    account_info = algorand.account.get_information(account.address)
    print(f"Account Closed Succesfully\nBalance (in microAlgos):", account_info['amount'])
    
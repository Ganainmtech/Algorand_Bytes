from algokit_utils.beta.algorand_client import (
    AlgorandClient,
    PayParams,
)

# Initialize Algorand client connected to localnet
algorand = AlgorandClient.default_local_net()

# Get dispenser account from KMD to fund other accounts
dispenser = algorand.account.dispenser()

# Create and fund a new account
account = algorand.account.random()
algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        receiver=account.address,
        amount=10_000_000  # Fund with 10 Algos
    )
)

# Query account information
account_info = algorand.account.get_information(account.address)

# Print the queried account information
print("Account Address:", account_info['address'])
print("Balance (in microAlgos):", account_info['amount'])
print("Assets Held:", account_info.get('assets', 'None'))
print("Pending Rewards:", account_info['pending-rewards'])
print("Status:", account_info['status'])

from algokit_utils.beta.algorand_client import (
    AlgorandClient,
    PayParams,
)

# Initialize an Algorand client connected to the default local network
algorand = AlgorandClient.default_local_net()

# Get dispenser account from KMD to fund other accounts
dispenser = algorand.account.dispenser()

# Create a new random account
creator = algorand.account.random()

# Transfer 10 Algos from the dispenser to the creator account
algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        receiver=creator.address,
        amount=10_000_000  # Amount in microAlgos (10 Algos)
    )
)

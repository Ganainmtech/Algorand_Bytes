from algokit_utils.beta.algorand_client import (
    AlgorandClient,
    AssetCreateParams,
    PayParams,
)

# Initialize an Algorand client connected to the default local network
algorand = AlgorandClient.default_local_net()

# Get dispenser account from KMD to fund other accounts
dispenser = algorand.account.dispenser()

# Create a new random Algorand account
accountOne = algorand.account.random()

# Transfer 10 Algos from the dispenser to the creator account
algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        receiver=accountOne.address,
        amount=10_000_000  # Amount in microAlgos (10 Algos)
    )
)

# Create a new Algorand Standard Asset (ASA) called "Algofam"
sent_txn = algorand.send.asset_create(
    AssetCreateParams(
        sender=accountOne.address,
        total=1000,  # Total supply of the asset
        asset_name="Algofam",  # Name of the asset
        unit_name="FAM",  # Unit name for the asset
        manager=accountOne.address,  # Address with management privileges
        clawback=accountOne.address,  # Address with clawback privileges
        freeze=accountOne.address  # Address with freeze privileges
    )
)

# Extract asset ID from the transaction
asset_id = sent_txn["confirmation"]["asset-index"]

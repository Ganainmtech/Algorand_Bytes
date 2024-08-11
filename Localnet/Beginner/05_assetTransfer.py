from algokit_utils.beta.algorand_client import (
    AlgorandClient,
    AssetCreateParams,
    AssetTransferParams,
    PayParams,
    AssetOptInParams,
)

# Initialize Algorand client connected to localnet
algorand = AlgorandClient.default_local_net()

# Get dispenser account from KMD to fund other accounts
dispenser = algorand.account.dispenser()

# Create and fund a new account (creator)
creator = algorand.account.random()
algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        receiver=creator.address,
        amount=10_000_000  # Fund with 10 Algos
    )
)

# Create a new Algorand Standard Asset (ASA)
sent_txn = algorand.send.asset_create(
    AssetCreateParams(
        sender=creator.address,
        total=1000,  
        asset_name="algofam",  
        unit_name="FAM",  
        manager=creator.address, 
        clawback=creator.address,  
        freeze=creator.address  
    )
)

# Extract the Asset ID from the transaction confirmation
asset_id = sent_txn["confirmation"]["asset-index"]

# Create and fund another new account (receiver)
receiver = algorand.account.random()
algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        receiver=receiver.address,
        amount=10_000_000  # Fund with 10 Algos
    )
)

# Opt-in the receiver account to the newly created ASA
algorand.send.asset_opt_in(
    AssetOptInParams(
        sender=receiver.address,
        asset_id=asset_id
    )
)

# Transfer 10 units of the ASA from creator to receiver
algorand.send.asset_transfer(
    AssetTransferParams(
        sender=creator.address,
        receiver=receiver.address,
        asset_id=asset_id, # The extracted Asset ID
        amount=10  # Transfer amount
    )
)

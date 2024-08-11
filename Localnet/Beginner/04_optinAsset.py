from algokit_utils.beta.algorand_client import (
    AlgorandClient,
    AssetCreateParams,
    AssetOptInParams,
    PayParams,
)

# Initialize Algorand client connected to localnet
algorand = AlgorandClient.default_local_net()

# Get dispenser account from KMD to fund other accounts
dispenser = algorand.account.dispenser()

# Create and fund creator account
creator = algorand.account.random()
algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        receiver=creator.address,
        amount=10_000_000
    )
)

# Create Algorand Standard Asset (ASA)
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

# Extract asset ID from the transaction
asset_id = sent_txn["confirmation"]["asset-index"]

# Create and fund receiver account
receiver = algorand.account.random()
algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        receiver=receiver.address,
        amount=10_000_000
    )
)

# Opt-in receiver account to the newly created asset
algorand.send.asset_opt_in(
    AssetOptInParams(
        sender=receiver.address,
        asset_id=asset_id
    )
)

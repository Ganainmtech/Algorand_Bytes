from algokit_utils.beta.algorand_client import (
    AlgorandClient,
    AssetCreateParams,
    AssetTransferParams,
    PayParams,
    AssetOptInParams,
)
# Initialize an Algorand client connected to the default local network
algorand = AlgorandClient.default_local_net()

# Get dispenser account from KMD to fund other accounts
dispenser = algorand.account.dispenser()

# Create a new random account
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
        total=50,  # Total supply of the asset
        asset_name="Algofam",  # Name of the asset
        unit_name="FAM",  # Unit name for the asset
        manager=accountOne.address,  # Address with management privileges
        clawback=accountOne.address,  # Address with clawback privileges
        freeze=accountOne.address  # Address with freeze privileges
    )
)

# Extract asset ID from the transaction
asset_id = sent_txn["confirmation"]["asset-index"]


# Create and fund receiver account
accountTwo = algorand.account.random()
algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        receiver=accountTwo.address,
        amount=10_000_000
    )
)

# Opt-in receiver account to the newly created asset
algorand.send.asset_opt_in(
    AssetOptInParams(
        sender=accountTwo.address,
        asset_id=asset_id
    )
)

# Transfer 10 units of the ASA from accounts
algorand.send.asset_transfer(
    AssetTransferParams(
        sender=accountOne.address,
        receiver=accountTwo.address,
        asset_id=asset_id, # The extracted Asset ID
        amount=10  # Transfer amount
    )
)

# Query account information
accountTwoInfo = algorand.account.get_information(accountTwo.address)

# Print the queried accountOne information
print("Account Address:", accountTwoInfo['address'])
print("Balance (in microAlgos):", accountTwoInfo['amount'])
print("Assets Held:", accountTwoInfo.get('assets', 'None'))
print("Pending Rewards:", accountTwoInfo['pending-rewards'])
print("Status:", accountTwoInfo['status'])

# Print the queried accountOne information
print(f"Receiver Account Address: {accountTwo.address}")
print(f"Number of Assets Opted-In: {len(accountTwoInfo.get('assets', []))}")
print(f"Default Asset Holding Info: {(accountTwoInfo.get('assets'))}")
for asset in accountTwoInfo.get('assets', []):
    if asset['asset-id'] == asset_id:
        print(f"\nAsset ID of Asset: {asset_id}")
        print(f"Asset Balance of Asset {asset_id}: {asset['amount']}")


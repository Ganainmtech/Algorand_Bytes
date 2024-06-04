

multisig = MultisigAccount(version=1, threshold=2, addresses=[
    account1.address, account2.address, account3.address
])


asset_id = 123456  # Assume asset_id is known
algorand.send.asset_opt_in(
    AssetOptInParams(
        sender=multisig.address,
        asset_id=asset_id
    )
)



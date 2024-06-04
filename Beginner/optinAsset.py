


from algokit_utils.beta.algorand_client import AlgorandClient, AssetOptInParams

algorand = AlgorandClient.default_local_net()

receiver = algorand.account.random()
asset_id = 123456  # Example asset ID
algorand.send.asset_opt_in(
    AssetOptInParams(
        sender=receiver.address,
        asset_id=asset_id
    )
)






from algokit_utils.beta.algorand_client import AlgorandClient, AssetTransferParams

algorand = AlgorandClient.default_local_net()

creator = algorand.account.random()
receiver = algorand.account.random()
asset_id = 123456  # Example asset ID
algorand.send.asset_transfer(
    AssetTransferParams(
        sender=creator.address,
        receiver=receiver.address,
        asset_id=asset_id,
        amount=10
    )
)



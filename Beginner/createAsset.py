

from algokit_utils.beta.algorand_client import AlgorandClient, AssetCreateParams

algorand = AlgorandClient.default_local_net()

creator = algorand.account.random()
algorand.send.asset_create(
    AssetCreateParams(
        sender=creator.address,
        total=1000,
        asset_name="Algofam",
        unit_name="FAM"
    )
)






from algokit_utils.beta.algorand_client import AlgorandClient, PayParams

algorand = AlgorandClient.default_local_net()

dispenser = algorand.account.dispenser()
receiver = algorand.account.random()
algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        receiver=receiver.address,
        amount=10_000_000
    )
)



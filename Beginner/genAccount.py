


from algokit_utils.beta.algorand_client import AlgorandClient

algorand = AlgorandClient.default_local_net()

account = algorand.account.random()
print(account.address)



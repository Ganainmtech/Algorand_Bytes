from algokit_utils.beta.algorand_client import AlgorandClient

# Initialize an Algorand client connected to the default local network
algorand = AlgorandClient.default_local_net()

# Create a new random account and print its extracted information
account = algorand.account.random()
print(algorand.account.get_information(account.address))

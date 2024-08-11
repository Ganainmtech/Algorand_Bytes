# Import the AlgorandClient class from the Algokit utilities library,
# This class provides methods to interact with the Algorand blockchain.
from algokit_utils.beta.algorand_client import AlgorandClient


# Initialize an Algorand client connected to the default local network
algorand = AlgorandClient.default_local_net()
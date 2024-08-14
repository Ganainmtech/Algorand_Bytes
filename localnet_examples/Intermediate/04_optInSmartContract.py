'''
This script demonstrates how to opt an account into an existing Algorand Smart Contract (ASC1).

This is where you would include any setup code needed, such as:

- Import the necessary libraries and modules:
  from algokit_utils.beta.algorand_client import *
  from algokit_utils.application import ApplicationClient
- Ensure the account is funded and opted into the application
- Deploy or have access to a deployed smart contract

You can find all the foundational code in the 'Beginner' folder.
'''

# Initialize the Algorand Client
algorand = AlgorandClient.default_local_net()

# Specify the Application ID to opt into
app_id = 123456  # Replace with the actual application ID

# Opt-in the account into the smart contract
app_client = ApplicationClient(algorand)
app_client.opt_in(app_id, sender_address=account.address)

'''
About Opting into a Smart Contract:
- This script demonstrates how to opt an account into an existing Algorand Smart Contract (ASC1) using Algokit Utils.
- Opting into a smart contract allows an account to interact with it by participating in its local state.

Why Opt-In to a Smart Contract?
- Opting in is required before an account can interact with a contracts logic and state.
- It allows the contract to maintain a local state for the account, tracking its interaction.

Remember:
- Ensure the account has sufficient funds to cover transaction fees.
'''

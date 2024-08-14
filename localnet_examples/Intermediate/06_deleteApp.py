'''
This script deletes an existing Algorand smart contract from the blockchain, removing its state and logic.

This is where you would include any setup code needed, such as:

- Import the necessary libraries and modules:
  from algokit_utils.beta.algorand_client import *
- Have access to the Application ID (app_id) of the smart contract you want to delete
- Ensure the deployer account has sufficient balance to cover transaction fees

You can find all the foundational code in the 'Beginner' folder.
'''

# Initialize the Algorand Client
algorand = AlgorandClient.default_local_net()

# Specify the Application ID to delete
app_id = 123456  # Replace with the actual application ID of the deployed smart contract

# Delete the smart contract
algorand.send.application_delete(
    ApplicationDeleteParams(
        sender=deployer.address,  # The address of the account deleting the smart contract
        app_id=app_id             # The ID of the application to delete
    )
)

'''
About Deleting Smart Contracts:
- This script demonstrates how to delete an existing Algorand Smart Contract (ASC1) from the blockchain.
- Deleting a smart contract removes it from the Algorand network, and its state and logic will no longer be accessible.

Why Delete a Smart Contract?
- Smart contracts may need to be deleted to remove obsolete or redundant contracts.
- For example, if a smart contract is no longer needed or has been replaced by a new version, it may be removed to clean up the blockchain.
- Deleting a contract helps manage resources and ensures that only relevant contracts remain on the network.

Remember:
- Only the account with the appropriate permissions (typically the creator or manager) can delete the smart contract.
- Ensure that you no longer need the contract or its state before deletion, as this action cannot be undone.
'''

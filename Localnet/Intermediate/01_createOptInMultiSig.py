'''
This script demonstrates how to opt a multisig account into an asset, allowing it to manage and transact with that asset.

This is where you would include any setup code needed, such as:

- Import the necessary libraries and modules:
  from algokit_utils.beta.algorand_client import *
  from algokit_utils.beta.multisig import MultisigAccount
- Generate Algorand Accounts
- Fund the accounts

You can find all the foundational code in the 'Beginner' folder.
'''

# Initialize the Algorand Client
algorand = AlgorandClient.default_local_net()

# Create a Multisig Account
multisig = MultisigAccount(
    version=1,                # Multisig version (use 1 for standard multisig)
    threshold=2,              # Threshold: the minimum number of signatures required
    addresses=[               # List of Algorand addresses that form the multisig account
        account1.address, 
        account2.address, 
        account3.address
    ]
)

# Specify the Asset ID to opt in
asset_id = 123456  # Replace with the actual asset_id you want to opt in to

# Opt the Multisig Account into the Asset
algorand.send.asset_opt_in(
    AssetOptInParams(
        sender=multisig.address,  # The address of the multisig account
        asset_id=asset_id         # The asset ID to opt into
    )
)

'''
About Multisig Opt-In:
- A multisig account is a shared account that requires multiple signatures to authorize a transaction.
- The `threshold` value determines how many signatures are needed to authorize a transaction.

Why Use a Multisig Account? |  Why Opt-In a Multisig Account?
- Multisig accounts are used for scenarios requiring shared decision-making and enhanced security, ensuring that multiple parties agree before a transaction is executed.
- Corporate Funds: To manage company assets where multiple executives must approve transactions, reducing the risk of unauthorized access.
- Joint Ventures: In partnerships, where all partners must approve fund movements to ensure collaborative decision-making and accountability.

Remember:
- Ensure the `threshold` matches the required number of signatures for your use case.
- Confirm all multisig account addresses have sufficient funds for transaction fees.
- Obtain all required signatures before submitting the opt-in transaction.
'''

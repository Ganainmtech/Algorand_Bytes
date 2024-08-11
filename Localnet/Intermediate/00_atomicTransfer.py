'''
This script demonstrates how to execute multiple transactions atomically, ensuring all transactions in a group either succeed or fail together.

This is where you would include any setup code needed, such as:

- Import the necessary libraries and modules:
  from algokit_utils.beta.algorand_client import *
- Generate Algorand Accounts
- Fund the accounts

You can find all the foundational code in the 'Beginner' folder.
'''

# Initialize the Algorand Client
algorand = AlgorandClient.default_local_net()

# Group transactions for atomic transfer
group_tx = algorand.new_group()

# Add the first payment transaction to the group
group_tx.add_payment(
    PayParams(
        sender=receiver_one.address,   # Address of the first sender
        receiver=receiver_two.address, # Address of the first receiver
        amount=1_000_000               # Amount to transfer (in microAlgos)
    ))

# Add the second payment transaction to the group
group_tx.add_payment(
    PayParams(
        sender=receiver_two.address,   # Address of the second sender
        receiver=receiver_one.address, # Address of the second receiver
        amount=1_000_000               # Amount to transfer (in microAlgos)
    ))

# Execute the grouped transactions atomically
group_tx.execute()

'''
About atomic transfers:
- Atomic transfers or swaps ensure that every transaction in a group either all succeed or else all fail.
- You can use this structure to execute multiple transactions as a single atomic unit.

Why Use Atomic Transfers?
- Atomic transfers are essential when you need to ensure consistency and reliability across multiple transactions. For example:
  - When performing a swap or exchange where multiple parties are involved, you want to ensure that all parts of the transaction complete successfully before finalizing.
  - In decentralized finance (DeFi) applications, atomic transfers can be used to maintain integrity and prevent partial or failed transactions that could lead to unexpected outcomes.

Remember:
- Atomic transfers are subject to the Algorand networks transaction limits and fees. Make sure you account for these in your planning.
- The success of atomic transfers depends on the overall validity of the group transaction. If any single transaction fails validation, the entire group will be rejected.
'''

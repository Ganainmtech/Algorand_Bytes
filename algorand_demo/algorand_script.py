from algokit_utils.beta.algorand_client import (
    AlgorandClient,
    AssetCreateParams,
    AssetTransferParams,
    PayParams,
    AssetOptInParams,
)

class AlgorandActions:
    def __init__(self):
        self.algorand = AlgorandClient.default_local_net()
        self.dispenser = self.algorand.account.dispenser()
        self.accounts = {}  # Dictionary to store generated accounts
        self.asset_id = None

    def generate_account(self):
        account = self.algorand.account.random()
        self.accounts[account.address] = account  # Store the account
        return account.address  # Return the public address

    def fund_account(self, address):
        fund_account_txn = self.algorand.send.payment(
            PayParams(
                sender=self.dispenser.address,
                receiver=address,
                amount=10_000_000
            )
        )
        tx_id = fund_account_txn.get("tx_id")
        return tx_id
        
    def create_asa(self, creator_address):
        # Retrieve the account object using the address
        account = self.accounts.get(creator_address)
        
        if account is None:
            raise ValueError(f"No account found for address {creator_address}")
        
        # Send the asset creation transaction
        create_asset_txn = self.algorand.send.asset_create(
            AssetCreateParams(
                sender=account.address,  # Use the account address directly
                total=50,
                asset_name="Algofam",
                unit_name="FAM",
                manager=account.address,  
                clawback=account.address,
                freeze=account.address
            )
        )
        
        # Extract asset ID and transaction ID from the response
        self.asset_id = create_asset_txn["confirmation"].get("asset-index")
        tx_id = create_asset_txn.get("tx_id")
        
        # Ensure both asset_id and tx_id are returned correctly
        return self.asset_id, tx_id

    def opt_in_asa(self, receiver_address):
        # Ensure that the receiver account exists
        if receiver_address not in self.accounts:
            raise ValueError(f"No account found for address {receiver_address}")
        
        opt_in_txn = self.algorand.send.asset_opt_in(
            AssetOptInParams(
                sender=receiver_address,
                asset_id=self.asset_id
            )
        )
        tx_id = opt_in_txn.get("tx_id")
        return tx_id

    def transfer_asa(self, sender_address, receiver_address, amount):
        # Ensure that both sender and receiver accounts exist
        if sender_address not in self.accounts:
            raise ValueError(f"No account found for sender address {sender_address}")
        
        if receiver_address not in self.accounts:
            raise ValueError(f"No account found for receiver address {receiver_address}")
        
        transfer_asa_txn = self.algorand.send.asset_transfer(
            AssetTransferParams(
                sender=sender_address,
                receiver=receiver_address,
                asset_id=self.asset_id,
                amount=amount
            )
        )
        tx_id = transfer_asa_txn.get("tx_id")
        return tx_id

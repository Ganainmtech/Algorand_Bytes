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
        self.account = None
        self.asset_id = None

    def generate_account(self):
        self.account = self.algorand.account.random()
        return self.account

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

    def set_account(self, address):
        # Assuming this is how you fetch an account by address
        # Adjust this method based on the actual implementation to fetch or set an account
        self.account = self.algorand.account.get(address)
        
    def create_asa(self):
        if self.account is None:
            raise ValueError("Account is not set")
        # Send the asset creation transaction
        create_asset_txn = self.algorand.send.asset_create(
            AssetCreateParams(
                sender=self.account.address,
                total=50,
                asset_name="Algofam",
                unit_name="FAM",
                manager=self.account.address,
                clawback=self.account.address,
                freeze=self.account.address
            )
        )
        
        # Extract asset ID and transaction ID from the response
        self.asset_id = create_asset_txn["confirmation"].get("asset-index")
        tx_id = create_asset_txn.get("tx_id")
        
        # Ensure both asset_id and tx_id are returned correctly
        return self.asset_id, tx_id
    
    def opt_in_asa(self, receiver_address):
        opt_in_txn = self.algorand.send.asset_opt_in(
            AssetOptInParams(
                sender=receiver_address,
                asset_id=self.asset_id
            )
        )
        tx_id = opt_in_txn.get("tx_id")
        return tx_id

    def transfer_asa(self, sender_address, receiver_address, amount):
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

from flask import Flask, render_template, request, redirect, url_for, flash
from algorand_script import AlgorandActions

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize AlgorandActions
algo = AlgorandActions()

# This will store a list of tuples for tx_id, account_address, and state
blockchain_activity = []

@app.route('/')
def index():
    # Pass the blockchain_activity list to the template
    return render_template('index.html', data=blockchain_activity)

@app.route('/generate_account', methods=['POST'])
def generate_account():
    account = algo.generate_account()
    flash(f"Generated Account Address: {account.address}")
    
    # Store the account creation as an activity (no tx_id here)
    blockchain_activity.append((None, account.address, 'Account Created'))
    
    return redirect(url_for('index'))

@app.route('/fund_account', methods=['POST'])
def fund_account():
    address = request.form.get('address')
    tx_id = algo.fund_account(address)
    flash(f"Funded Account: {address}")
    
    # Store the funding as an activity
    blockchain_activity.append((tx_id, address, 'Account Funded'))
    
    return redirect(url_for('index'))

@app.route('/create_asa', methods=['POST'])
def create_asa():
    creator_address = request.form.get('creator_address')
    # Set the account for ASA creation
    algo.set_account(creator_address)  # Use the new set_account method
    
    asset_id, tx_id = algo.create_asa()
    flash(f"Created ASA with Asset ID: {asset_id} and Transaction ID: {tx_id}")
    
    # Store the ASA creation as an activity
    blockchain_activity.append((tx_id, f'ASA {asset_id}', 'ASA Created'))
    
    return redirect(url_for('index'))

@app.route('/generate_receiver_account', methods=['POST'])
def generate_receiver_account():
    account = algo.generate_account()
    flash(f"Generated Receiver Account Address: {account.address}")
    
    # Store the receiver account creation as an activity (no tx_id here)
    blockchain_activity.append((None, account.address, 'Receiver Account Created'))
    
    return redirect(url_for('index'))

@app.route('/opt_in_asa', methods=['POST'])
def opt_in_asa():
    receiver_address = request.form.get('receiver_address')
    tx_id = algo.opt_in_asa(receiver_address)
    flash(f"Opted Receiver Account {receiver_address} into ASA")
    
    # Store the opt-in as an activity
    blockchain_activity.append((tx_id, receiver_address, 'Opted-in ASA'))
    
    return redirect(url_for('index'))

@app.route('/transfer_asa', methods=['POST'])
def transfer_asa():
    sender_address = request.form.get('sender_address')
    receiver_address = request.form.get('receiver_address')
    amount = int(request.form.get('amount'))
    tx_id = algo.transfer_asa(sender_address, receiver_address, amount)
    flash(f"Transferred {amount} units from {sender_address} to {receiver_address}")
    
    # Store the transfer as an activity
    blockchain_activity.append((tx_id, receiver_address, f'Transferred {amount} ASA'))
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

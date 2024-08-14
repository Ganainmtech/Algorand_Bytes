from flask import Flask, render_template, request, redirect, url_for, flash
from algorand_script import AlgorandActions

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize AlgorandActions
algo = AlgorandActions()

# This will store a list of tuples for tx_id, account_address, state, and asset_id
blockchain_activity = []

@app.route('/')
def index():
    # Pass the blockchain_activity list to the template
    return render_template('index.html', data=blockchain_activity)

@app.route('/generate_account', methods=['POST'])
def generate_account():
    account_address = algo.generate_account()
    flash(f"Generated Account Address: {account_address}")
    
    # Store the account creation as an activity (no tx_id or asset_id here)
    blockchain_activity.append((None, account_address, 'Account Created', None))
    
    return redirect(url_for('index'))

@app.route('/fund_account', methods=['POST'])
def fund_account():
    address = request.form.get('address')
    tx_id = algo.fund_account(address)
    flash(f"Funded Account: {address} with Transaction ID: {tx_id}")
    
    # Store the funding as an activity
    blockchain_activity.append((tx_id, address, 'Account Funded', None))
    
    return redirect(url_for('index'))

@app.route('/create_asa', methods=['POST'])
def create_asa():
    creator_address = request.form.get('creator_address')
    
    try:
        asset_id, tx_id = algo.create_asa(creator_address)
        flash(f"Created ASA with Asset ID: {asset_id} and Transaction ID: {tx_id}")
        
        # Store the ASA creation as an activity
        blockchain_activity.append((tx_id, creator_address, 'ASA Created', asset_id))
    except Exception as e:
        flash(f"Error creating ASA: {str(e)}")
    
    return redirect(url_for('index'))

@app.route('/generate_receiver_account', methods=['POST'])
def generate_receiver_account():
    account_address = algo.generate_account()
    flash(f"Generated Receiver Account Address: {account_address}")
    
    # Store the receiver account creation as an activity (no tx_id or asset_id here)
    blockchain_activity.append((None, account_address, 'Receiver Account Created', None))
    
    return redirect(url_for('index'))

@app.route('/opt_in_asa', methods=['POST'])
def opt_in_asa():
    receiver_address = request.form.get('receiver_address')
    
    try:
        tx_id = algo.opt_in_asa(receiver_address)
        flash(f"Opted Receiver Account {receiver_address} into ASA with Transaction ID: {tx_id}")
        
        # Store the opt-in as an activity
        blockchain_activity.append((tx_id, receiver_address, 'Opted-in ASA', algo.asset_id))
    except Exception as e:
        flash(f"Error opting in ASA: {str(e)}")
    
    return redirect(url_for('index'))

@app.route('/transfer_asa', methods=['POST'])
def transfer_asa():
    sender_address = request.form.get('sender_address')
    receiver_address = request.form.get('receiver_address')
    amount = int(request.form.get('amount'))
    
    try:
        tx_id = algo.transfer_asa(sender_address, receiver_address, amount)
        flash(f"Transferred {amount} units from {sender_address} to {receiver_address} with Transaction ID: {tx_id}")
        
        # Store the transfer as an activity
        blockchain_activity.append((tx_id, sender_address, f'Transferred {amount} ASA', algo.asset_id))
    except Exception as e:
        flash(f"Error transferring ASA: {str(e)}")
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

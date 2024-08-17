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
    return render_template('index.html', data=blockchain_activity)

@app.route('/generate_account', methods=['POST'])
def generate_account():
    try:
        account_address = algo.generate_account()
        blockchain_activity.append((None, account_address, 'Account Created', None))
        flash(f"Generated Account Address: {account_address}", 'success')
        return redirect(url_for('index'))
    except Exception as e:
        flash(f"Error generating account: {str(e)}", 'error')
        return redirect(url_for('index'))

@app.route('/fund_account', methods=['POST'])
def fund_account():
    address = request.form.get('address')
    try:
        tx_id = algo.fund_account(address)
        blockchain_activity.append((tx_id, address, 'Account Funded', None))
        flash(f"Funded Account: {address}", 'success')
        return redirect(url_for('index'))
    except Exception as e:
        flash(f"Error funding account: {str(e)}", 'error')
        return redirect(url_for('index'))

@app.route('/create_asa', methods=['POST'])
def create_asa():
    creator_address = request.form.get('creator_address')
    total = int(request.form.get('total'))
    
    try:
        asset_id, tx_id = algo.create_asa(creator_address, total)
        blockchain_activity.append((tx_id, creator_address, 'ASA Created', asset_id))
        flash(f"Created ASA with Asset ID: {asset_id} and a total of {total}", 'success')
        return redirect(url_for('index'))
    except Exception as e:
        flash(f"Error creating ASA: {str(e)}", 'error')
        return redirect(url_for('index'))

@app.route('/opt_in_asa', methods=['POST'])
def opt_in_asa():
    receiver_address = request.form.get('receiver_address')
    
    try:
        tx_id = algo.opt_in_asa(receiver_address)
        flash(f"Opted Receiver Account {receiver_address} into ASA", "opt_in_asa")
        
        # Store the opt-in as an activity
        blockchain_activity.append((tx_id, receiver_address, 'Opted-in ASA', algo.asset_id))
    except Exception as e:
        flash(f"Error opting in ASA: {str(e)}", "opt_in_asa_error")
    
    return redirect(url_for('index'))

@app.route('/transfer_asa', methods=['POST'])
def transfer_asa():
    sender_address = request.form.get('sender_address')
    receiver_address = request.form.get('receiver_address')
    amount = int(request.form.get('amount'))
    
    try:
        tx_id = algo.transfer_asa(sender_address, receiver_address, amount)
        flash(f"Transferred {amount} units from {sender_address} to {receiver_address}", "transfer_asa")
        
        # Store the transfer as an activity
        blockchain_activity.append((tx_id, sender_address, f'Transferred {amount} ASA', algo.asset_id))
    except Exception as e:
        flash(f"Error transferring ASA: {str(e)}", "transfer_asa_error")
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

from fastapi import FastAPI
from fasthtml import HTML, HTMLEngine
from algokit_utils.beta.algorand_client import (
    AlgorandClient,
    AssetCreateParams,
    AssetTransferParams,
    PayParams,
    AssetOptInParams,
)
import uvicorn

app = FastAPI()
engine = HTMLEngine()

# Algorand setup and functions
def setup_algorand():
    algorand = AlgorandClient.default_local_net()
    dispenser = algorand.account.dispenser()

    # Create and fund a new account (creator)
    creator = algorand.account.random()
    algorand.send.payment(
        PayParams(
            sender=dispenser.address,
            receiver=creator.address,
            amount=10_000_000  # Fund with 10 Algos
        )
    )

    # Create a new Algorand Standard Asset (ASA)
    sent_txn = algorand.send.asset_create(
        AssetCreateParams(
            sender=creator.address,
            total=1000,
            asset_name="algofam",
            unit_name="FAM",
            manager=creator.address,
            clawback=creator.address,
            freeze=creator.address
        )
    )

    asset_id = sent_txn["confirmation"]["asset-index"]

    # Create and fund another new account (receiver)
    receiver = algorand.account.random()
    algorand.send.payment(
        PayParams(
            sender=dispenser.address,
            receiver=receiver.address,
            amount=10_000_000  # Fund with 10 Algos
        )
    )

    # Opt-in the receiver account to the newly created ASA
    algorand.send.asset_opt_in(
        AssetOptInParams(
            sender=receiver.address,
            asset_id=asset_id
        )
    )

    # Transfer 10 units of the ASA from creator to receiver
    algorand.send.asset_transfer(
        AssetTransferParams(
            sender=creator.address,
            receiver=receiver.address,
            asset_id=asset_id,
            amount=10  # Transfer amount
        )
    )

    return {
        "creator_address": creator.address,
        "receiver_address": receiver.address,
        "asset_id": asset_id
    }

@app.get("/", response_class=HTML)
async def index():
    return engine.render_string("""
    <html>
        <head>
            <title>Algorand Token Journey</title>
        </head>
        <body>
            <h1>Algorand Token Creation and Transfer</h1>
            <form action="/run" method="post">
                <button type="submit">Run the Script</button>
            </form>
        </body>
    </html>
    """)

@app.post("/run", response_class=HTML)
async def run_script():
    result = setup_algorand()
    return engine.render_string(f"""
    <html>
        <head>
            <title>Result</title>
        </head>
        <body>
            <h1>Script Execution Result</h1>
            <p>Creator Address: {result['creator_address']}</p>
            <p>Receiver Address: {result['receiver_address']}</p>
            <p>Asset ID: {result['asset_id']}</p>
            <a href="/">Go Back</a>
        </body>
    </html>
    """)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

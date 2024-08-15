// Code snippets and their respective sources
const codeSnippets = {
    generateAccount: {
        code: `# Create a new random account\naccountOne = algorand.account.random()`,
        source: "https://github.com/Ganainmtech/Algorand_Bytes/blob/main/localnet_examples/Beginner/01_genAccount.py"
    },
    fundAccount: {
        code: `# Fund an existing account with Algos\nalgorand.send.payment(\n    PayParams(\n        sender=dispenser.address,\n        receiver=accountOne.address,\n        amount=10_000_000  # Fund with 10 Algos\n    )\n)`,
        source: "https://github.com/Ganainmtech/Algorand_Bytes/blob/main/localnet_examples/Beginner/02_fundAccount.py"
    },
    createAsa: {
        code: `# Create a new Algorand Standard Asset (ASA)\nsent_txn = algorand.send.asset_create(\n    AssetCreateParams(\n        sender=accountOne.address,\n        total=1000,\n        asset_name="algofam",\n        unit_name="FAM",\n        manager=accountOne.address,\n        clawback=accountOne.address,\n        freeze=accountOne.address\n    )\n)\n\n# Extract the Asset ID from the transaction confirmation\nasset_id = sent_txn["confirmation"]["asset-index"]`,
        source: "https://github.com/Ganainmtech/Algorand_Bytes/blob/main/localnet_examples/Beginner/03_createAsset.py"
    },
    optInAsa: {
        code: `# Opt-in the receiver account to the newly created ASA\nalgorand.send.asset_opt_in(\n    AssetOptInParams(\n        sender=accountTwo.address,\n        asset_id=asset_id\n    )\n)`,
        source: "https://github.com/Ganainmtech/Algorand_Bytes/blob/main/localnet_examples/Beginner/04_optinAsset.py"
    },
    transferAsa: {
        code: `# Transfer 10 units of the ASA from creator to receiver\nalgorand.send.asset_transfer(\n    AssetTransferParams(\n        sender=accountOne.address,\n        receiver=accountTwo.address,\n        asset_id=asset_id,\n        amount=10  # Transfer amount\n    )\n)`,
        source: "https://github.com/Ganainmtech/Algorand_Bytes/blob/main/localnet_examples/Beginner/05_assetTransfer.py"
    }
};

// Function to handle menu clicks
function handleMenuClick(action) {
    // Load code snippet
    const codeBox = document.getElementById('mainCodeBox');
    const copyBtn = document.getElementById('copyBtn');
    const sourceLink = document.getElementById('sourceLink');

    if (codeSnippets[action]) {
        codeBox.textContent = codeSnippets[action].code;
        sourceLink.href = codeSnippets[action].source;
        Prism.highlightAll(); // Re-highlight the code after updating

        // Update copy button functionality
        copyBtn.onclick = function() {
            navigator.clipboard.writeText(codeSnippets[action].code).then(function() {
                alert('Code copied to clipboard!');
            }).catch(function(err) {
                console.error('Failed to copy code: ', err);
                alert('Failed to copy code.');
            });
        };
    } else {
        console.error('No code snippet found for action:', action);
    }

    // Show the relevant form and hide others
    showForm(`${action}Form`);
}

// Function to show the form based on formId and hide others
function showForm(formId) {
    // Hide all forms
    const forms = document.querySelectorAll('.action-forms form');
    forms.forEach(form => form.style.display = 'none');
    
    // Show the selected form
    document.getElementById(formId).style.display = 'block';
}

// Ensure the JavaScript executes after the DOM has loaded
document.addEventListener('DOMContentLoaded', () => {
    // Add event listeners to menu buttons
    document.getElementById('generateAccountBtn').addEventListener('click', () => handleMenuClick('generateAccount'));
    document.getElementById('fundAccountBtn').addEventListener('click', () => handleMenuClick('fundAccount'));
    document.getElementById('createAsaBtn').addEventListener('click', () => handleMenuClick('createAsa'));
    document.getElementById('optInAsaBtn').addEventListener('click', () => handleMenuClick('optInAsa'));
    document.getElementById('transferAsaBtn').addEventListener('click', () => handleMenuClick('transferAsa'));
});

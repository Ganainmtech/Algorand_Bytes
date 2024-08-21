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

// Initialize currentStep and define the exact steps
let currentStep = 0;
let learningGuideActive = true; // Track if the learning guide is active
const steps = [
    'generateAccount',
    'fundAccount',
    'createAsa',
    'generateAccount',
    'fundAccount',
    'optInAsa',
    'transferAsa'
];

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

// Start journey and show flash message
function startJourney() {
    currentStep = 0; // Start from the first step
    learningGuideActive = true; // Enable learning guide
    updateProgress();

    // Save state to localStorage
    localStorage.setItem('learningGuideActive', 'true');
    localStorage.setItem('currentStep', currentStep);

    // Show flash message
    showFlashMessage("Your journey has started! Hint: Generate your account.");

    // Set button states
    setActiveButton('startJourneyBtn');
}

// Function to turn off learning guide and hide the progress bar
function toggleLearningGuide() {
    learningGuideActive = false;  // Turn off the learning guide

    showFlashMessage("Learning guide off, have fun!");
    
    // Hide the progress bar when the guide is off
    document.querySelector('.progress-container').style.display = 'none';
    
    // Reset progress
    currentStep = 0;

    // Save state to localStorage
    localStorage.setItem('learningGuideActive', 'false');
    localStorage.setItem('currentStep', currentStep);

    // Update progress (though it should just reset and hide the bar)
    updateProgress();

    // Set button states
    setActiveButton('toggleGuideBtn');
}


// Function to show flash messages
function showFlashMessage(message) {
    const flashMessage = document.getElementById('flashMessage');
    flashMessage.textContent = message;
    flashMessage.style.display = 'block';

    // Hide flash message after 3 seconds
    setTimeout(() => {
        flashMessage.style.display = 'none';
    }, 3000);
}

// Move to the next step only if it's the expected step
function nextStep(action) {
    if (!learningGuideActive || steps[currentStep] === action) {
        currentStep++;
        updateProgress();
        return true;  // Allow form submission
    } else {
        alert("Please complete the current step before proceeding.");
        return false;  // Prevent form submission
    }
}

// Update progress bar and steps
function updateProgress() {
    const progressBar = document.getElementById('progressBar');
    const stepsElements = document.querySelectorAll('.step');

    if (learningGuideActive) {
        // Update progress bar width
        progressBar.style.width = (currentStep) * (100 / (steps.length)) + "%";

        // Update active step
        stepsElements.forEach((step, index) => {
            if (index < currentStep) {
                step.classList.add('active');
            } else {
                step.classList.remove('active');
            }
        });

        // Check if all steps are completed
        if (currentStep === steps.length) {
            launchConfetti();  // Trigger confetti if all steps are completed
        }

        // Show the progress container
        document.querySelector('.progress-container').style.display = 'block';
    } else {
        // Hide the progress container
        document.querySelector('.progress-container').style.display = 'none';
    }

    // Save current step to localStorage
    localStorage.setItem('currentStep', currentStep);
}

// Set the active button and reset others
function setActiveButton(activeButtonId) {
    const startJourneyBtn = document.getElementById('startJourneyBtn');
    const toggleGuideBtn = document.getElementById('toggleGuideBtn');

    // Reset button styles
    startJourneyBtn.classList.remove('active');
    toggleGuideBtn.classList.remove('active');

    // Set the appropriate button based on the learning guide state
    if (learningGuideActive) {
        toggleGuideBtn.classList.add('active');  // Learning guide ON
    } else {
        startJourneyBtn.classList.add('active');  // Learning guide OFF
    }

    // Optionally save active button state to localStorage
    localStorage.setItem('activeButton', activeButtonId);
}


// Function to update blockchain activity table (can be called on page load or other events)
function updateBlockchainActivity(activity) {
    const activityTable = document.getElementById('blockchainActivityTableBody');
    activityTable.innerHTML = ''; // Clear existing rows

    activity.forEach(([tx_id, account_address, state, asset_id]) => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${tx_id || '-'}</td>
            <td>${account_address || '-'}</td>
            <td>${state || '-'}</td>
            <td>${asset_id || '-'}</td>
        `;
        activityTable.appendChild(row);
    });
}

// Function to initialize form submission handlers
function initializeFormHandlers() {
    const forms = document.querySelectorAll('.action-forms form');
    forms.forEach((form) => {
        form.addEventListener('submit', function(event) {
            const action = form.id.replace('Form', '');
            if (!nextStep(action)) {
                event.preventDefault(); // Prevent submission if not ready
            } else {
                console.log('Form is being submitted'); 
                form.submit();  // Ensure form submission
            }
        });
    });
}

// Confetti launcher function
function launchConfetti() {
    confetti({
        particleCount: 100,
        spread: 70,
        origin: { y: 0.6 }
    });
}

window.onload = function() {
    // Load current step and learning guide state
    const savedStep = localStorage.getItem('currentStep');
    const savedGuideState = localStorage.getItem('learningGuideActive');
    const savedActiveButton = localStorage.getItem('activeButton');

    // Restore learning guide state and progress
    if (savedGuideState) {
        learningGuideActive = savedGuideState === 'true';
        if (learningGuideActive && savedStep) {
            currentStep = parseInt(savedStep, 10);
            updateProgress();

            // Trigger confetti if progress is 100% after loading the page
            if (currentStep === steps.length) {
                launchConfetti();
            }
        } else {
            // Hide the progress bar if the guide is off
            document.querySelector('.progress-container').style.display = 'none';
        }
    }

    // Restore active button state
    if (savedActiveButton) {
        setActiveButton(savedActiveButton);
    }

    initializeFormHandlers();  // Attach form handlers on page load

    // Add event listeners to nav buttons
    document.getElementById('lightModeBtn').addEventListener('click', function(event) {
        event.preventDefault(); 
        alert("This feature is coming soon!"); 
    });
    document.getElementById('signInBtn').addEventListener('click', function(event) {
        event.preventDefault(); 
        alert("This feature is coming soon!"); 
    });
    document.getElementById('signUpBtn').addEventListener('click', function(event) {
        event.preventDefault(); 
        alert("This feature is coming soon!"); 
    });

    // Add event listeners to menu buttons
    document.getElementById('generateAccountBtn').addEventListener('click', () => handleMenuClick('generateAccount'));
    document.getElementById('fundAccountBtn').addEventListener('click', () => handleMenuClick('fundAccount'));
    document.getElementById('createAsaBtn').addEventListener('click', () => handleMenuClick('createAsa'));
    document.getElementById('optInAsaBtn').addEventListener('click', () => handleMenuClick('optInAsa'));
    document.getElementById('transferAsaBtn').addEventListener('click', () => handleMenuClick('transferAsa'));
    document.getElementById('atomicSwapBtn').addEventListener('click', function(event) {
        event.preventDefault(); 
        alert("This feature is coming soon!"); 
    });

    // Add event listeners to control buttons
    document.getElementById('startJourneyBtn').addEventListener('click', startJourney);
    document.getElementById('toggleGuideBtn').addEventListener('click', toggleLearningGuide);
};


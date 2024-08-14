// Function to clear the message displayed on the page
function clearMessage() {
    document.getElementById('message').innerText = '';
}

// Function to copy the code to the clipboard
function copyCode(elementId) {
    // Get the code element by ID
    const codeElement = document.getElementById(elementId);
    
    // Use the navigator.clipboard API to copy the text to the clipboard
    navigator.clipboard.writeText(codeElement.innerText).then(function() {
        // Show a success message after copying
        alert('Code copied to clipboard!');
    }).catch(function(err) {
        // Handle any errors that occur during the copying process
        alert('Failed to copy code: ', err);
    });
}

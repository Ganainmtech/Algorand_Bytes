// Function to copy the code to the clipboard
function copyCode(elementId) {
    const codeElement = document.getElementById(elementId);
    if (codeElement) {
        navigator.clipboard.writeText(codeElement.innerText).then(function() {
            alert('Code copied to clipboard!');
        }).catch(function(err) {
            console.error('Failed to copy code: ', err);
            alert('Failed to copy code.');
        });
    } else {
        console.error('Element with ID ' + elementId + ' not found.');
        alert('Element not found.');
    }
}

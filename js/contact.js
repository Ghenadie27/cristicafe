// contact.js
// This script handles the form submission for the contact page

document.getElementById('submitBtn').addEventListener('click', async () => {
    const formData = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        message: document.getElementById("message").value,
    };

    try {
        const response = await fetch('https://npft1r7xse.execute-api.us-east-1.amazonaws.com/dev/contact', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        });

        if (response.ok) {
            const result = await response.json();
            alert('Message sent! ' + JSON.stringify(result));
        } else {
            const error = await response.text();
            alert('Error: ' + error);
        }
    } catch (err) {
        alert('Failed to send the message. Please try again.');
    }
});

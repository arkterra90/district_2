document.addEventListener('DOMContentLoaded', function () {
    // Form submission
    document.getElementById('contactForm').addEventListener('submit', function (e) {
        e.preventDefault(); // Prevent the default form submission

        // Collect form data
        var formData = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            phone: document.getElementById('phone').value,
            message: document.getElementById('message').value,
            volunteer: document.getElementById('volunteerCheckbox').checked,
            yardSign: document.getElementById('yardSignCheckbox').checked,
            doorHangers: document.getElementById('doorHangersCheckbox').checked,
            largeSign: document.getElementById('largeSignCheckbox').checked,
            meetAndGreet: document.getElementById('meetAndGreetCheckbox').checked,
        };

        // Send data to Django API
        fetch('/api/contact-form/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') // Add this line to include CSRF token
            },
            body: JSON.stringify(formData)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Handle success response
            console.log('Data sent successfully:', data);
            // Display success message
            alert('Form submitted successfully!');
            // You can perform additional actions here if needed
            document.getElementById('contactForm').reset();
        })
        .catch(error => {
            // Handle error
            console.error('Error sending data:', error);
            // Display error message
            alert('Error submitting form. Please try again.');
            // You can display an error message or perform other actions
        });
    });
});

// Function to get CSRF token from cookies
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var color_sub = 0;

// Function to load chat data and display it on the webpage
function loadChat() {
    // Make a GET request to retrieve the chat data in JSON format from the 'chat_data.json' file
    fetch('chat_data.json')
        .then(response => response.json()) // Convert the response to JSON
        .then(data => {
            // Get the element on the page with the ID 'chat-box'
            const chatBox = document.getElementById('chat-box');
            chatBox.innerHTML = ''; // Clear the current contents of the chat box

            // Reverse the order of the chat data array to show the most recent messages at the top
            data.reverse().forEach(message => {
                // Create new div, paragraph, and span elements to hold the chat message and metadata
                const div = document.createElement('div');
                const p = document.createElement('p');
                const span = document.createElement('span');
                
                // Set the text content of the paragraph to the chat message
                p.textContent = message.chat;
                // Set the text content of the span to the sender's IP address and timestamp, formatted as a local string
                span.textContent = `${message.ip} at ${new Date(message.time).toLocaleString()}`;
                // Style the span to have small font size and a margin to the right
                span.style.fontSize = 'small';
                span.style.marginRight = '10px';

                // Append the span to the div element first, so it appears above the message
                div.appendChild(span);
                // Then append the paragraph (the chat message) to the div
                div.appendChild(p);
                // Finally, append the newly created div to the chat box, adding it to the webpage
                chatBox.appendChild(div);
            });
        })
        .catch(error => console.error('Error fetching chat data:', error)); // Log errors to the console if the fetch operation fails
}

function getUser() {
    // Make a GET request to retrieve the chat data in JSON format from the 'user_data.json' file
    fetch('user_data.json')
        .then(response => response.json()) // Convert the response to JSON
        .then(data => {
                const chatBox = document.getElementById('chat-box');
                chatBox.innerHTML = ''; // Clear the current contents of the chat box
        })
        .catch(error => console.error('Error fetching user data:', error)); // Log errors to the console if the fetch operation fails
}

function change_submit_button() {
    var color_sub_temp = color_sub + 180;
    submit.style.backgroundColor = 'hsl(' + color_sub + ', 50%, 50%)';
    submittemp.style.backgroundColor = 'hsl(' + color_sub_temp + ', 50%, 50%)';
    color_sub += 2;
}

// Set an interval to automatically refresh the chat by calling the loadChat function every 5 seconds
setInterval(loadChat, 5000);

// Set an interval to automatically refresh the chat by calling the loadChat function every 5 seconds
setInterval(getUser, 2501);

// Set an interval to change the color of the submit button every second
setInterval(change_submit_button, 50);

// Call the loadChat function when the window loads to populate the chat on initial page load
window.onload = loadChat;

// Initialize the submit button's color
change_submit_button();

// Function to load chat data and display it
function loadChat() {
    fetch('chat_data.json')
        .then(response => response.json())
        .then(data => {
            const chatBox = document.getElementById('chat-box');
            chatBox.innerHTML = ''; // Clear chat box
            // Reverse the data array to show the most recent messages first
            data.reverse().forEach(message => {
                const div = document.createElement('div');
                const p = document.createElement('p');
                const span = document.createElement('span');
                
                p.textContent = message.chat; // Add message
                span.textContent = `${message.ip} at ${new Date(message.time).toLocaleString()}`;
                span.style.fontSize = 'small';
                span.style.marginRight = '10px';

                div.appendChild(span); // First add the timestamp and IP
                div.appendChild(p); // Then add the chat message
                chatBox.appendChild(div); // Append the new div at the end
            });
        })
        .catch(error => console.error('Error fetching chat data:', error));
}

// Set interval to refresh chat every 5 seconds
setInterval(loadChat, 5000);

// Load chat when the page loads
window.onload = loadChat;

// Function to load chat data and display it
function loadChat() {
    fetch('chat_data.json')
        .then(response => response.json())
        .then(data => {
            const chatBox = document.getElementById('chat-box');
            chatBox.innerHTML = ''; // Clear chat box
            data.forEach(message => {
                const p = document.createElement('p');
                p.textContent = message.chat; // Add message
                chatBox.appendChild(p);
            });
        })
        .catch(error => console.error('Error fetching chat data:', error));
}

// Set interval to refresh chat every 5 seconds
setInterval(loadChat, 5000);

// Load chat when the page loads
window.onload = loadChat;


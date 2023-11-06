# Import required modules: http.server for handling HTTP requests, socketserver for network communication,
# json for data handling, urllib.parse for parsing query strings, and datetime for timestamps
import http.server
import socketserver
import json
from urllib.parse import parse_qs
from datetime import datetime

# Define the port number that the server will listen on
PORT = 58541
# Define the name of the file where chat data will be stored
DATA_FILE = 'chat_data.json'
DATA_FILE_2 = 'user_data.json'

# Create a class called ChatHandler that inherits from SimpleHTTPRequestHandler, which can handle HTTP requests
class ChatHandler(http.server.SimpleHTTPRequestHandler):
    # Define what the server should do when it receives a POST request
    def do_POST(self):
        # Check if the path of the request is '/submit-form', which is the endpoint for submitting chat data
        if self.path == '/submit-form':
            # Get the length of the data that's being posted
            content_length = int(self.headers['Content-Length'])
            # Read the data from the request and decode it from bytes to a UTF-8 string
            post_data = self.rfile.read(content_length).decode('utf-8')
            # Parse the posted data to get the 'chat' field from it
            chat_data = parse_qs(post_data)['chat'][0]

            # Get the IP address of the client that made the request
            ip_address = self.client_address[0]
            # Get the current time and convert it to a string in ISO format
            timestamp = datetime.now().isoformat()

            try:
                # Try to open the chat data file in read mode
                with open(DATA_FILE, 'r') as file:
                    # Load the JSON data from the file
                    data = json.load(file)
            except FileNotFoundError:
                # If the file doesn't exist, start with an empty list to hold chat data
                data = []

            # Append a new dictionary with the chat message, IP address, and timestamp to the list of data
            data.append({
                'chat': chat_data,
                'ip': ip_address,
                'time': timestamp
            })
            
            # Open the chat data file in write mode
            with open(DATA_FILE, 'w') as file:
                # Write the updated list of data to the file as JSON
                json.dump(data, file)

            # Send a 303 See Other response to redirect the client to the root path
            self.send_response(303)
            self.send_header('Location', '/')
            # Finish the headers for the response
            self.end_headers()

            
        elif self.path == '/submit-user':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            user_data = parse_qs(post_data)['username'][0]  # Corrected from ['user'][0] to ['username'][0]
        
            ip_address = self.client_address[0]
        
            try:
                with open(DATA_FILE_2, 'r') as file:  # Corrected from DARA_FILE_2 to DATA_FILE_2
                    data = json.load(file)
            except FileNotFoundError:
                data = []
        
            data.append({
                'user': user_data,
                'ip': ip_address,
            })
            
            with open(DATA_FILE_2, 'w') as file:  # Corrected from DARA_FILE_2 to DATA_FILE_2
                json.dump(data, file)
        
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()
        else:
            # If the path isn't '/submit-form', call the superclass method to handle other POST requests
            super().do_POST()

# Set up the server using an empty string for the host (indicating localhost) and the defined port
httpd = socketserver.TCPServer(("", PORT), ChatHandler)
# Print a message to the console indicating that the server is running and on which port
print(f"Serving at port {PORT}")
# Start the server and have it begin listening for requests
httpd.serve_forever()

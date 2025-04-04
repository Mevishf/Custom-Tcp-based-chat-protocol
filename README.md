# Custom-Tcp-based-chat-protocol

Overview

The Custom TCP Chat Protocol (CTCP) is a structured messaging protocol for a chat server and clients communicating over TCP. It standardizes message exchange, ensuring clear communication between users.

Protocol Structure

Each message follows this format:

[HEADER] | [USERNAME] | [MESSAGE]

Headers:

MSG → Normal chat message.

JOIN → User joining the chat.

EXIT → User leaving the chat.

ERR → Error messages.

Examples:

User joins:

JOIN | Alice | Hello, everyone!

Normal message:

MSG | Alice | How are you all?

User exits:

EXIT | Alice | Goodbye!

Features

Structured message format for better parsing.

Automated broadcasting to notify all users.

Error handling with predefined error messages.

Technologies Used

Programming Language: Python

Networking: Socket programming with TCP

Concurrency: Threading for handling multiple clients

Installation and Setup

Server Setup:

Clone the repository:

git clone  https://github.com/Mevishf/Custom-Tcp-based-chat-protocol.git
cd  Custom-Tcp-based-chat-protocol

Run the server:

python server.py

Client Setup:

Run the client:

python client.py

Enter your username when prompted.

Start chatting with other users.

Future Enhancements

Encrypt messages for security.

Support multimedia messages.

Implement user authentication.

Contributors

Your Name - Developer

License

This project is licensed under the MIT License - see the LICENSE file for details.

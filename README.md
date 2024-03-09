AirBnB Clone Project Overview
This project serves as the groundwork for developing a comprehensive web application mirroring the functionality of AirBnB. It encapsulates the integration of database storage solutions, a functional back-end API, and front-end interaction, marking the preliminary phase of a student initiative to recreate the AirBnB platform. The current phase introduces a back-end console designed for data management, enabling the creation, modification, and deletion of objects, alongside managing persistent storage through JSON serialization/deserialization.

Project Details
The initial phase of the project introduces a foundational step in creating a full-fledged web application inspired by AirBnB. This includes:

A bespoke command-line interface (CLI) for effective data management, coupled with the fundamental classes required for data storage.
The CLI, fashioned after Unix shell interfaces, utilizes the Python CmdModule to interact with users by displaying prompts and processing input commands specific to our project (denoted as 'hbnb').
Key Features and Commands:
Help Command: Displays available commands or detailed information about specific commands.
Syntax: (hbnb) help [command]
Create Command: Generates a new object and outputs its ID.
Syntax: (hbnb) create <ClassName>
Destroy Command: Eliminates an object.
Syntax: (hbnb) destroy <ClassName> <id> or (hbnb) <ClassName>.destroy(<id>)
Show Command: Reveals details of a specific object.
Syntax: (hbnb) show <ClassName> <id> or (hbnb) <ClassName>.show(<id>)
All Command: Lists all objects, or all instances of a specific class.
Syntax: (hbnb) all or (hbnb) all <ClassName>
Starting the Console: Execute ./console.py in the command line.
Quitting the Console: Type (hbnb) quit.
Examples of Help and Quit Commands
Getting Help:(hbnb) help

Documented commands (type help <topic>):
EOF  help  quit
This phase lays the essential groundwork for subsequent development stages, focusing on further integrating and refining the web application's functionalities.







Eye-Park

Eye-Park is an AI-based parking lot monitoring system that uses a Raspberry Pi and an attached camera to monitor parking spots and track the license plates of parked cars. The system is able to check whether a parked car has paid for the parking spot, and send alerts to security if an unauthorized vehicle is parked.
Requirements

To use Eye-Park, you will need:

    A Raspberry Pi 3 or higher
    An SD card with Raspbian installed
    A compatible camera module
    OpenALPR installed on your Raspberry Pi
    A static IP address or DDNS service

Setup

    Install Raspbian on your Raspberry Pi and set up the camera module.
    Clone the Eye-Park repository from Github.
    Install OpenALPR on your Raspberry Pi and set it up according to the instructions provided in the OpenALPR documentation.
    Configure the server by editing the settings.py file with your own settings for the database, email, and other options.
    Set up the DDNS service if you do not have a static IP address.
    Run the server with python manage.py runserver and the client with python client.py.

Theory of Operation

The Eye-Park system is composed of a server, which uses the Django python framework to receive and respond to requests, and a client, which runs on a Raspberry Pi and captures license plate images using OpenALPR.

When a license plate is read, the client sends a GET request to the server containing the number of the parking spot, the license number, and a unique key. If the server responds with a 404 status code, meaning not found, and the user authorizes the vehicle to be added, the client sends a POST request to the server with the parking spot number, the license plate number, and the unique key.

If the system checks with the server and the license plate is not in the database and the user does not input the PIN or accept through the app, the Raspberry Pi client sends a POST request to the server that contains the parking spot number and the license plate number as a JSON file, and the server adds it to the SecurityAlerts database.
OpenALPR Issues

While the algorithm is really good at reading license plates, it can have some troubles in reading a plate correctly when encountering different lighting conditions, when the vehicle is in motion, or different angles. To deal with the majority of these issues, the system loops up to 10 times reading a plate until a correct plate is recognized, giving the system more chances to get a correct reading.
Maintenance Requirements

Due to the active monitoring feature of this project, regular inspections of connectivity of the system as well as status of its camera and processing units are needed. In addition to physical upkeep of the equipment, the server will need monitoring and backup service on a regular basis. Considering the fact that this project is heavily relied upon consuming power for long processing times, it is important to keep the system’s housing box clean of any dust and to inspect the status of ventilation fans and other air intakes. Lastly, it is advisable to keep the camera’s lens clean of any visually obstructing stains which have a tendency to absorb more dust and fumes emitted by surrounding vehicles.

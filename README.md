# Project Title: Remote-Controlled Robot Using Firebase

## Overview:
The project aims to repurpose a vacuum cleaner robot into a remotely controlled robot using Firebase, a platform that provides various services for web and mobile app development. By integrating Firebase's real-time database and cloud services, users will be able to control the robot's movements remotely through a web or mobile interface.

## Components:
- **Vacuum Cleaner Robot:** The base hardware for the project is a vacuum cleaner robot equipped with motors for movement without additional sensors for environment detection.
- **Microcontroller:** A microcontroller, Raspberry Pi, will be used to interface between the robot's hardware and Firebase services. It will interpret commands received from Firebase and control the robot's movements accordingly.
- **Firebase:** Firebase provides the backend infrastructure for the project. This includes the real-time database, authentication, and cloud functions necessary for communication between the remote interface and the robot. Visit here https://github.com/marcelkv/rasBot. I have used his work.
- **Remote Control Interface:** A web application will serve as the remote control interface. Users will interact with this interface to send commands to Firebase, which will then be relayed to the robot via the microcontroller.

## Deployment Steps for the Robot:
1. **Hardware Setup:** Ensure that the vacuum cleaner robot is ready for modification and that the microcontroller is configured to interface with its hardware components.
2. **Firebase Configuration:** Create a Firebase connection and authentication services. Generate the necessary API keys and authentication tokens for accessing Firebase from the microcontroller.
3. **Microcontroller Programming:** Program the microcontroller to establish a connection with Firebase and interpret commands received from the remote control interface. Implement logic to control the robot's movements based on these commands.
4. **Testing and Debugging:** Test the entire system to ensure that commands are transmitted accurately and the robot responds as expected. Debug any issues that arise during testing.
5. **Optimization and Refinement:** Fine-tune the system for optimal performance, considering factors such as latency, reliability, and user experience.

## Conclusion:
By completing these steps, the vacuum cleaner robot will be transformed into a versatile remotely controlled robot, capable of performing various tasks under the user's command. The integration of Firebase adds scalability and real-time capabilities to the system, enhancing its usability and functionality.

## Technologies Used

- Raspberry pi 4 B
- L298N Dual H Bridge Stepper Motor Driver Board
- 12 V Akku
- 20000 mH Powerbank
- Python
- WinSCP

## Installation
**Hardware:**
In response to a malfunctioning control system in the vacuum cleaner robot, a comprehensive overhaul was undertaken. The original control setup was replaced with a custom-built system comprising a Raspberry Pi, a power bank, an H-bridge motor driver, and a 12V battery. Additionally, to accommodate the new components, certain parts of the robot chassis were carefully modified.

Details:

    Replacement Components:
        Raspberry Pi: The Raspberry Pi serves as the central processing unit for the robot, providing the computational power and connectivity required for remote control and automation tasks.
        Power Bank: A portable power bank was integrated to supply power to the Raspberry Pi and other electronic components, ensuring uninterrupted operation without the need for mains power.
        H-Bridge Motor Driver: An H-bridge motor driver was employed to control the movement of the robot's motors. This component facilitates bi-directional control and enables smooth motor operation.
        12V Battery: A high-capacity 12V battery was incorporated to power the robot's motors and provide the necessary voltage for optimal performance.
    Modifications for Space Optimization:
        To accommodate the new control system within the confines of the robot chassis, meticulous adjustments were made to the internal layout.
        In some cases, non-essential parts of the chassis were removed entirely to create additional space for the Raspberry Pi, H-bridge, and other components.
        In instances where space constraints were particularly tight, selective melting or trimming of certain chassis sections was carried out using precision tools such as a soldering iron.

Conclusion:

The replacement of the vacuum cleaner robot's control system marks a significant upgrade in terms of functionality, reliability, and performance. By leveraging modern electronic components and innovative design approaches, the revamped control setup promises enhanced efficiency and versatility. The project showcases a practical example of hardware modification and customization to address technical challenges and achieve desired outcomes in robotics applications.

**Software:**
*Clone the repository:* https://github.com/Schukalla/RasBot.git
*Install the library for firebase on the raspberry:* https://github.com/AMHD/Connecting-Raspberry-Pi-with-Firebase-Database/blob/master/README.md
*Configure Firebase:* https://console.firebase.google.com/u/0/?pli=1




## Usage

1. Open the RasBot web app in your browser.

2. Use the joystick interface to control the robot's movements.

3. Observe the live camera stream to see where the robot is going.

4. The web app sends joystick position data to Firebase, which the Raspberry Pi reads to move the robot accordingly.

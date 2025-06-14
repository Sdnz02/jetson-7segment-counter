7-Segment Counter with Jetson Nano
This project is developed as a homework for the EEE 313 Introduction to Embedded Systems course. It demonstrates a simple 0–9 counter system using a Common Cathode 7-Segment Display and two buttons with an NVIDIA Jetson Nano Developer Kit.

📺 Project Video: Watch on YouTube

🧠 Purpose of the Project
To implement a counter:

Increment from 0 to 9 when the UP button is pressed.

Decrement from 9 to 0 when the DOWN button is pressed.

Display the current count on a 7-segment display.

🔧 Hardware Used
NVIDIA Jetson Nano Developer Kit

Common Cathode 7-Segment Display

2 Push Buttons

Breadboard, jumper wires

🔌 GPIO Pin Connections
Segment	GPIO Pin
A	9
B	11
C	5
D	6
E	13
F	19
G	26
DP	4
UP Button	27
DOWN Button	22

📐 Circuit Schematic
Designed with Fritzing and attached as jetson_finder_schmetics.fzz.

💻 Software and Language
IDE: Thonny

Language: Python 3

Library: Jetson.GPIO

🧾 Code Summary
The main script Code.py:

Initializes GPIO pins.

Handles UP/DOWN button inputs.

Displays numbers (0–9) on the 7-segment.

Uses changeNumber() function to light appropriate segments.

Contains a cleanup step with GPIO.cleanup().

📸 Circuit Photo
📷 Included in homework submission file.

📂 File Structure
bash
Kopyala
Düzenle
project-root/
│
├── Code.py                      # Main Python script
├── jetson_finder_schmetics.fzz # Fritzing circuit design
├── Application Homework-2.docx # Project report with team info
👨‍🔬 Team Members
Suat Deniz

Ata Güneş

⚖️ License
This project is licensed under the MIT License. See the LICENSE file for details.

text
Kopyala
Düzenle
MIT License

Copyright (c) 2025 Suat Deniz

Permission is hereby granted, free of charge, to any person obtaining a copy...

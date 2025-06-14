# 7-Segment Counter with Jetson Nano

This project was developed for the **EEE 313 - Introduction to Embedded Systems** course. It demonstrates a simple up/down counter using a **Common Cathode 7-Segment Display** and **two buttons**, controlled by an **NVIDIA Jetson Nano**.

🎥 **[Project Demo Video](https://youtu.be/OVsHyTpEdF4?feature=shared)**

---

## Purpose

The goal of this project is to:
- Increment a counter from **0 to 9** when the **UP button** is pressed
- Decrement the counter from **9 to 0** when the **DOWN button** is pressed
- Display the current count on a 7-segment display

---

## Hardware Components

- NVIDIA Jetson Nano Developer Kit
- Common Cathode 7-Segment Display
- 2x Push Buttons
- Breadboard & Jumper Wires

---

## GPIO Pin Mapping

| Segment | GPIO Pin |
|---------|----------|
| A       | 9        |
| B       | 11       |
| C       | 5        |
| D       | 6        |
| E       | 13       |
| F       | 19       |
| G       | 26       |
| DP      | 4        |
| UP Button    | 27   |
| DOWN Button  | 22   |

---

## ⚙️ Software Setup

- **IDE**: Thonny
- **Language**: Python 3
- **Library**: Jetson.GPIO

---

## Code Overview

The core functionality is implemented in [`Code.py`](Code.py):

- `changeNumber()` updates the 7-segment display according to the counter
- The main loop detects button presses and updates the counter value
- Segment logic ensures only one digit is shown at a time
- `GPIO.cleanup()` ensures safe GPIO state reset on exit

---

## File Structure

project-root/
├── Code.py # Main Python script
├── jetson_finder_schmetics.fzz # Circuit design (Fritzing)
├── Application Homework-2.docx # Homework report

---

## Team Members

- **Suat Deniz**
- **Ata Güneş**

---

## License

This project is licensed under the MIT License.

MIT License

Copyright (c) 2025 Suat Deniz

Permission is hereby granted, free of charge, to any person obtaining a copy
...

## Notes

- Works with NVIDIA Jetson Nano and Jetson.GPIO library
- Not compatible with Arduino IDE
- Suitable for educational and demonstrative use

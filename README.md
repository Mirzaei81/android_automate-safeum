# Safeum Automation

## Overview
This repository contains a project that uses UiAutomate to automate interactions with the Safeum application. The goal is to perform various tasks within the application automatically and efficiently.

## Prerequisites
- **Python 3.6+**: Ensure you have Python installed on your system.
- **UiAutomator**: An Android UI testing framework.
- **ADB (Android Debug Bridge)**: For communication between your computer and the Android device.

## Installation

1. **Clone the Repository**
    ```sh
    git clone https://github.com/yourusername/safeum-automation.git
    cd safeum-automation
    ```

2. **Install Required Python Packages**
    ```sh
    pip install -r requirements.txt
    ```

3. **Setup UiAutomator**
    - Ensure you have the Android SDK installed.
    - Connect your Android device and enable USB debugging.
    - Use ADB to ensure your device is recognized:
      ```sh
      adb devices
      ```

## Usage

1. **Initialize UiAutomator**
    ```sh
    uiautomator init
    ```

2. **Run Automation Script**
    ```sh
    python automate_safeum.py
    ```

## Project Structure

- `main.py`: Main script to automate tasks within the Safeum application.
- `README.md`: This file.
- `requirements.txt`: List of required Python packages.

## Features

- **Login Automation**: Automatically logs into the Safeum application.
- **Extracting PhoneNumbers Automation**: Exreact phonenumbers basesd on given username and password.

## Contributing
Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

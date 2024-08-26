import psutil
import time
import re
import os
from cryptography.fernet import Fernet
import ctypes
import tkinter as tk
from tkinter import simpledialog

# Configuration
PASSWORD_FILE = "password.dat"
SYSTEM_PROCESSES = set([
    "System Idle Process", "System", "Registry", "smss.exe", "svchost.exe", "csrss.exe", "msedge.exe", "wininit.exe", 
    "winlogon.exe", "services.exe", "lsass.exe", "explorer.exe", "taskhostw.exe"
])
INSTALLER_EXTENSIONS = {".exe", ".msi"}
EXTERNAL_PATHS = {"D:\\", "E:\\", "F:\\", "G:\\", "H:\\", "I:\\", "J:\\", "K:\\", "L:\\", "M:\\", "N:\\", "O:\\", "P:\\", "Q:\\"}  # Example external drive letters
DOWNLOAD_DIRS = {"C:/Users/Zoro/Downloads"}  # Add your user download directories

def generate_key():
    return Fernet.generate_key()

def save_password(password, key):
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())
    with open(PASSWORD_FILE, "wb") as f:
        f.write(key + b"\n" + encrypted_password)

def load_password():
    if not os.path.exists(PASSWORD_FILE):
        return None, None
    with open(PASSWORD_FILE, "rb") as f:
        key = f.readline().strip()
        encrypted_password = f.read()
    cipher_suite = Fernet(key)
    password = cipher_suite.decrypt(encrypted_password).decode()
    return password, key

def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."

    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one number."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character."

    return True, ""

def prompt_for_password():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    entered_password = simpledialog.askstring("Password", "Enter the installation password:", show='*')
    stored_password, _ = load_password()
    return stored_password == entered_password

def block_installation():
    ctypes.windll.user32.MessageBoxW(0, "Installation blocked due to incorrect password.", "Blocked", 0x10)

def is_external_installation(process_path):
    if process_path:
        process_path = os.path.abspath(process_path)
        for path in EXTERNAL_PATHS:
            if process_path.startswith(path):
                return True
        for dir_path in DOWNLOAD_DIRS:
            if process_path.startswith(dir_path):
                return True
    return False

def monitor_installations():
    print("Monitoring for new installations...")
    while True:
        for process in psutil.process_iter(['pid', 'name', 'exe']):
            process_name = process.info['name'].lower()
            process_path = process.info.get('exe')
            if process_path:
                process_path = os.path.abspath(process_path).lower()
                if process_name.endswith(tuple(INSTALLER_EXTENSIONS)) and process_name not in SYSTEM_PROCESSES:
                    if is_external_installation(process_path):
                        print(f"External installation detected: {process.info['name']}")
                        if prompt_for_password():
                            print("Password correct. Allowing installation...")
                        else:
                            print("Password incorrect. Blocking installation...")
                            block_installation()
                    else:
                        print(f"Internal installation detected: {process.info['name']}. No password required.")
        time.sleep(5)  # Adjust monitoring interval as needed

def main():
    stored_password, _ = load_password()
    if stored_password is None:
        root = tk.Tk()
        root.withdraw()  # Hide the main window

        while True:
            password = simpledialog.askstring("Set Password", "Enter a new password:", show='*')
            valid, message = validate_password(password)
            if valid:
                confirm_password = simpledialog.askstring("Confirm Password", "Confirm the new password:", show='*')
                if password == confirm_password:
                    key = generate_key()
                    save_password(password, key)
                    print("Password has been set.")
                    break
                else:
                    print("Passwords do not match.")
                    ctypes.windll.user32.MessageBoxW(0, "Passwords do not match.", "Error", 0x10)
            else:
                print("Password does not meet the criteria.")
                ctypes.windll.user32.MessageBoxW(0, message, "Invalid Password", 0x10)
    else:
        monitor_installations()

if __name__ == "__main__":
    main()

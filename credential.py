import ctypes
import getpass
import time
import os

def set_fullscreen():
    ctypes.windll.kernel32.GetConsoleWindow()
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 3)

def main():
    # Set console window to fullscreen
    set_fullscreen()

    # Prompt for password
    password = getpass.getpass(prompt="Enter your password: ")

    # Check if password is correct (this is a simple example)
    if password == "your_password":
        tm = input("Minutes allowed? ")
        tm = tm * 60
        print(f"Password accepted. Starting {tm!r} minute timer.")
        time.sleep(tm)  # Sleep for 1 hour (3600 seconds)

        # After 1 hour, put the computer to sleep
        print("1-hour timer elapsed. Putting the computer to sleep.")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    else:
        # If password is incorrect, shutdown the computer after 1 minute
        print("Incorrect password. Shutting down the computer in 1 minute.")
        time.sleep(60)  # Sleep for 1 minute
        os.system("shutdown /s /t 1")

if __name__ == "__main__":
    main()

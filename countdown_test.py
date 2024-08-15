import threading
import time

def countdown(seconds):
    while seconds > 0:
        print(f"Countdown: {seconds}", end="\r")
        time.sleep(1)
        seconds -= 1
    print("Countdown finished!")

def user_input_thread():
    input()  # Wait for user input (Enter key)

if __name__ == "__main__":
    seconds = int(input("Enter the countdown duration in seconds: "))
    countdown_thread = threading.Thread(target=countdown, args=(seconds,))
    user_input_thread = threading.Thread(target=user_input_thread)

    countdown_thread.start()
    user_input_thread.start()

    # Wait for the user input thread to finish (meaning the user pressed Enter)
    user_input_thread.join()

    # Terminate the countdown thread
    countdown_thread.join()

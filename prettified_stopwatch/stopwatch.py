#! python3
# stopwatch.py

import time
import pyperclip

def stopwatch():
    """
    Summary:
        Simple stopwatch, prints laps and copies them to clipboard
    """
    # Display the program's instructions.
    print(
        'Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.'
    )

    # Press Enter to begin
    input()  
    print("Started")

    data = ""
    # Get the first lap's start time.
    startTime = time.time()  
    lastTime = startTime
    lapNum = 1

    # Start tracking the lap times.
    # try/except statement to prevent crashing on KeyboardInterrupt
    try:
        while True:
            input()
            lapTime = round(time.time() - lastTime, 2)
            totalTime = round(time.time() - startTime, 2)
            info = f"Lap #{str(lapNum).ljust(2)}: {str(round(totalTime,2)).center(7)} ({str(round(lapTime,2)).rjust(4)})"
            data += info + ",\n"
            print(info, end="")
            lapNum += 1
            # Reset the last lap time.
            lastTime = time.time()  
    except KeyboardInterrupt:
        # Handle the Ctrl-C exception to keep its error message from displaying.
        # Copy to clipboard
        print("\nDone")
        pyperclip.copy(data)
        print("Data copied to clipboard.")

if __name__ == '__main__':
    stopwatch()
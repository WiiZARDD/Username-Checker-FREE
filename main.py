import os
import sys
import time

def clear_console():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def display_loading_spinner():
    spinner_frames = [
        "   .",
        "       .",
        "   . ;.",
        "    .;",
        "     ;;.",
        "   ;.;;",
        "   ;;;;.",
        "   ;;;;;",
        "   ;;;;;",
        "   ;;;;;",
        "   ;;;;;",
        " ..;;;;;..",
        "  ':::::'",
        "    ':`",
    ]

    frame_delay = 0.1
    animation_duration = 5  # Set the duration of the animation in seconds
    start_time = time.time()

    while (time.time() - start_time) < animation_duration:
        clear_console()
        for frame in spinner_frames:
            print(frame)
        spinner_frames.insert(0, spinner_frames.pop())  # Rotate the frames
        time.sleep(frame_delay)

def main():
    clear_console()
    display_loading_spinner()

    # After the animation is complete, start the main script (checker.py)
    os.system("python checker.py")

if __name__ == "__main__":
    main()

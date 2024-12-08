import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_heart():
    frames = [
        "  💖       💖  ",
        " 💖💖     💖💖 ",
        "💖💖💖   💖💖💖",
        " 💖💖💖💖💖💖 ",
        "  💖💖💖💖💖  ",
        "   💖💖💖💖   ",
        "    💖💖💖    ",
        "     💖💖     ",
        "      💖      "
    ]
    for _ in range(3): 
        for frame in frames:
            clear_screen()
            print(frame.center(40))
            time.sleep(0.2)

def love_message():
    clear_screen()
    message = "I ❤️ You Forever!"
    print("\n" * 5) 
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print("\n\n")

if __name__ == "__main__":
    animate_heart()
    time.sleep(1)
    love_message()

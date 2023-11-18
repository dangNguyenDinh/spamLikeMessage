import pyautogui
import pyperclip
import time

def main():
    # Allow the user to open a window or application first
    input("Open the window or application you want to interact with and press Enter.")

    # Specify the Unicode character you want to insert
    unicode_character = "👍"  # Unicode for thumbs up emoji

    # Specify the number of times to insert the Unicode character
    time_ = int(input("Enter the number of times to insert the Unicode character: "))

    # Pause for 5 seconds to allow the user to position the cursor
    print("Wait for 5 seconds to position the cursor.")
    time.sleep(5)

    # Copy the Unicode character to the clipboard and paste it
    for i in range(time_):
        pyperclip.copy(unicode_character)
        pyautogui.hotkey("ctrl", "v")  # Paste from clipboard
        pyautogui.press('enter')

    print("Inserted Unicode character successfully.")

if __name__ == "__main__":
    main()

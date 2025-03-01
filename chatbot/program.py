import pyautogui
import time
import pyperclip

# Give a little time to switch to the application window
time.sleep(2)

# Step 1: Click on the icon at position (1099, 1042)
pyautogui.click(1016, 1050)

# Wait for the application to respond (if needed)
time.sleep(1)

# Step 2: Click and drag from (557, 159) to (1897, 940) to select text
pyautogui.moveTo(679, 231)
pyautogui.dragTo(1764, 970, duration=1.0,button="left")  # Smooth drag




# Step 3: Copy the selected text to the clipboard (Ctrl + C)
pyautogui.hotkey('ctrl', 'c')

time.sleep(1)
pyautogui.click(1764, 970) #deselect after selection
# Give the system a moment to copy the data to the clipboard
time.sleep(0.5)

# Step 4: Use pyperclip to get the copied text from the clipboard
copied_text = pyperclip.paste()

# Print the copied text
print(f"Copied Text: {copied_text}")

import cv2
import os
import numpy as np

def encrypt_message(image_path, secret_msg, passcode, output_path="Batman_encrypted.png"):
    """Encrypts a secret message into an image by modifying pixel values (Blue channel)."""
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found or cannot be opened.")
        return
    
    height, width, _ = img.shape
    total_pixels = height * width

    if len(secret_msg) > total_pixels:
        print("Error: Message is too long to fit in the image.")
        return

    idx = 0  # Track position in the message
    for row in range(height):
        for col in range(width):
            if idx < len(secret_msg):
                char = secret_msg[idx]
                img[row, col, 0] = np.uint8(ord(char))  # Store ASCII in Blue channel
                idx += 1
            else:
                break

    # Save the encrypted image (Use PNG to avoid compression artifacts)
    success = cv2.imwrite(output_path, img)
    if success:
        print(f"Message encrypted and saved as {output_path}")
    else:
        print("Error: Failed to save the encrypted image.")

    return passcode

def decrypt_message(image_path, passcode, original_passcode, msg_length):
    """Decrypts a message hidden in an image, given the correct passcode."""
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found or cannot be opened.")
        return

    if passcode != original_passcode:
        print("YOU ARE NOT AUTHORIZED!")
        return

    decrypted_msg = ""
    idx = 0
    height, width, _ = img.shape

    for row in range(height):
        for col in range(width):
            if idx < msg_length:
                decrypted_msg += chr(img[row, col, 0])  # Convert back to character
                idx += 1
            else:
                break

    print(f"Decrypted message: {decrypted_msg}")

# === Main Execution ===
image_path = "Batman.jpg"  # Replace with your actual image path
secret_msg = input("Enter secret message: ")
passcode = input("Enter a passcode: ")

# Encrypt the message in the image
original_passcode = encrypt_message(image_path, secret_msg, passcode)

# Decrypt the message
entered_passcode = input("Enter passcode for decryption: ")
decrypt_message("Batman_encrypted.png", entered_passcode, original_passcode, len(secret_msg))

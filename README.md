# ACITE-PROJECT-Steganography

Secure Data Hiding in Image Using Steganography
Introduction
This project demonstrates a simple yet effective image steganography technique that hides a secret message inside an image by modifying pixel values. The message is securely stored in the blue channel of the image pixels and can only be retrieved with the correct passcode.

Features
✔️ Encrypt a message into an image using pixel manipulation.
✔️ Decrypt the hidden message with the correct passcode.
✔️ Ensures data security by preventing unauthorized access.
✔️ Uses PNG format to prevent data loss due to compression.

Requirements
Ensure you have Python installed along with the necessary dependencies:

sh
Copy
Edit
pip install opencv-python numpy
How It Works
Encryption Process
The script reads the input image (e.g., Batman.jpg).
It modifies the blue channel of pixels to store the ASCII values of the secret message.
The encrypted image is saved as Batman_encrypted.png.
Decryption Process
The script reads the encrypted image.
If the correct passcode is provided, it extracts and reconstructs the secret message.
If an incorrect passcode is entered, access is denied.
Usage
Encrypt a Message
Place an image (e.g., Batman.jpg) in the working directory.
Run the script and enter a secret message and a passcode.
The encrypted image is saved as Batman_encrypted.png.
Decrypt the Message
Run the script again.
Enter the correct passcode to retrieve the hidden message.

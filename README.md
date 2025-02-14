# Secure Data Hiding in Images Using Steganography

🔒 A Python-based steganography tool that securely hides and retrieves secret messages within images using pixel manipulation.This project demonstrates a simple yet effective image steganography technique that hides a secret message inside an image by modifying pixel values. The message is securely stored in the blue channel of the image pixels and can only be retrieved with the correct passcode.

---

## 🚀 Features  

✔ **Encrypt Messages** – Hide a secret message within an image by modifying pixel values.  
✔ **Decrypt Securely** – Retrieve the hidden message only with the correct passcode.  
✔ **Data Security** – Prevents unauthorized access using passcode-based protection.  
✔ **Lossless Encryption** – Uses PNG format to ensure no data loss due to compression.  

---

## 📌 Requirements  

Ensure you have Python installed along with the required dependencies:  

```sh
pip install opencv-python numpy
```

---

## 🔧 How It Works  

### 🖼 Encryption Process  
1️⃣ The script reads the input image (e.g., `Batman.jpg`).  
2️⃣ It modifies the **blue channel** of the image pixels to store the **ASCII values** of the secret message.  
3️⃣ The encrypted image is saved as `Batman_encrypted.png`.  

### 🔓 Decryption Process  
1️⃣ The script reads the **encrypted image**.  
2️⃣ If the **correct passcode** is provided, it extracts and reconstructs the **hidden message**.  
3️⃣ If an **incorrect passcode** is entered, access is **denied**.  

---

## 📌 Usage  

### 🔐 Encrypt a Message  
1️⃣ Place an image (e.g., `Batman.jpg`) in the working directory.  
2️⃣ Run the script and enter a **secret message** and a **passcode**.  
3️⃣ The encrypted image is saved as `Batman_encrypted.png`.  

### 🕵 Decrypt the Message  
1️⃣ Run the script again.  
2️⃣ Enter the **correct passcode** to retrieve the hidden message.  

---

## 🛠 Technologies Used  

🔹 **Python** – Core programming language  
🔹 **OpenCV** – Image processing library  
🔹 **NumPy** – For efficient data manipulation  

---

## 🔽 How to Clone the Repository  

To get a copy of this project on your local machine, follow these steps:  

1️⃣ **Open Terminal / Command Prompt**  
2️⃣ Run the following command to clone the repository:  

```sh
git clone https://github.com/your-username/ACITE-PROJECT-Steganography.git
```

3️⃣ Navigate into the project folder:  

```sh
cd ACITE-PROJECT-Steganography
```

4️⃣ Install dependencies:  

```sh
pip install opencv-python numpy
```

5️⃣ Run the script:  

```sh
python steganography.py
```

---

## 📜 License  

📄 This project is licensed under the **MIT License** – feel free to modify and share!  

---

## 🤝 Contributing  

🔹 **Fork the repository**  
🔹 **Create a new branch** (`feature-branch`)  
🔹 **Commit your changes**  
🔹 **Push to your branch**  
🔹 **Submit a Pull Request**  

---

## 📬 Contact  

✉ **Your Name** – [Your Email]  
📌 **GitHub** – [Your GitHub Profile]  

🔥 **If you like this project, don’t forget to give it a ⭐ on GitHub!**  

---

This README file is now **well-structured, visually appealing, and includes cloning instructions**. 🚀 Let me know if you need any modifications! 😃

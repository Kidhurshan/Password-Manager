# 🔒 Password Manager

A simple Python-based Password Manager that allows you to securely store and retrieve passwords using encryption. 🛡️

## ✨ Features
- **➕ Add Passwords**: Store usernames and encrypted passwords in a file.
- **👀 View Passwords**: Decrypt and view stored passwords.
- **🔐 Secure Encryption**: Uses the `cryptography.fernet` module for encryption and decryption of passwords.

## ⚙️ How It Works
1. **🔑 Generate Encryption Key**: 
   - The key is generated using the `add_key` method and saved in a file named `key.key`. 
   - This key is essential for encrypting and decrypting passwords.
   - **⚠️ Note**: Ensure the `key.key` file is kept secure. Losing it will result in being unable to decrypt stored passwords.

2. **🔒 Encryption and Decryption**:
   - Passwords are encrypted when stored and decrypted when viewed using the `cryptography.fernet.Fernet` class.

3. **💻 User Interface**:
   - The program provides two options:
     - **➕ Add Passwords**: Store a username and an encrypted password.
     - **👀 View Passwords**: Retrieve and decrypt stored passwords.
   - Type `❌ q` to exit the program.

## 🚀 Setup and Usage
### 📋 Prerequisites
- 🐍 Python 3.6 or higher.
- Install the `cryptography` module:
  ```bash
  pip install cryptography

![image](https://github.com/user-attachments/assets/0284e210-16ca-4883-a10e-ea5595f7e1d3)

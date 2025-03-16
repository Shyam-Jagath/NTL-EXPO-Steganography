from cryptography.fernet import Fernet

# Step 1: Generate or load a secret key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Step 2: Take user input
message = input("Enter your message: ").encode()

# Step 3: Encrypt the message
encrypted_message = cipher_suite.encrypt(message)

# Step 4: Append to image
file_path = 'images/Snowbell.png'

with open(file_path, 'ab') as file:
    file.write(encrypted_message)

print(f"Encrypted message stored in {file_path}!")
print(f"Encryption Key (Save this!): {key.decode()}")

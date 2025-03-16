from cryptography.fernet import Fernet

key=input("Enter the key: ").encode()
cipher_key=Fernet(key)

file_path ='image_path'
with open(file_path, 'rb') as file:
    decrypted_message = file.read()
    hidden_data_start=decrypted_message.index(bytes.fromhex('FFD9'))
    file.seek(hidden_data_start+2)
    encrypted_message = file.read()

    decrypted_message = cipher_key.decrypt(encrypted_message).decode()
print(f"Decrypted message: {decrypted_message}")
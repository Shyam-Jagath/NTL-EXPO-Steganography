import PIL.Image
import io
from cryptography.fernet import Fernet

key=input("Enter the key: ").encode()
cipher_key=Fernet(key)

with open('image_path', 'rb') as file:
    content = file.read()

    hidden_data_start = content.index(bytes.fromhex('FFD9')) + 2
    file.seek(hidden_data_start)

    encrypted_data = file.read()

    decrypted_data = cipher_key.decrypt(encrypted_data)

    new_image = PIL.Image.open(io.BytesIO(decrypted_data))

    new_image.save('decrypted_image.png')

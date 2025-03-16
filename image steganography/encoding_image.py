import PIL.Image
import io
from cryptography.fernet import Fernet

key=Fernet.generate_key()
cipher_key=Fernet(key)

image=PIL.Image.open('image_path')
byte_array=io.BytesIO()
image.save(byte_array, format='PNG')
image_data=byte_array.getvalue()

encrypted_data=cipher_key.encrypt(image_data)

with open('image_path', 'ab') as file:
    file.write(encrypted_data)

print(f"Key -> {key.decode()}")
print("Image has been encrypted successfully")
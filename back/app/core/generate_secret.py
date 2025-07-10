import secrets
import base64

secret_key = secrets.token_bytes(32)

encoded_key = base64.urlsafe_b64encode(secret_key).decode()

print(encoded_key)
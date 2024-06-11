import hashlib


def hash_password(password):
    if not password:
        raise ValueError("Password cannot be empty")  # Raise error if password is empty
    return hashlib.sha256(password.encode()).hexdigest()
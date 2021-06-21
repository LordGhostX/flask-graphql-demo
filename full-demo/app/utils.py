import secrets


def generate_id(n=10):
    return secrets.token_urlsafe(n).lower()

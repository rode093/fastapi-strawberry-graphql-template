
from services.config import Config


def create_password_hash(plain_text: str) -> str:
    import bcrypt
    security_key = Config().get('security_key')
    if security_key == None or len(security_key) == 0:
        raise Exception(message="Invalid Security Key")
    return bcrypt.hashpw(plain_text, security_key)

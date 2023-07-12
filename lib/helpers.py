
from xmlrpc.client import Boolean
from services.config import Config


def create_password_hash(plain_text: str) -> str:
    import bcrypt
    security_key = Config().get('security_key')
    if security_key == None or len(security_key) == 0:
        raise Exception(message="Invalid Security Key")
    return bcrypt.hashpw(plain_text+security_key, bcrypt.gensalt(10))


def compare_password_hash(plain_text: str, hash: str) -> Boolean:
    import bcrypt
    return bcrypt.checkpw(plain_text, hash)

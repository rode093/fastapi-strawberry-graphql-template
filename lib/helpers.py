
from xmlrpc.client import Boolean
from services.config import Config
import bcrypt


def create_password_hash(plain_text: str) -> str:
    security_key = Config().get('security_key')
    if security_key == None or len(security_key) == 0:
        raise Exception(message="Invalid Security Key")
    return bcrypt.hashpw(str(plain_text+security_key).encode("utf-8"), bcrypt.gensalt(10))


def compare_password_hash(plain_text: str, hash: str) -> Boolean:
    security_key = Config().get('security_key')
    if security_key == None or len(security_key) == 0:
        raise Exception(message="Invalid Security Key")
    return bcrypt.checkpw(str(plain_text+security_key).encode("utf-8"), hash)

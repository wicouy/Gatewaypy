# managements/token_management
import jwt
from datetime import datetime, timedelta

class TokenManagement:
    def __init__(self, config):
        self.config = config

    def get_secret_key(self):
        secret_key = self.config.get('SecretKey')
        expiration_hours = self.config.get('TokenExpirationHours')
        if secret_key is None:
            raise ValueError("La clave secreta no está configurada en la configuración.")
        return secret_key, expiration_hours

    def generate_token(self, payload):
        secret_key, expiration_hours = self.get_secret_key()
        expiration = datetime.now() + timedelta(hours=expiration_hours)
        payload['exp'] = expiration
        token = jwt.encode(payload, secret_key, algorithm='HS256')
        return token

    def refresh_token(self, token):
        secret_key, expiration_hours = self.get_secret_key()
        payload = self.validate_token(token, secret_key)
        if payload:
            new_token = self.generate_token(payload)
            return new_token
        else:
            return None

    def validate_token(self, token, secret_key):
        try:
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            # El token ha expirado
            return None
        except jwt.InvalidTokenError:
            # El token no es válido
            return None

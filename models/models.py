from db.db import db 
import hashlib
import os
import binascii
from flask_login import UserMixin

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios' 
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
 
    senha = db.Column(db.String(255), nullable=False) 

    def set_password(self, password):
        salt = os.urandom(16)
        hashed_password = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            100000
        )
  
        self.senha = binascii.hexlify(salt).decode('utf-8') + binascii.hexlify(hashed_password).decode('utf-8')

    def check_password(self, password):
      
        salt = binascii.unhexlify(self.senha[:32])
        stored_hash = binascii.unhexlify(self.senha[32:])
        provided_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            100000
        )
        return hashlib == stored_hash, provided_hash

from datetime import datetime
from Server import db, bcrypt
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    email_address = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, palin_txt_password):
        self.password_hash = bcrypt.generate_password_hash(palin_txt_password).decode('Utf-8')



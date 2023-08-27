## models.py

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from typing import Any

db = SQLAlchemy()

class User(UserMixin, db.Model):
    """User model."""
    
    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(20), unique=True, nullable=False)
    password: str = db.Column(db.String(60), nullable=False)
    created_at: datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at: datetime = db.Column(db.DateTime, onupdate=datetime.utcnow)
    recipes = db.relationship('Recipe', backref='author', lazy=True)

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def check_password(self, password: str) -> bool:
        return self.password == password

class Recipe(db.Model):
    """Recipe model."""
    
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), nullable=False)
    ingredients: str = db.Column(db.Text, nullable=False)
    cost: float = db.Column(db.Float, nullable=False)
    created_at: datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at: datetime = db.Column(db.DateTime, onupdate=datetime.utcnow)
    user_id: int = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, name: str, ingredients: str, cost: float) -> None:
        self.name = name
        self.ingredients = ingredients
        self.cost = cost

    def calculate_cost(self) -> float:
        return self.cost

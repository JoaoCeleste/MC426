from models.database import db
from sqlalchemy.sql import func

class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user_.id'))
    created_at = db.Column(db.DateTime, default=func.now())

    user = db.relationship('User', back_populates='comments')
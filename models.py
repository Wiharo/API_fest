from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    accounts = db.relationship("Account", backref="user")
    # transactions = db.relationship("Transaction", backref="user")


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


class Fest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    date_time = db.Column(db.Text, nullable=False)
    category_name = db.Column(db.Text, nullable=False)
    price = db.Column(db.String, nullable=False)
    location = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "date_time": self.date_time,
            "category_id": self.category_name,
            "price": self.price,
            "location": self.location
        }

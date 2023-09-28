from models import User, Account, Fest
from app import db


def create_user(username, password, email):
    user = User(username=username, password=password, email=email)
    try:
        db.session.add(user)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False


def get_user_id(username):
    user = User.query.filter_by(username=username).first()
    return user.id


def authenticate_user(username, password):
    user = User.query.filter_by(username=username, password=password).first()
    return user


def create_account(user_id):
    account = Account(user_id=user_id)
    try:
        db.session.add(account)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False


def add_fest(name, description, date_time, category_name, price, location):
    new_fest = Fest(name=name, description=description, date_time=date_time, category_name=category_name,
                    price=price, location=location)
    db.session.add(new_fest)
    db.session.commit()


def delete_fest_by_name(name):
    fest = Fest.query.filter_by(name=name).first()

    if fest:
        db.session.delete(fest)
        db.session.commit()
        return True
    return False

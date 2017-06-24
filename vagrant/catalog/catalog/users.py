from flask import session as login_session
from catalog import db
from catalog.models import User


def create_user(login_session):
    newUser = User(
        name = login_session['username'],
        email = login_session['email'],
        picture = login_session['picture'])
    db.add(newUser)
    db.commit()
    user = db.query(User).filter_by(email = login_session['email']).one()
    return user.id

def get_user_id(email):
    try:
        user = db.query(User).filter_by(email = email).one()
        return user.id
    except:
        return None

def get_user_info(user_id):
    user = db.query(User).filter_by(id=user_id).one()
    return user

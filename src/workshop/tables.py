import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.Text, unique=True)
    username = sa.Column(sa.Text, unique=True)
    profile_child = relationship("Profile", backref="users", uselist=False)

    hash_password = sa.Column(sa.Text)


class Operation(Base):
    __tablename__ = 'operations'

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    date = sa.Column(sa.Date)
    kind = sa.Column(sa.String)
    amount = sa.Column(sa.Numeric(10, 2))
    description = sa.Column(sa.String, nullable=True)


class Profile(Base):
    __tablename__ = 'profiles'

    id = sa.Column(sa.Integer, primary_key=True)
    user_parent = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    creation_date = sa.Column(sa.Date)
    name = sa.Column(sa.String)
    last_name = sa.Column(sa.String)
    birth_date = sa.Column(sa.Date)



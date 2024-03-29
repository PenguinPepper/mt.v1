#!/usr/bin/env python3
"""
Contains the user class
"""

import models
from models.user_model import UserModel, Base
from dotenv import load_dotenv
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


load_dotenv()

class User(UserModel, Base):
    """
    Class for users

    Attributes:
        __init__(): initialises the reiew object
        email (str): contains email of user
        password (str): contains password for profile
        first_name (str): name of user
        last_name (str): last name of user
        cohort_no (int): cohort that user belongs to.
    """

    if models.storage_t == "db":
        __tablename__ = 'users'
        email = Column(String(120), nullable=False)
        password = Column(String(120), nullable=False)
        name = Column(String(120), nullable=False)
        surname = Column(String(120), nullable=False)
        github_name = Column(String(120), nullable=False)
        cohort_no = Column(String(5), nullable=False)
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        github_name = ""
        cohort_no = ""

    def __init__(self, *args, **kwargs):
        """Initialise User"""
        super().__init__(*args, **kwargs)

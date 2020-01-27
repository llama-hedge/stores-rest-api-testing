"""
BaseTest

This class should be the parent class for non-unit tests. It instantiates a database dynamically and makes sure that it
is a new, blank database for each test

"""
from unittest import TestCase
from app import app
from db import db


class BaseTest(TestCase):
    @classmethod
    def setUpClass(cls):
        # setUpClass runs once per test case, as opposed to setUp which runs once per test method
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        app.config['DEBUG'] = False
        app.config['PROPAGATE_EXCEPTIONS'] = True
        with app.app_context():
            db.init_app(app)

    def setUp(self):
        # Make sure the database exists
        # this creates a blank sqlite file

        with app.app_context():
            # this is a flask thing that creates a fake app to test
            db.create_all()
        # get a test client
        self.app = app.test_client
        self.app_context = app.app_context

    def tearDown(self) -> None:
        # tearDown runs after every test
        with app.app_context():
            db.session.remove()
            db.drop_all()

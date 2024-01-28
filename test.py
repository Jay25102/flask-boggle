from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def setUp(self):
        self.client = app.test_client()
        app.config["TESTING"] = True

    def test_gameboard(self):
        with self.client:
            response = self.client.get("/board")
            self.assertIn(session.get("highscore"))
            self.assertIn(session.get("nplays"))
            self.assertIn(b'<h2>Score', response.data)
            self.assertIn(b'<div>Played:', response.data)
            self.assertIn(b'<div>Highscore:', response.data)
            self.assertIn(b'<div>Time left:', response.data)


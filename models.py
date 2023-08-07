from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class WebPage(db.Model):
    __tablename__ = 'web_page'

    id = db.Column(db.Integer, primary_key = True)
    long_url = db.Column(db.String())
    short_url = db.Column(db.String())

    def __init__(self, long_url,short_url):
        self.long_url = long_url
        self.short_url = short_url

    def __repr__(self):
        return f"{self.short_url}:{self.id}"

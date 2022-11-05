from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class db_time(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    series_name = db.Column(db.String)
    timestamp = db.Column(db.DateTime, nullable=False)
    value = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "Print something important"
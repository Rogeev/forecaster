import pandas as pd
from web_app.model import db, db_time

file_db = pd.read_csv('daily_consumption.csv')

def save_db(file_db):
    new_db = db_time(series_name=file_db['Site ID'], value=file_db['Energy Consumption (kWh)'], timestamp=file_db['Date'])
    db.session.add(new_db)
    db.session.commit()

if __name__ == '__main__':
    save_db(file_db)
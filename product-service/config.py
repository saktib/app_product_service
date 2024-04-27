import os

class Config:
    dbhost = os.environ.get('MYSQL_HOST')
    dbport = os.environ.get('MYSQL_PORT')
    dbuser = os.environ.get('MYSQL_USER')
    dbpassword = os.environ.get('MYSQL_PASSWORD')
    dbname = os.environ.get('MYSQL_DATABASE')

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{dbuser}:{dbpassword}@{dbhost}:{dbport}/{dbname}?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
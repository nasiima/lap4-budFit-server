import os



# SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://')

SQLALCHEMY_DATABASE_URI = 'postgresql://qmcuqdtwphecds:0bd4056db7ad5dda50da5e6d5ce64e7efdf08384b9445dbfb9381f9c50334aa8@ec2-99-80-170-190.eu-west-1.compute.amazonaws.com:5432/d28ps4h9no69kj'


SECRET_KEY = os.environ.get('SECRET_KEY')
# SECRET_KEY ='1eedds23rrr4rrrfrw'
SQLALCHEMY_TRACK_MODIFICATIONS = False



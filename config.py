from configparser import ConfigParser


configur = ConfigParser()
configur.read("config.ini")


APP_NAME = "TINYURL"
ENVIRONMENT='LOCAL_ENV' 

EXPIRY = 60*15

REDIS_HOST = configur.get(ENVIRONMENT, "redis_host")
REDIS_PORT = configur.get(ENVIRONMENT, "redis_port")

SQLALCHEMY_DATABASE_URI = f'{configur.get(ENVIRONMENT, "sqlalchemy_url")}?application_name={APP_NAME}_initialize'
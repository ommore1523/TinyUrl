from configparser import ConfigParser


configur = ConfigParser()
configur.read("config.ini")


APP_NAME = "TINYURL"


EXPIRY = 60*15
ENVIRONMENT="LOCAL_ENV"

REDIS_PORT = configur.get(ENVIRONMENT, "redis_port")
REDIS_HOST = configur.get(ENVIRONMENT, "redis_host")

SQLALCHEMY_DATABASE_URI = f'{configur.get(ENVIRONMENT, "sqlalchemy_url")}?application_name={APP_NAME}_initialize'
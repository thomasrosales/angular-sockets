import os
from os import environ, path
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = environ.get("SECRET_KEY")
    JWT_SECRET_KEY = environ.get("JWT_SECRET_KEY")
    JWT_ALGORITHM = environ.get("JWT_ALGORITHM", "HS256")
    JWT_HEADER_TYPE = environ.get("JWT_HEADER_TYPE", "JWT")
    JWT_IDENTITY_CLAIM = environ.get("JWT_IDENTITY_CLAIM", "identity")
    JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]
    JWT_BLACKLIST_ENABLED = environ.get("JWT_BLACKLIST_ENABLED", True)
    JWT_COOKIE_CSRF_PROTECT = environ.get("JWT_COOKIE_CSRF_PROTECT", True)
    ALLOWED_EXTENSIONS = ["txt", "pdf", "png", "jpg", "jpeg", "gif"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    FLASK_ENV = "production"
    TESTING = False

    DB_HOST = environ.get("DATABASE_URL")
    DB_USERNAME = environ.get("DB_USERNAME")
    DB_PASSWORD = environ.get("DB_PASSWORD")
    DB_NAME = environ.get("DB_NAME")
    DB_TYPE = environ.get("DB_TYPE")
    DB_CONNECTOR = environ.get("DB_CONNECTOR")
    DB_PORT = environ.get("DB_PORT", 5432)

    SQLALCHEMY_URL = f"{DB_TYPE}+{DB_CONNECTOR}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    SQLALCHEMY_URL = environ.get("DATABASE_URL")


class DevelopmentConfig(Config):
    FLASK_APP = environ.get("FLASK_APP", "app")
    FLASK_ENV = "development"
    DEBUG = True
    SERVER_NAME = environ.get("SERVER_NAME", "localhost:5000")
    SESSION_COOKIE_DOMAIN = environ.get("SERVER_NAME", "localhost:5000")

    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_USERNAME = environ.get("DB_USERNAME", "flask")
    DB_PASSWORD = environ.get("DB_PASSWORD", "admin")
    DB_NAME = environ.get("DB_NAME", "spirosscovid")
    DB_TYPE = environ.get("DB_TYPE", "postgresql")
    DB_CONNECTOR = environ.get("DB_CONNECTOR", "psycopg2")
    DB_PORT = environ.get("DB_PORT", 5432)

    SQLALCHEMY_URL = f"{DB_TYPE}+{DB_CONNECTOR}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


class TestingConfig(Config):
    DEBUG = True


config = {"development": DevelopmentConfig(), "production": ProductionConfig()}

from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()


class Config:
    """Base configuration class."""
    APP_NAME = os.getenv('APP_NAME', 'MyApp')
    DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')
    TESTING = os.getenv('TESTING', 'False').lower() in ('true', '1', 't')
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///default.db')


config = Config()


def get_config():
    """Returns the configuration object."""
    return config


def is_debug_mode():
    """Checks if the application is in debug mode."""
    return config.DEBUG


def is_testing_mode():
    """Checks if the application is in testing mode."""
    return config.TESTING


def get_database_url():
    """Returns the database URL."""
    return config.DATABASE_URL


def get_app_name():
    """Returns the application name."""
    return config.APP_NAME
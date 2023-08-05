import os
import pathlib
from datetime import timedelta
from typing import Optional
from functools import lru_cache


class BaseConfig:
    SERVER_ID: str = pathlib.Path(os.getcwd()).parts[-1]
    PROCESS_COUNT: int = 10

    # JWT configs.
    JWT_SECRET_KEY: Optional[str] = os.environ.get('JWT_SECRET_KEY')
    JWT_ALGORITHM = 'HS256'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15) \
        if os.environ.get('FLASK_ENV') == 'production' else timedelta(seconds=36000)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(hours=10)

    # SQLAlchemy configs.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PG_USER = os.environ.get('PG_USER', 'postgres')
    PG_PASSWORD: Optional[str] = os.environ.get('PG_PASSWORD')
    PG_HOST = os.environ.get('PG_HOST', 'localhost')
    PG_PORT = os.environ.get('PG_PORT', 5432)
    PG_DB = os.environ.get('PG_DB', SERVER_ID if os.environ.get('ENV') == 'production' else f'{SERVER_ID}_dev')

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return f'postgresql://{self.PG_USER}:{self.PG_PASSWORD}@{self.PG_HOST}:{self.PG_PORT}/{self.PG_DB}'

    @property
    def ASYNC_SQLALCHEMY_DATABASE_URI(self):
        return f'postgresql+asyncpg://{self.PG_USER}:{self.PG_PASSWORD}@{self.PG_HOST}:{self.PG_PORT}/{self.PG_DB}'

    # Celery configs.
    broker_url = f'redis://{os.environ.get("REDIS_HOST")}:{os.environ.get("REDIS_PORT", 6379)}/0'
    result_backend = f'redis://{os.environ.get("REDIS_HOST")}:{os.environ.get("REDIS_PORT", 6379)}/0'
    accept_content = ['application/json']
    task_serializer = 'json'
    result_serializer = 'json'
    redis_max_connections = 5


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True


class ProductionConfig(BaseConfig):
    """Production configuration."""
    DEBUG = False


class TestingConfig(BaseConfig):
    """Testing configuration with postgres."""
    TESTING = True


class TestingConfigSqlite(BaseConfig):
    """Testing configuration with sqlite in memory."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


@lru_cache()
def get_settings():
    config_cls_dict = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        # Use PostgreSQL DB if USE_PG environment variable is set, else default to sqlite in memory.
        'testing': TestingConfig if os.environ.get('USE_PG', '') else TestingConfigSqlite,
    }

    config_name = os.environ.get('FASTAPI_ENV', 'development')
    config_cls = config_cls_dict[config_name]

    return config_cls()


settings = get_settings()

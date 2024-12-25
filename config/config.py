from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic.networks import PostgresDsn

class Config(BaseSettings):
    DATABASE_URL: PostgresDsn = "postgresql://user:password@localhost/dbname"
    
    model_config = SettingsConfigDict(env_file=".env")


cfg = Config()

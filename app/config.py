from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    debug: bool = False

    # Yangi uslub (Pydantic V2 uchun):
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
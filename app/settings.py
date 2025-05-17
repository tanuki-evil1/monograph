from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_username: str
    database_password: str
    database_host: str
    database_port: int
    database_name: str

    @property
    def database_url(self) -> str:
        """Url database."""
        return (
            f"postgresql+asyncpg://{self.database_username}:{self.database_password}@{self.database_host}:"
            f"{self.database_port}/{self.database_name}"
        )

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)


settings = Settings()

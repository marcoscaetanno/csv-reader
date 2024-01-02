from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    port: int = 8080
    smpt_server: str = "your.email.server.com"
    sender_email: str = "your-email@here.com"
    password: str = "your_email.Password"
    db_name: str = "imports"
    db_user: str = "postgres"
    db_password: str = "postgres"
    db_host: str = "localhost"
    db_port: int = 5432
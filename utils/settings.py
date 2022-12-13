import json
from dataclasses import dataclass

from models.user import User


class Settings:
    def __init__(self):
        self.app_name: str = 'CyberController™ by CyberFox'
        self.config_path: str = 'config.json'
        self.user: User | None = None
        self.user_path: str | None = None

        try:
            with open(self.config_path, 'r') as f:
                config = json.load(f)
                if 'current_user_path' in config:
                    self.user = User(config['current_user_path'])
                else:
                    self.user = User()
                    self.user_path = self.user.filename
                    self.export_settings()

        except Exception:
            self.user = User()
            self.export_settings()
            self.user.save_to_file()

    def export_settings(self):
        with open(self.config_path, 'w') as f:
            json.dump(
                obj={
                    'current_user_path': self.user.filename
                },
                fp=f,
                indent=2,
                ensure_ascii=False
            )


settings = Settings()

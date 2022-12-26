import json

from models.cyber.cybernetics_base import CyberBase


class User:
    def __init__(self, config_path: str | None = None):
        if config_path:
            with open(config_path, 'r') as f:
                config = json.load(f)
                self.name: str = config['name']
                self.filename: str = config['filename']
                self.emp_max: int = config['emp_max']
                self.emp_current: int = config['emp_current']
                self.emp_mod: int = config['emp_mod']
                self.hp_mod: float = config['hp_mod']
                self.cybernetics: list[CyberBase] = self.load_cybernetics(config['cybernetics'])
        else:
            self.name: str = 'User'
            self.filename: str = 'default.json'
            self.emp_max: int = 6
            self.emp_current: int = 6
            self.emp_mod: int = 0
            self.hp_mod: float = 0.0
            self.cybernetics: list[CyberBase] = list()

    def get_hp(self) -> float:
        return 0.0 + self.hp_mod

    def get_emp(self) -> int:
        return self.emp_current + self.emp_mod

    def load_cybernetics(self, cyber_list) -> list[CyberBase]:
        cybernetics = []
        for implant_dict in cyber_list:
            if implant_dict['sockets']:
                sockets = self.load_cybernetics(implant_dict['sockets'])
            elif implant_dict['sockets'] is None:
                sockets = None
            else:
                sockets = []
            del implant_dict['sockets']
            implant = CyberBase(**implant_dict)
            implant.sockets = sockets
            cybernetics.append(implant)
        return cybernetics

    def export_cybernetics(self) -> list:
        return list()

    def save_to_file(self):
        with open(self.filename, 'w') as f:
            json.dump(
                obj={
                    'name': self.name,
                    'filename': self.filename,
                    'emp_max': self.emp_max,
                    'emp_current': self.emp_current,
                    'emp_mod': self.emp_mod,
                    'hp_mod': self.hp_mod,
                    'cybernetics': self.export_cybernetics()
                },
                fp=f,
                indent=2,
                ensure_ascii=False
            )

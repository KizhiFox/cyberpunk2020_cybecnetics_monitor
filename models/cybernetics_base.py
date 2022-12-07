from dataclasses import dataclass, field
from enum import Enum


class Operations(Enum):
    N = 'Незначительная'
    M = 'Малая'
    MA = 'Значительная'
    CR = 'Сложная'


class Types(Enum):
    BASE = 'Базовый'
    FASHIONWARE = 'Биомода'
    NEURALWARE = 'Неуротехника'
    CHIPWARE = 'Чиптехника'
    IMPLANTS = 'Импланты'
    BIOWARE = 'Биотехника'
    CYBERWEAPONS = 'Кибероружие'
    CYBEROPTIC = 'Кибероптика'
    CYBERAUDIO = 'Кибераудио'
    CYBERLIMB = 'Киберконечность'
    HANDS_AND_FEET = 'Кисти и ступни'
    BUILT_INS = 'Встраиваемые устройства'
    LIMB_CYBERWEAPONS = 'Оружие киберлимб'
    LINEAR_FRAME = 'Внешние рамы'
    BODY_PLATING = 'Покрытие тела'


NEYRALWARE_PROCESSOR = 'M'


@dataclass()
class CyberBase:
    type: Types = Types.BASE
    name = ''
    code: str | None = None  # Unique short code
    description: str | None = None
    installs_in: list | None = None  # List[code] where it must be installs
    requires: list | None = field(default_factory=lambda: [NEYRALWARE_PROCESSOR])  # List[code] of stuff required for installation
    operation: Operations | None = None  # Installation operation difficulty
    has_sockets = False
    sockets: list | None = None  # List[CyberBase]
    max_sockets = 0  # 0 is zero, -1 is infinity
    show_in_status = False  # Separate page at main screen
    stats: str | None = None  # Stats that ere influenced by stic stuff
    avg_price: str | None = None  # 10, 2.5, 0.5-100
    avg_hp: str | None = None  # 1, 0.5, 2d6/3
    prise: float | None = None  # real amount of money that have been spent on installation
    hp: float | None = None  # amount of los humanity points

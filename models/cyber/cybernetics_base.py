import uuid
from dataclasses import dataclass, field
from enum import Enum


class Operations(str, Enum):
    N = 'Незначительная'
    M = 'Малая'
    MA = 'Значительная'
    CR = 'Сложная'


class Types(str, Enum):
    BASE = 'Базовый'
    FASHIONWARE = 'Биомода'
    NEURALWARE = 'Нейротехника'
    CHIPWARE = 'Чиптехника'
    IMPLANTS = 'Импланты'
    BIOWARE = 'Биотехника'
    CYBERWEAPONS = 'Кибероружие'
    CYBEROPTIC = 'Кибероптика'
    CYBERAUDIO = 'Кибераудио'
    CYBERLIMB = 'Киберконечности'
    HANDS_AND_FEET = 'Кисти и ступни'
    BUILT_INS = 'Встраиваемые устройства'
    LIMB_CYBERWEAPONS = 'Оружие киберлимб'
    LINEAR_FRAME = 'Внешние рамы'
    BODY_PLATING = 'Покрытие тела'


@dataclass()
class CyberBase:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))  # unique id of installed implant
    type: Types = Types.BASE
    name: str = ''
    code: str = ''  # unique short code
    description: str | None = None
    installs_in: list | None = None  # list[code] where it must be installs
    requires: list | None = None  # list[code] of stuff required for installation
    operation: Operations | None = None  # installation operation difficulty
    has_sockets: bool = False
    max_sockets: int | None = None  # -1 is infinity
    num_sockets_use: int | None = None  # number of sockets that stuff requires
    is_chip: bool = False
    show_in_status: bool = False  # separate page at main screen
    stats: str | None = None  # stats that ere influenced by this stuff
    avg_price: str | None = None  # 10, 2.5, 0.5-100
    avg_hp: str | None = None  # 1, 0.5, 2d6/3 1d6|2d6/2
    prise: float | None = None  # real amount of money that have been spent on installation
    hp: float | None = None  # amount of los humanity points
    extra: str | None = None  # some extra stuff: description etc
    sockets: list | None = None  # list[CyberBase]

from dataclasses import dataclass

from models.cyber.cybernetics_base import Operations, Types, CyberBase
from models.cyber.cyberlimbs import CyberlimbBase


@dataclass()
class HandFeetBase(CyberBase):
    type = Types.HANDS_AND_FEET
    installs_in = [CyberlimbBase.code]
    requires = [CyberlimbBase.code]
    operation = Operations.N
    has_sockets = False
    num_sockets_use = 1


@dataclass()
class StandardHand(HandFeetBase):
    name = 'Standard Hand'
    code = 'STD'
    description = 'Нормальная кисть'
    avg_price = '160'
    avg_hp = '0'


@dataclass()
class RipperHand(HandFeetBase):
    name = 'Ripper Hand'
    code = 'RPH'
    description = 'Стандартная кисть со встроенными ripperами'
    stats = 'Оружие в теле (руки) 1D6+3 повр. (AP = нож)'
    avg_price = '600'
    avg_hp = '2d6'


@dataclass()
class HammerHand(HandFeetBase):
    name = 'HAM'
    code = 'Кулак наносит 1D10 повреждений'
    description = 'Кулак наносит 1D10 повреждений'
    avg_price = '600'
    avg_hp = '2d6'


@dataclass()
class BuzzerHand(HandFeetBase):
    name = 'Buzzer Hand'
    code = 'BUZ'
    description = 'Нитецеркулярная пила. 2D6+2. Режет мягкую броню'
    stats = '2D6+2 повр. Режет мягкую броню'
    avg_price = '600'
    avg_hp = '2d6'


@dataclass()
class ToolHand(HandFeetBase):
    name = 'Tool Hand'
    code = 'TOL'
    description = 'Инструменты в пальцах'
    avg_price = '600'
    avg_hp = '2'


@dataclass()
class GrappleHand(HandFeetBase):
    name = 'Grapple Hand'
    code = 'GRP'
    description = 'Забрасываемая кошка в кисти, 100 метров'
    avg_price = '350'
    avg_hp = '3'


@dataclass()
class ExtensionHand(HandFeetBase):
    name = 'Extension Hand'
    code = 'EXT'
    description = 'Выдвигается на 1 m'
    avg_price = '350'
    avg_hp = '2'


@dataclass()
class SpikeHand(HandFeetBase):
    name = 'Spike Hand'
    code = 'SPK'
    description = 'Острые коготки 1D6+3 AP повреждений'
    stats = 'Острые коготки 1D6+3 AP повреждений'
    avg_price = '500'
    avg_hp = '2d6'


@dataclass()
class ModularHand(HandFeetBase):
    name = 'Modular Hand'
    code = 'MOD'
    description = 'Любые 4 инструмента'
    avg_price = '600'
    avg_hp = '2'


@dataclass()
class StandardFoot(HandFeetBase):
    name = 'Standard Foot'
    code = 'STDF'
    description = 'Нормальная ступня'
    avg_price = '200'
    avg_hp = '0'


@dataclass()
class TalonFoot(HandFeetBase):
    name = 'Talon Foot'
    code = 'TAL'
    description = 'На ногтях лезвия 1D6 повреждений (AP как нож)'
    stats = 'На ногтях лезвия 1D6 повреждений (AP как нож)'
    avg_price = '600'
    avg_hp = '2d6'


@dataclass()
class ToolFoot(HandFeetBase):
    name = 'Tool Foot'
    code = 'TOLF'
    description = 'Инструменты'
    avg_price = '300'
    avg_hp = '2'


@dataclass()
class WebFoot(HandFeetBase):
    name = 'Web Foot'
    code = 'WEB'
    description = 'Удваивает скорость плавания, +3 к Swim'
    stats = 'Удваивает скорость плавания, +3 к Swim'
    avg_price = '500'
    avg_hp = '2'


@dataclass()
class GripFoot(HandFeetBase):
    name = 'Grip Foot'
    code = 'GRPF'
    description = 'Разработана для скалолазания, +2 к Climb'
    stats = '+2 к Climb'
    avg_price = '500'
    avg_hp = '2'


@dataclass()
class SpikeHeelFoot(HandFeetBase):
    name = 'Spike Heel Foot'
    code = 'SPKF'
    description = 'Шпора. Пинки назад 2D6 AP повреждений'
    stats = 'Шпора. Пинки назад 2D6 AP повреждений'
    avg_price = '500'
    avg_hp = '2d6'

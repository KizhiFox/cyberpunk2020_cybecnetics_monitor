from dataclasses import dataclass

from models.cyber.cybernetics_base import Operations, Types, CyberBase
from models.cyber.body_plating import FrontOpticMount


@dataclass()
class Cyberoptic(CyberBase):
    name = 'Cyberoptic'
    code = '_Cyberoptic'
    description = 'Базовый глазной модуль (до 4 опций в глазу)'
    type: Types = Types.CYBEROPTIC
    operation = Operations.MA
    has_sockets = True
    sockets = []
    max_sockets = 4
    avg_price = '500'
    avg_hp = '2d6'


@dataclass()
class CyberopticBase(CyberBase):
    operation = Operations.N
    requires = [Cyberoptic.code, FrontOpticMount]
    installs_in = [Cyberoptic.code, FrontOpticMount]
    num_sockets_use = 1


@dataclass()
class ColorShift(CyberopticBase):
    name = 'Color Shift'
    code = 'CF'
    description = 'Позволяет менять цвет, модные эффекты'
    avg_price = '300'
    avg_hp = '0.5'


@dataclass()
class ImageEnhancement(CyberopticBase):
    name = 'Image Enhancement'
    code = 'IE'
    description = '+2 Awareness при визуальном осмотре'
    stats = '+2 Awareness при визуальном осмотре'
    avg_price = '300'
    avg_hp = '1'


@dataclass()
class TargetingScope(CyberopticBase):
    name = 'Targeting Scope'
    code = 'TA'
    description = '+1 на все атаки из смартгана'
    stats = '+1 на все атаки из смартгана'
    avg_price = '400'
    avg_hp = '2'


@dataclass()
class TimesSquareMarquee(CyberopticBase):
    name = 'Times Square Marquee'
    code = 'TS'
    description = 'Жидкокристаллический дисплей для сообщений'
    avg_price = '300'
    avg_hp = '1'


@dataclass()
class Teleoptics(CyberopticBase):
    name = 'Teleoptics'
    code = 'TE'
    description = 'Увеличение макс. в 20 раз'
    avg_price = '150'
    avg_hp = '0.5'


@dataclass()
class MicroOptics(CyberopticBase):
    name = 'Micro-optics'
    code = 'ME'
    description = 'Микроскоп'
    avg_price = '150'
    avg_hp = '0.5'


@dataclass()
class AntiDazzle(CyberopticBase):
    name = 'Anti Dazzle'
    code = 'AD'
    description = 'Иммунитет в ослеплению ярким сетом и лазером'
    avg_price = '200'
    avg_hp = '0.5'


@dataclass()
class LowLite(CyberopticBase):
    name = 'Low Lite™'
    code = 'LL'
    description = 'Видишь в сумерках'
    avg_price = '200'
    avg_hp = '0.5'


@dataclass()
class ThermographSensor(CyberopticBase):
    name = 'Thermograph sensor'
    code = 'TH'
    description = 'Видишь теплые поверхности, термозрение'
    avg_price = '200'
    avg_hp = '1'


@dataclass()
class Infrared(CyberopticBase):
    name = 'Infrared'
    code = 'IR'
    description = 'Видишь в полной темноте используя теплоэмиссию'
    avg_price = '200'
    avg_hp = '1'


@dataclass()
class UltraViolet(CyberopticBase):
    name = 'Ultra Violet'
    code = 'UV'
    description = 'Видишь в полной темноте используя УФ подсветку'
    avg_price = '200'
    avg_hp = '1'


@dataclass()
class MicroVideoOptic(CyberopticBase):
    name = 'MicroVideo Optic'
    code = 'MV'
    description = 'Видео камера до 20 мин (занимает 2 опции)'
    num_sockets_use = 2
    avg_price = '300'
    avg_hp = '0.5'


@dataclass()
class DigitalCamera(CyberopticBase):
    name = 'Digital Camera'
    code = 'DC'
    description = 'Цифровой фотоаппарат, 20фото (занимает 2 опции)'
    num_sockets_use = 2
    avg_price = '300'
    avg_hp = '0.5'


@dataclass()
class Dartgun(CyberopticBase):
    name = 'Dartgun'
    code = 'DE'
    description = 'Ядовитое оружие (занимает 3 опции) несет 1 дротик'
    avg_price = '200'
    avg_hp = '2'

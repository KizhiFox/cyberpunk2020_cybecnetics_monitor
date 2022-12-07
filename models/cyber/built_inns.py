from dataclasses import dataclass

from models.cyber.cybernetics_base import Operations, Types, CyberBase
from models.cyber.cyberlimbs import CyberlimbBase


@dataclass()
class BuildInBase(CyberBase):
    type = Types.BUILT_INS
    installs_in = [CyberlimbBase.code]
    requires = [CyberlimbBase.code]
    operation = Operations.N
    has_sockets = False
    num_sockets_use = 1


@dataclass()
class AVTapeRecorder(BuildInBase):
    name = 'AV Tape Recorder'
    code = 'AVR2'
    description = 'Пишет видео и аудио на кассеты'
    avg_price = '250'
    avg_hp = '1'


@dataclass()
class Cybermodem(BuildInBase):
    name = 'Cybermodem'
    code = 'CMD'
    description = 'Встроенная "кибердека" 5.000 за сотовую версию'
    avg_price = '3000|5000'
    avg_hp = '1'


@dataclass()
class DigitalRecorder(BuildInBase):
    name = 'Digital Recorder'
    code = 'DGRC'
    description = 'Записывает цифровые данные на встроенный чип'
    avg_price = '300'
    avg_hp = '1'


@dataclass()
class StorageSpace(BuildInBase):
    name = 'Storage Space'
    code = 'STR'
    description = '2"x6" свободного места. Можно закрыть на замок'
    avg_price = '50'
    avg_hp = '5'


@dataclass()
class MiniCam(BuildInBase):
    name = 'MiniCam'
    code = 'CAM'
    description = 'Выезжающий фотоаппарат (20 снимков)'
    avg_price = '200'
    avg_hp = '2'


@dataclass()
class MiniVid(BuildInBase):
    name = 'MiniVid'
    code = 'MVID'
    description = 'Выезжающая видеокамера (30 минут)'
    avg_price = '400'
    avg_hp = '2'


@dataclass()
class HiddenHolster(BuildInBase):
    name = 'Hidden Holster'
    code = 'HOL'
    description = 'Место для хранение оружия'
    avg_price = '100'
    avg_hp = '1'


@dataclass()
class LCDScreenReadout(BuildInBase):
    name = 'LCD Screen Readout'
    code = 'LCD'
    description = 'Минимонитор, можно вывести на внешний экран'
    avg_price = '200'
    avg_hp = '1'


@dataclass()
class Techscanner(BuildInBase):
    name = 'Techscanner'
    code = 'TKSN'
    description = 'Техсканер'
    avg_price = '400'
    avg_hp = '3'

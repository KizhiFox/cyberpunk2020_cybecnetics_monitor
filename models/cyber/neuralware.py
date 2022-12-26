from dataclasses import dataclass

from models.cyber.cybernetics_base import Operations, Types, CyberBase


@dataclass()
class NeyralwareProcessor(CyberBase):
    name = 'Neyralware Processor'
    code = 'M'
    description = 'Базовый процессор, требуется для всех систем'
    type = Types.NEURALWARE
    operation = Operations.M
    has_sockets = True
    sockets = []
    max_sockets = -1
    avg_price = '1000'
    avg_hp = '1d6'


@dataclass()
class NeyralwareBase(CyberBase):
    type = Types.NEURALWARE
    operation = Operations.N
    requires = [NeyralwareProcessor.code]
    installs_in = [NeyralwareProcessor.code]


@dataclass()
class KerenzikovBoosterware(NeyralwareBase):
    name = 'Kerenzikov Boosterware'
    code = 'RFB'
    description = '+1 к инициативе за уровень до +2'
    stats = '+1 к инициативе за уровень до +2'
    avg_price = '500'
    avg_hp = '1d6|2d6'


@dataclass()
class SpeedwareSandevistan(NeyralwareBase):
    name = 'Speedware (Sandevistan)'
    code = 'SW'
    description = '+3 к инициативе на 5 раундов'
    stats = '+3 к инициативе на 5 раундов'
    avg_price = '1600'
    avg_hp = '1d6/2'


@dataclass()
class TactileBoost(NeyralwareBase):
    name = 'Tactile Boost'
    code = 'TB'
    description = '+2 к тактильным ощущениям'
    stats = '+2 к тактильным ощущениям'
    avg_price = '100'
    avg_hp = '2'


@dataclass()
class OlfactoryBoost(NeyralwareBase):
    name = 'Olfactory Boost'
    code = 'OLF'
    description = '+2 к обонятельным ощущениям'
    stats = '+2 к обонятельным ощущениям'
    avg_price = '100'
    avg_hp = '2'


@dataclass()
class PainEditor(NeyralwareBase):
    name = 'Pain Editor'
    code = 'TE'
    description = 'Отключает боль, чувство холода и жары'
    avg_price = '200'
    avg_hp = '2d6'


@dataclass()
class CybermodenLink(NeyralwareBase):
    name = 'Cybermoden Link'
    code = 'PE'
    description = 'Прямое соединение с кибермодемом'
    avg_price = '100'
    avg_hp = '1'


@dataclass()
class VehicleLink(NeyralwareBase):
    name = 'Vehicle Link'
    code = 'VLNK'
    description = 'Прямое подключение с транспортным средствам'
    avg_price = '100'
    avg_hp = '3'


@dataclass()
class SmartgunLink(NeyralwareBase):
    name = 'Smartgun Link'
    code = 'WLNK'
    description = 'Работа со смартганами'
    avg_price = '100'
    avg_hp = '2'


@dataclass()
class MachineTechLink(NeyralwareBase):
    name = 'Machine/Tech Link'
    code = 'MLNK'
    description = 'Прямое подключение к тяжелой технике'
    avg_price = '100'
    avg_hp = '2'


@dataclass()
class DataTermLink(NeyralwareBase):
    name = 'DataTerm Link'
    code = 'DLNK'
    description = 'Закачка данных с ДатаТерма в память'
    avg_price = '100'
    avg_hp = '2'


@dataclass()
class InterfacePlugs(NeyralwareBase):
    name = 'Interface plugs'
    code = 'PLG'
    description = 'Разъем для подключения и чипов (пара)'
    avg_price = '200'
    avg_hp = '1d6'
    operation = Operations.M
    has_sockets = True
    sockets = []
    max_sockets = 2

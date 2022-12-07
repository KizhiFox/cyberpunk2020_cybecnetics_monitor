from dataclasses import dataclass

from models.cyber.cybernetics_base import Operations, Types, CyberBase


@dataclass()
class Cowl(CyberBase):
    type = Types.BODY_PLATING
    name = 'Cowl'
    code = 'SKUL'
    description = 'Черепное покрытие, SP 25'
    stats = 'Черепное покрытие, SP 25'
    avg_price = '200'
    avg_hp = '1d6'
    operation = Operations.MA


@dataclass()
class Faceplate(CyberBase):
    type = Types.BODY_PLATING
    name = 'Faceplate'
    code = 'FACE'
    description = 'Защитная маска SP 25'
    stats = 'Защитная маска SP 25'
    avg_price = '400'
    avg_hp = '4d6'
    operation = Operations.CR


@dataclass()
class TorsoPlate(CyberBase):
    type = Types.BODY_PLATING
    name = 'Torso Plate'
    code = 'TORS'
    description = 'На грудь (торс) SP 25'
    stats = 'На грудь (торс) SP 25'
    avg_price = '2000'
    avg_hp = '3d6'
    operation = Operations.MA


@dataclass()
class FrontOpticMount(CyberBase):
    type = Types.BODY_PLATING
    name = 'Front Optic Mount'
    code = 'FOM'
    description = 'До 5 опций на лице'
    stats = '-1 ATTR'
    avg_price = '1000'
    avg_hp = '4d6'
    operation = Operations.MA
    has_sockets = True
    sockets = []
    max_sockets = 4


@dataclass()
class SenseExtRabbitEars(CyberBase):
    type = Types.BODY_PLATING
    name = 'Sense ext. ("Rabbit Ears")'
    code = 'RABB'
    description = 'Дополнительное наголовье для оптики и аудио'
    avg_price = '500'
    avg_hp = '3d6'
    operation = Operations.M

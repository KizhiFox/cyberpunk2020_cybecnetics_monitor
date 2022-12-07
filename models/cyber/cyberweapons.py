from dataclasses import dataclass

from models.cyber.cybernetics_base import Operations, Types, CyberBase
from models.cyber.cyberlimbs import CyberlimbBase


@dataclass()
class CyberweaponsBase(CyberBase):
    type: Types = Types.CYBERWEAPONS
    operation = Operations.M
    installs_in = [None, CyberlimbBase.code]
    num_sockets_use = 1


@dataclass()
class Scratchers(CyberweaponsBase):
    name = 'Scratchers'
    code = 'SCR'
    description = 'Оружие в теле (руки) 1D6/2 повр.'
    stats = 'Оружие в теле (руки) 1D6/2 повр.'
    avg_price = '100'
    avg_hp = '2d6'
    operation = Operations.N


@dataclass()
class ImplantedFangsVampires(CyberweaponsBase):
    name = 'Implanted Fangs (Vampires)'
    code = 'VAM'
    description = 'Оружие в теле (рот) 1D6/3 повр.'
    stats = 'Оружие в теле (рот) 1D6/3 повр.'
    avg_price = '200'
    avg_hp = '3d6'
    installs_in = None
    num_sockets_use = None


@dataclass()
class Rippers(CyberweaponsBase):
    name = 'Rippers'
    code = 'RIP'
    description = 'Оружие в теле (руки) 1D6+3 повр. (AP = нож)'
    stats = 'Оружие в теле (руки) 1D6+3 повр. (AP = нож)'
    avg_price = '400'
    avg_hp = '3d6'


@dataclass()
class Wolvers(CyberweaponsBase):
    name = 'Wolvers'
    code = 'WLV'
    description = 'Оружие в теле (руки) 3D6 повр. (AP =нож)'
    stats = 'Оружие в теле (руки) 3D6 повр. (AP =нож)'
    avg_price = '600'
    avg_hp = '3d6+1'


@dataclass()
class BigKnucks(CyberweaponsBase):
    name = 'Big Knucks'
    code = 'BGN'
    description = 'Оружие в теле (руки) 1D6+2 повр.'
    stats = 'Оружие в теле (руки) 1D6+2 повр.'
    avg_price = '500'
    avg_hp = '3d6'


@dataclass()
class SliceNDice(CyberweaponsBase):
    name = 'Slice N’Dice'
    code = 'SND'
    description = 'Оружие в теле (руки) 2D6 повр.'
    stats = 'Оружие в теле (руки) 2D6 повр.'
    avg_price = '700'
    avg_hp = '3d6'


@dataclass()
class Cybersnake(CyberweaponsBase):
    name = 'Cybersnake'
    code = 'CSN'
    description = 'Киберорудие самоконтролируемое 1D6 повр.'
    stats = 'Киберорудие самоконтролируемое 1D6 повр.'
    avg_price = '1200'
    avg_hp = '4d6'

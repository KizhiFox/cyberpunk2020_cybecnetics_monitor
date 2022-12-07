from dataclasses import dataclass

from models.cyber.cybernetics_base import Operations, Types, CyberBase
from models.cyber.cyberlimbs import CyberlimbBase


@dataclass()
class LimbWeaponBase(CyberBase):
    type = Types.LIMB_CYBERWEAPONS
    installs_in = [CyberlimbBase.code]
    requires = [CyberlimbBase.code]
    operation = Operations.N
    has_sockets = False
    num_sockets_use = 1
    avg_hp = '2d6'


@dataclass()
class GrenadeLauncher(LimbWeaponBase):
    name = 'Grenade Launcher'
    code = 'GLN'
    description = '1 граната любого типа'
    avg_price = '500'


@dataclass()
class MicroMissileLauncher(LimbWeaponBase):
    name = 'MicroMissileLauncher'
    code = 'MML'
    description = '4 микроракеты, каждая наносит 4D6 повреждений'
    stats = '4 микроракеты, каждая наносит 4D6 повреждений'
    avg_price = '900'


@dataclass()
class PopupGun(LimbWeaponBase):
    name = 'Popup Gun'
    code = 'PUG'
    description = 'Выезжающее оружие'
    avg_price = '2-800'


@dataclass()
class FlameThrower(LimbWeaponBase):
    name = 'Flame Thrower'
    code = 'FTH'
    description = '2D6 поврежд. в 1ый раунд, 1D6/2 в следующие два'
    stats = '2D6 поврежд. в 1ый раунд, 1D6/2 в следующие два'
    avg_price = '600'


@dataclass()
class WeaponMountLink(LimbWeaponBase):
    name = 'Weapon Mount & Link'
    code = 'WML'
    description = 'Вмонтированное крепление с линоком под 1 оружие'
    avg_price = '100'
    avg_hp = '3'


@dataclass()
class TwoShotCapacitorLaser(LimbWeaponBase):
    name = '2 shot Capacitor Laser'
    code = 'LSR'
    description = 'На предплечье. Лазер, малый 3D6 повреждений'
    stats = 'На предплечье. Лазер, малый 3D6 повреждений'
    avg_price = '800'

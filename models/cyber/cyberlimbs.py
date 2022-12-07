from dataclasses import dataclass

from models.cyber.cybernetics_base import Operations, Types, CyberBase


@dataclass()
class ArtificialShoulderMount(CyberBase):
    name = 'Artificial Shoulder Mount'
    code = 'ASHO'
    description = 'Позволяет вешать еще 2 руки (не больше одной)'
    stats = 'SDP = 25'
    has_sockets = True
    sockets = []
    max_sockets = 2
    operation = Operations.CR
    avg_price = '1500'
    avg_hp = '2d6'


@dataclass()
class CyberlimbBase(CyberBase):
    code = 'CR'
    type = Types.CYBERLIMB
    operation = Operations.CR
    has_sockets = True
    sockets = []
    installs_in = [None, ArtificialShoulderMount.code]
    num_sockets_use = 1
    avg_price = '200'
    avg_hp = '2d6'


@dataclass()
class Cyberarm(CyberlimbBase):
    name = 'Cyberarm'
    stats = 'SDP конечности = 20, сдавливание 2d6, удар 1d6'
    description = 'Стандартная киберука (4 опции)'
    max_sockets = 4
    avg_price = '3000'


@dataclass()
class Cyberleg(CyberlimbBase):
    name = 'Cyberleg'
    description = 'Стандартная кибернога (3 опции)'
    stats = 'SDP конечности = 20, сдавливание 2d6, пинок 2d6, прыжок 6/8м.'
    max_sockets = 3
    avg_price = '2000'


@dataclass()
class LimbAttachmentBase(CyberBase):
    operation = Operations.N
    requires = [CyberlimbBase.code]
    installs_in = [CyberlimbBase.code]
    num_sockets_use = 1


@dataclass()
class QuickChangeMount(LimbAttachmentBase):
    name = 'Quick change Mount'
    code = 'QC'
    description = 'Смена киберконечности за 1 ход'
    avg_price = '200'
    avg_hp = '2'


@dataclass()
class HydraulicRams(LimbAttachmentBase):
    name = 'Hydraulic Rams'
    code = 'HRAM'
    description = 'SDP конечности = 30, 3x повреждения'
    stats = 'SDP конечности = 30, 3x повреждения'
    avg_price = '200'
    avg_hp = '3'


@dataclass()
class ThikenedMyomar(LimbAttachmentBase):
    name = 'Thikened Myomar'
    code = 'THK'
    description = 'SDP конечности +5, 2x поврежд. +50% прыжки'
    stats = 'SDP конечности +5, 2x поврежд. +50% прыжки'
    avg_price = '250'
    avg_hp = '2'


@dataclass()
class ReinforcedJoints(LimbAttachmentBase):
    name = 'Reinforced Joints'
    code = 'RJ'
    description = 'SDP конечности +5'
    stats = 'SDP конечности +5'
    avg_price = '200'
    avg_hp = '1'


@dataclass()
class MicrowaveEMPShielding(LimbAttachmentBase):
    name = 'Microwave/EMP Shielding'
    code = 'MSR'
    description = 'Конечность неподвержена микроволновому излуч.'
    avg_price = '300'
    avg_hp = '1'


@dataclass()
class PlasticCovering(LimbAttachmentBase):
    name = 'Plastic Covering'
    code = 'PSTK'
    description = 'Цветное или прозрачное покрытие'
    avg_price = '1-200'
    avg_hp = '1'


@dataclass()
class RealSkinn(LimbAttachmentBase):
    name = 'RealSkinn™'
    code = 'REAL'
    description = 'Выглядит как настоящая (сложность заметить 20).'
    stats = 'Понижает HP на 1D6/2'
    avg_price = '200'


@dataclass()
class SuperChrome(LimbAttachmentBase):
    name = 'SuperChrome®'
    code = 'SUPR'
    description = 'Металопокрытие'
    avg_price = '200'
    avg_hp = '3'


@dataclass()
class Kevlar(LimbAttachmentBase):
    name = 'Kevlar'
    code = 'ARM'
    description = 'SP конечности = 20'
    stats = 'SP конечности = 20'
    avg_price = '200'
    avg_hp = '1d6'

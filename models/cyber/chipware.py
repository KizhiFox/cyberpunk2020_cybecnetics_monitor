from dataclasses import dataclass

from models.cyber.cybernetics_base import Operations, Types, CyberBase
from models.cyber.neuralware import NeyralwareProcessor, InterfacePlugs


@dataclass()
class ChipwareSocket(CyberBase):
    type = Types.CHIPWARE
    name = 'Chipware Socket'
    code = '_ChipwareSocket'
    description = 'Держит до 10 чипов'
    installs_in = None
    requires = [NeyralwareProcessor.code]
    operation = Operations.N
    has_sockets = True
    sockets = []
    max_sockets = 10
    avg_price = '200'
    avg_hp = '1d6/2'


@dataclass()
class ReflexChip(CyberBase):
    type = Types.CHIPWARE
    name = 'Reflex Chip'
    code = 'APTR'
    avg_hp = '0'
    is_chip = True
    installs_in = [ChipwareSocket.code, InterfacePlugs.code]
    requires = [ChipwareSocket.code, InterfacePlugs.code]


@dataclass()
class MemoryChip(CyberBase):
    type = Types.CHIPWARE
    name = 'Memory Chip'
    code = 'MRAM'
    avg_hp = '0'
    is_chip = True
    installs_in = [ChipwareSocket.code, InterfacePlugs.code]
    requires = [ChipwareSocket.code, InterfacePlugs.code]

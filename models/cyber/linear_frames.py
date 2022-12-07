from dataclasses import dataclass

from models.cyber.cybernetics_base import Operations, Types, CyberBase


@dataclass()
class FrameSigma(CyberBase):
    type = Types.LINEAR_FRAME
    name = 'Frame Sigma'
    code = 'SIGMA'
    description = 'Сила = 12'
    operation = Operations.MA
    stats = 'Сила = 12'
    avg_price = '6000'
    avg_hp = '2d6'


@dataclass()
class FrameBeta(CyberBase):
    type = Types.LINEAR_FRAME
    name = 'Frame Beta'
    code = 'BETA'
    description = 'Сила = 14'
    operation = Operations.MA
    stats = 'Сила = 14'
    avg_price = '8000'
    avg_hp = '2d6'


@dataclass()
class FrameOmega(CyberBase):
    type = Types.LINEAR_FRAME
    name = 'Frame Omega'
    code = 'OMEGA'
    description = 'Сила = 16'
    operation = Operations.MA
    stats = 'Сила = 16'
    avg_price = '10000'
    avg_hp = '3d6'

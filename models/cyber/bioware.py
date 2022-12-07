from dataclasses import dataclass

from models.cyber.cybernetics_base import Operations, Types, CyberBase


@dataclass()
class BiowareBase(CyberBase):
    type: Types = Types.BIOWARE
    operation = Operations.N


@dataclass()
class GraftedMuscle(BiowareBase):
    name = 'Grafted Muscle'
    code = 'GR'
    description = 'Увеличивает BODY до +2'
    stats = 'Увеличивает BODY до +2'
    avg_price = '1000|2000'
    avg_hp = '2d6'
    operation = Operations.MA


@dataclass()
class MuscleAndBoneLace(BiowareBase):
    name = 'Muscle and Bone Lace'
    code = 'MBL'
    description = 'Увеличивает BODY на 2'
    stats = 'Увеличивает BODY на 2'
    avg_price = '1500'
    avg_hp = '1d6/2'


@dataclass()
class SkinWeave(BiowareBase):
    name = 'Skin Weave'
    code = 'SKW'
    description = 'Броня на все тело 12 SP'
    stats = 'Броня на все тело 12 SP'
    avg_price = '2000'
    avg_hp = '2d6'


@dataclass()
class EnhancedAntibodies(BiowareBase):
    name = 'Enhanced Antibodies'
    code = 'EA'
    description = 'Лечение быстрей на +1 пункт в день'
    stats = 'Лечение быстрей на +1 пункт в день'
    avg_price = '3000'
    avg_hp = '1d6/2'


@dataclass()
class ToxinBinders(BiowareBase):
    name = 'Toxin Binders'
    code = 'TBN'
    description = 'Спасбросок от ядов и наркотиков с +4'
    stats = 'Спасбросок от ядов и наркотиков с +4'
    avg_price = '3000'
    avg_hp = '1d6/2'


@dataclass()
class Nanosurgeons(BiowareBase):
    name = 'Nanosurgeons'
    code = 'NSR'
    description = 'Удваивает скорость лечения'
    stats = 'Удваивает скорость лечения'
    avg_price = '6000'
    avg_hp = '1d6/2'

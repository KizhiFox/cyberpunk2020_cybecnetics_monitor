from dataclasses import dataclass, field

from models.cybernetics_base import Operations, Types, NEYRALWARE_PROCESSOR, CyberBase


@dataclass()
class FashionwareBase(CyberBase):
    type = Types.FASHIONWARE
    operation = Operations.N
    requires = None


@dataclass()
class Biomonitor(FashionwareBase):
    name = 'Biomonitor'
    code = 'BIO'
    description = '+2 к сопротивлению наркотикам'
    stats = '+2 к сопротивлению наркотикам'
    avg_price = '100'
    avg_hp = '1'

@dataclass()
class Skinwatch(FashionwareBase):
    name = 'Skinwatch'
    code = 'SWTC'
    description = 'Подкожные часы'
    avg_price = '50'
    avg_hp = '1'


@dataclass()
class LightTattoo(FashionwareBase):
    name = 'Light Tattoo'
    code = 'LT'
    description = 'Декоративная татуировка'
    avg_price = '1-20'
    avg_hp = '0.5'


@dataclass()
class ShiftTacts(FashionwareBase):
    name = 'Shift-tacts'
    code = 'SHF'
    description = 'Меняющие цвет контактные линзы'
    avg_price = '1-200'
    avg_hp = '0.5'


@dataclass()
class ChemSkins(FashionwareBase):
    name = 'ChemSkins'
    code = 'CSK'
    description = 'Краска меняющая цвет кожи'
    avg_price = '200'
    avg_hp = '1d6/2'


@dataclass()
class Synthskins(FashionwareBase):
    name = 'Synthskins'
    code = 'SYN'
    description = 'Меняющая цвет искусственная кожа'
    avg_price = '400'
    avg_hp = '1d6'


@dataclass()
class Techhair(FashionwareBase):
    name = 'Techhair'
    code = 'TEH'
    operation = Operations.M
    description = 'Волосы меняющие цвет и оттенок'
    avg_price = '1-200'
    avg_hp = '2'

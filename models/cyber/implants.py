from dataclasses import dataclass

from models.cyber.cybernetics_base import Operations, Types, CyberBase
from models.cyber.cyberoptic import Cyberoptic


@dataclass()
class ImplantBase(CyberBase):
    type: Types = Types.IMPLANTS
    operation = Operations.M


@dataclass()
class NasalFilters(ImplantBase):
    name = 'Nasal Filters'
    code = 'NF'
    description = 'Фильтрует токсичные газы, 70% эффективность'
    avg_price = '60'
    avg_hp = '2'


@dataclass()
class Gill(ImplantBase):
    name = 'Gill'
    code = 'GA'
    description = 'Система дыхания водой, 4 часа'
    avg_price = '400'
    avg_hp = '3d6'
    operation = Operations.MA


@dataclass()
class IndependentAirSupply(ImplantBase):
    name = 'Independent Air Supply'
    code = 'IA'
    description = '25 минут дыхания'
    avg_price = '300'
    avg_hp = '2d6'
    operation = Operations.MA


@dataclass()
class MrStuddSexualImplant(ImplantBase):
    name = 'Mr. Studd™ Sexual Implant'
    code = 'MS'
    description = 'Всю ночь. Каждую ночь. И она никогда не узнает'
    avg_price = '300'
    avg_hp = '2d6'
    operation = Operations.MA


@dataclass()
class ContraceptiveImplant(ImplantBase):
    name = 'Contraceptive Implant'
    code = 'CI'
    description = 'Контоцепт на 5 лет. 98% эффективность'
    avg_price = '100'
    avg_hp = '0.5'


@dataclass()
class SubdermalPocket(ImplantBase):
    name = 'Subdermal Pocket'
    code = 'PKT'
    description = '2"x4" карман накрытый Realskinn™'
    avg_price = '200'
    avg_hp = '2d6'


@dataclass()
class AdrenalineBooster(ImplantBase):
    name = 'Adrenaline Booster'
    code = 'ADB'
    description = 'Ускоряет REF +1 на 1D6+2 раундов, три раза в день'
    stats = 'Ускоряет REF +1 на 1D6+2 раундов, три раза в день'
    avg_price = '400'
    avg_hp = '2d6'


@dataclass()
class SubdermalArmor(ImplantBase):
    name = 'Subdermal Armor'
    code = 'SDA'
    description = 'Броня на торсе SP 18'
    stats = 'Броня на торсе SP 18'
    avg_price = '1200'
    avg_hp = '2d6'
    operation = Operations.CR


@dataclass()
class MotionDetector(ImplantBase):
    name = 'Motion Detector'
    code = 'MD'
    description = 'Детектор движения 20 м2 70% эффективности'
    avg_price = '200'
    avg_hp = '2d6'


@dataclass()
class DigitalRecorder(ImplantBase):
    name = 'Digital Recorder'
    code = 'DGR'
    description = '2 часа записи с любого цифрового устройства'
    avg_price = '200'
    avg_hp = '2'


@dataclass()
class AudioVideoTapeRecorder(ImplantBase):
    name = 'Audio/Video Tape Recorder'
    code = 'AVR'
    description = '2 часа с аудио / видео линка'
    avg_price = '300'
    avg_hp = '2'


@dataclass()
class RadarSensor(ImplantBase):
    name = 'Radar Sensor'
    code = 'RA'
    description = 'Радар, радиус 100м. Требуется кибероптика, 70% эффективности'
    avg_price = '200'
    avg_hp = '2'
    requires = [Cyberoptic.code]


@dataclass()
class SonarImplant(ImplantBase):
    name = 'Sonar Implant'
    code = 'SN'
    description = '50м сонар. Только в воде, 70% эффективности'
    avg_price = '300'
    avg_hp = '2'


@dataclass()
class RadiationDetector(ImplantBase):
    name = 'Radiation Detector'
    code = 'RAD'
    description = '10м радиус 80% эффективность'
    avg_price = '200'
    avg_hp = '2'


@dataclass()
class ChemicalAnalyser(ImplantBase):
    name = 'Chemical Analyser'
    code = 'CH'
    description = '5м радиус 70% эффективность'
    avg_price = '200'
    avg_hp = '2'


@dataclass()
class VoiceSynthesizer(ImplantBase):
    name = 'Voice Synthesizer'
    code = 'VS'
    description = 'Может подделывать голос (60%). До 10 голосов'
    avg_price = '600'
    avg_hp = '1d10'


@dataclass()
class AudioVox(ImplantBase):
    name = 'AudioVox'
    code = 'LS'
    description = 'Голосовые спецэффекты +2 к Performance'
    stats = 'Голосовые спецэффекты +2 к Performance'
    avg_price = '700'
    avg_hp = '2d6'

from dataclasses import dataclass

from models.cyber.cybernetics_base import Operations, Types, CyberBase


@dataclass()
class Cyberaudio(CyberBase):
    name = 'Cyberaudio'
    code = '_Cyberaudio'
    description = 'Базовый сл. модуль Нет ограничения кол-ва опций'
    type: Types = Types.CYBERAUDIO
    operation = Operations.M
    has_sockets = True
    sockets = []
    max_sockets = -1
    avg_price = '500'
    avg_hp = '2d6'


@dataclass()
class CyberaudioBase(CyberBase):
    operation = Operations.N
    requires = [Cyberaudio.code]
    installs_in = [Cyberaudio.code]
    num_sockets_use = 1


@dataclass()
class AmplifiedHearing(CyberaudioBase):
    name = 'Amplified Hearing'
    code = 'AH'
    description = '+1 Awareness при броске на слух'
    stats = '+1 Awareness при броске на слух'
    avg_price = '200'
    avg_hp = '1'


@dataclass()
class RadioLink(CyberaudioBase):
    name = 'Radio Link'
    code = 'RL'
    description = 'Радио коммуникатор на 1 милю'
    avg_price = '100'
    avg_hp = '1'


@dataclass()
class PhoneSplice(CyberaudioBase):
    name = 'Phone Splice'
    code = 'PS'
    description = 'Сотовый коммуникатор'
    avg_price = '150'
    avg_hp = '1'


@dataclass()
class Scrambler(CyberaudioBase):
    name = 'Scrambler'
    code = 'SC'
    description = 'Нельзя подслушать без декриптора'
    avg_price = '100'
    avg_hp = '0.5'


@dataclass()
class BugDetector(CyberaudioBase):
    name = 'Bug Detector'
    code = 'BD'
    description = 'Определяет наличие жучков. 3 м. 60%'
    avg_price = '200'
    avg_hp = '0.5'


@dataclass()
class VoiceStressAnalyser(CyberaudioBase):
    name = 'Voice Stress Analyser'
    code = 'VSA'
    description = 'Детектор лжи +2 к Human Perception и Interrogation'
    stats = '+2 к Human Perception и Interrogation'
    avg_price = '200'
    avg_hp = '1'


@dataclass()
class SoundEditing(CyberaudioBase):
    name = 'Sound Editing'
    code = 'SE'
    description = 'Фильтрация шумов +2 Awareness на слух'
    stats = '+2 Awareness на слух'
    avg_price = '150'
    avg_hp = '0.5'


@dataclass()
class EnhancedHearingRange(CyberaudioBase):
    name = 'Enhanced Hearing Range'
    code = 'EH'
    description = 'Слышишь в сверхзуковом и дозвуковом диапозонах'
    avg_price = '150'
    avg_hp = '2'


@dataclass()
class WearMan(CyberaudioBase):
    name = 'WearMan™'
    code = 'WM'
    description = 'Встроенный плеер'
    avg_price = '100'
    avg_hp = '0.5'


@dataclass()
class RadarDetector(CyberaudioBase):
    name = 'Radar Detector'
    code = 'RD'
    description = 'Пикает при встрече луча радара (40%)'
    avg_price = '150'
    avg_hp = '0.5'


@dataclass()
class HomingTracer(CyberaudioBase):
    name = 'Homing Tracer'
    code = 'HT'
    description = 'Преследование по сигналу'
    avg_price = '200'
    avg_hp = '0.5'


@dataclass()
class TightBeamRadioLink(CyberaudioBase):
    name = 'Tight Beam Radio Link'
    code = 'TBR'
    description = 'Радиоканал узким лучом'
    avg_price = '200'
    avg_hp = '1'


@dataclass()
class WideBandRadioScanner(CyberaudioBase):
    name = 'Wide Band Radio Scanner'
    code = 'WB'
    description = 'Принимает передачи на всех волнах, сканер'
    avg_price = '100'
    avg_hp = '2'


@dataclass()
class MicroRecorderLink(CyberaudioBase):
    name = 'Micro-recorder Link'
    code = 'MR'
    description = 'Переходник к встроенному устройству записи'
    avg_price = '100'
    avg_hp = '0.5'


@dataclass()
class DigitalRecordingLink(CyberaudioBase):
    name = 'Digital Recording Link'
    code = 'DR'
    description = 'Переходник в цифровую запись звука'
    avg_price = '100'
    avg_hp = '0.5'


@dataclass()
class LevelDamper(CyberaudioBase):
    name = 'Level Damper'
    code = 'LD'
    description = 'Авто компенсатор шумов'
    avg_price = '300'
    avg_hp = '0.5'

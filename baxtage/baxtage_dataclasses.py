from dataclasses import dataclass
from datetime import datetime, timedelta

from phonenumbers import PhoneNumber


@dataclass
class Organisation:
    pass


@dataclass
class Person:
    name: str
    phone: PhoneNumber
    pass


@dataclass
class Artist(Person):
    instrument: str


@dataclass
class Crew(Person):
    role: str


@dataclass
class Act:
    ...


@dataclass
class TechRider:
    tour_eng: Person
    pass


@dataclass
class HospitalityRider:
    pass


@dataclass
class Rider:
    tech: TechRider
    hospitality: HospitalityRider


@dataclass
class Performance:
    # rank by time... beware midnight!

    # essential attrs
    on_stage_time: datetime
    off_stage_time: datetime
    act: Act

    # optional attrs
    tor_eng: Person = None  # defined in tech rider if there is no tech rider, there is no tour eng
    tech_rider: TechRider = None
    hospitality_rider: HospitalityRider = None
    tech_brief: str = None
    hospitality_brief: str = None
    gig_start_time: datetime = None

    def get_durs(self):
        gig_start_time = self.gig_start_time if self.gig_start_time else self.on_stage_time
        on_stage_time = self.on_stage_time
        off_stage_time = self.off_stage_time
        self.linecheck_dur: timedelta = gig_start_time - on_stage_time if gig_start_time else None
        self.gig_dur: timedelta = off_stage_time - gig_start_time if gig_start_time else off_stage_time - on_stage_time
        self.gig_start_time = gig_start_time if gig_start_time else on_stage_time


@dataclass
class PerformanceDict:
    performances: dict[Performance]




@dataclass
class ActDict:
    acts: dict[Act]


@dataclass
class PersonDict:
    persons = dict[Person]


@dataclass
class ArtistDict:
    artists = dict[Artist]

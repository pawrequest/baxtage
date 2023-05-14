from dataclasses import dataclass
from datetime import datetime, timedelta

from phonenumbers import PhoneNumber


##########################################
@dataclass
class Person:
    name: str
    phone: PhoneNumber
    pass


@dataclass
class Artist(Person):
    instrument: str


@dataclass
class CrewMember(Person):
    role: str


########################################
@dataclass
class Act:
    ...


@dataclass
class ActDict:
    acts: dict[Act]

######################################
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


###############################################

@dataclass
class Performance:
    # rank by time... beware midnight!

    # essential attrs
    on_stage_time: datetime
    off_stage_time: datetime
    act: Act
    linecheck_dur: timedelta = None

    # optional attrs
    tor_eng: Person = None  # defined in tech rider if there is no tech rider, there is no tour eng
    tech_rider: TechRider = None
    hospitality_rider: HospitalityRider = None
    tech_brief: str = None
    hospitality_brief: str = None

    # calculated attrs
    on_stage_dur: timedelta = None
    gig_start_time: datetime = None
    gig_dur: timedelta = None

    def __post_init__(self):
        # get durationss
        self.gig_start_time = self.on_stage_time + self.linecheck_dur if self.linecheck_dur else self.on_stage_time
        self.gig_dur: timedelta = self.off_stage_time - self.gig_start_time



@dataclass
class PerformanceDict:
    performances: dict[Performance]





@dataclass
class PersonDict:
    persons = dict[Person]


@dataclass
class ArtistDict:
    artists = dict[Artist]


""" FUTURE

@dataclass
class Organisation:
    pass

"""

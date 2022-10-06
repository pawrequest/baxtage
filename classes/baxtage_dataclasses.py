from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Any
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
    pass


@dataclass
class Crew(Person):
    role: str

@dataclass
class Act:
    artists: list
    pass

@dataclass
class TechRider:
    tour_eng:Person
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
    linecheck_time: datetime
    start_time: datetime
    finish_time: datetime
    linecheck_duration: timedelta
    on_stage_duration: timedelta
    show_duration: timedelta
    act: Act
    tech: TechRider
    hospitality: HospitalityRider
    tor_eng: Person # defined in tech rider if there is no tech rider, there is no tour eng



@dataclass
class Show:
    performances: list
    pass

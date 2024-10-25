from typing import Literal

from pydantic import BaseModel, constr

MicType = Literal['condenser', 'dynamic']


class Microphone(BaseModel):
    name: constr(max_length=50)
    mic_type: MicType = 'dynamic'
    phantom_power: bool = False

    def __str__(self):
        return self.name


class Instrument(BaseModel):
    default_mic: Microphone = None

    name: constr(max_length=50)
    needs_mic: bool = False
    needs_di: bool = False
    num_channels: int = 1

    def __str__(self):
        return self.name

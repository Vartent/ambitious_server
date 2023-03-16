from datetime import date

from pydantic import BaseModel

from typing import Optional


class ProfileBase(BaseModel):
    name: Optional[str]
    last_name: Optional[str]
    birth_date: Optional[date]
    creation_date: Optional[date]


class Profile(ProfileBase):
    id: int

    class Config:
        orm_mode = True


class ProfileCreate(ProfileBase):
    pass

class ProfileUpdate(ProfileBase):
    pass

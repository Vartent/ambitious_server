from sqlalchemy.orm import Session
from fastapi import (
    Depends,
    HTTPException,
    status
)

from .. import tables
from ..database import get_session

from ..models.profile import ProfileBase, ProfileCreate, ProfileUpdate


class ProfileService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, user_id: int) -> tables.Profile:
        profile = (
            self.session
            .query(
                tables.Profile
            ).filter_by(
                user_parent=user_id
            ).first()
        )
        if not profile:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return profile

    def _get_user(self, user_id: int) -> tables.User:
        user = (
            self.session
            .query(tables.User)
            .filter_by(id=user_id)
            .first()
        )
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='User doesn\'t exist'
            )
        return user

    def get(self, user_id: int) -> tables.Profile:
        return self._get(user_id)

    def create(self, user_id: int, profile_data: ProfileCreate) -> tables.Profile:
        user = self._get_user(user_id)
        profile = tables.Profile(
            user_parent=user_id,
            **profile_data.dict()
        )
        user.profile_child = profile
        self.session.add(profile)
        self.session.commit()
        return profile

    def update(self, user_id: int, profile_data: ProfileUpdate):
        profile = self._get(user_id)
        for field, value in profile_data:
            setattr(profile, field, value)
        self.session.commit()
        return profile

    def delete(self, user_id: int):
        profile = self._get(user_id)
        self.session.delete(profile)
        self.session.commit()
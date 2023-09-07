from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Extra, StrictStr, Field


class ChangePassword(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = Field(None, description='User login')
    token: Optional[UUID] = Field(None, description='Password reset token')
    oldPassword: Optional[StrictStr] = Field(
        None, description='Old password'
    )
    newPassword: Optional[StrictStr] = Field(
        None, description='New password'
    )

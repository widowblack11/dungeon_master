from pydantic import BaseModel, StrictStr, Field


class ChangePasswordModel(BaseModel):
    login: StrictStr
    email: StrictStr
    old_password: StrictStr = Field(alias="oldPassword")
    new_password: StrictStr = Field(alias="newPassword")

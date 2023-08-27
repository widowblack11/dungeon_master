from pydantic import BaseModel, StrictStr


class ChangeEmailModel(BaseModel):
    login: StrictStr
    email: StrictStr
    password: StrictStr

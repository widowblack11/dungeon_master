from pydantic import BaseModel, StrictStr


class ResetPasswordModel(BaseModel):
    login: StrictStr
    email: StrictStr


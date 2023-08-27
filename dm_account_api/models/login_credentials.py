from pydantic import BaseModel, StrictStr, StrictBool


class LoginCredentialsModel(BaseModel):
    login: StrictStr
    email: StrictStr
    rememberMe: StrictBool

# generated by datamodel-codegen:
#   filename:  get_user.json
#   timestamp: 2023-08-26T14:23:50+00:00

from __future__ import annotations

from enum import Enum
from typing import List

from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, Field


class Roles(Enum):
    GUEST = 'Guest'
    PLAYER = 'Player'
    ADMINISTRATOR = 'Administrator'
    NANNY_MODERATOR = 'NannyModerator'
    REGULAR_MODERATOR = 'RegularModerator'
    SENIOR_MODERATOR = 'SeniorModerator'


class Rating(BaseModel):
    enabled: StrictBool
    quality: StrictInt
    quantity: StrictInt


class Info(BaseModel):
    value: StrictStr
    parse_mode: StrictStr = Field(alias="parseMode")


class Paging(BaseModel):
    posts_per_page: StrictInt = Field(alias="postsPerPage")
    comments_per_page: StrictInt = Field(alias="commentsPerPage")
    topics_per_page: StrictInt = Field(alias="topicsPerPage")
    messages_per_page: StrictInt = Field(alias="messagesPerPage")
    entities_per_page: StrictInt = Field(alias="entitiesPerPage")


class Settings(BaseModel):
    color_schema: StrictStr = Field(alias="colorSchema")
    nanny_greetings_message: StrictStr = Field(alias="nannyGreetingsMessage")
    paging: Paging


class Resource(BaseModel):
    login: StrictStr
    roles: List[Roles]
    medium_picture_url: StrictStr = Field(alias="mediumPictureUrl")
    small_picture_url: StrictStr = Field(alias="smallPictureUrl")
    status: StrictStr
    rating: Rating
    online: StrictStr
    name: StrictStr
    location: StrictStr
    registration: StrictStr
    icq: StrictStr
    skype: StrictStr
    original_picture_url: StrictStr = Field(alias="originalPictureUrl")
    info: Info
    settings: Settings


class UserDetailsEnvelope(BaseModel):
    resource: Resource
    metadata: StrictStr

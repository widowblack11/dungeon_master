from datetime import datetime
from enum import Enum
from typing import Optional, Any, List

from pydantic import BaseModel, Extra, Field, StrictStr


class UserRole(Enum):
    guest = 'Guest'
    player = 'Player'
    administrator = 'Administrator'
    nanny_moderator = 'NannyModerator'
    regular_moderator = 'RegularModerator'
    senior_moderator = 'SeniorModerator'


class Rating(BaseModel):
    class Config:
        extra = Extra.forbid

    enabled: Optional[bool] = Field(None, description='Rating participation flag')
    quality: Optional[int] = Field(None, description='Quality rating')
    quantity: Optional[int] = Field(None, description='Quantity rating')


class BbParseMode(Enum):
    common = 'Common'
    info = 'Info'
    post = 'Post'
    chat = 'Chat'


class InfoBbText(BaseModel):
    class Config:
        extra = Extra.forbid

    value: Optional[StrictStr] = Field(None, description='Text')
    parse_mode: Optional[BbParseMode] = Field(None, alias='parseMode')


class ColorSchema(Enum):
    modern = 'Modern'
    pale = 'Pale'
    classic = 'Classic'
    classic_pale = 'ClassicPale'
    night = 'Night'


class PagingSettings(BaseModel):
    class Config:
        extra = Extra.forbid

    posts_per_page: Optional[int] = Field(
        None, alias='postsPerPage', description='Number of posts on a game room page'
    )
    comments_per_page: Optional[int] = Field(
        None,
        alias='commentsPerPage',
        description='Number of commentaries on a game or a topic page',
    )
    topics_per_page: Optional[int] = Field(
        None,
        alias='topicsPerPage',
        description='Number of detached topics on a forum page',
    )
    messages_per_page: Optional[int] = Field(
        None,
        alias='messagesPerPage',
        description='Number of private messages and conversations on dialogue page',
    )
    entities_per_page: Optional[int] = Field(
        None, alias='entitiesPerPage', description='Number of other entities on page'
    )


class UserSettings(BaseModel):
    class Config:
        extra = Extra.forbid

    color_schema: Optional[ColorSchema] = Field(None, alias='colorSchema')
    nanny_greetings_message: Optional[StrictStr] = Field(
        None,
        alias='nannyGreetingsMessage',
        description="Message that user's newbies will receive once they are connected",
    )
    paging: Optional[PagingSettings] = None


class UserDetails(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = Field(None, description='Login')
    roles: Optional[List[UserRole]] = Field(None, description='Roles')
    medium_picture_url: Optional[StrictStr] = Field(
        None, alias='mediumPictureUrl', description='Profile picture URL M-size'
    )
    small_picture_url: Optional[StrictStr] = Field(
        None, alias='smallPictureUrl', description='Profile picture URL S-size'
    )
    status: Optional[StrictStr] = Field(None, description='User defined status')
    rating: Optional[Rating] = None
    online: Optional[datetime] = Field(None, description='Last seen online moment')
    name: Optional[StrictStr] = Field(None, description='User real name')
    location: Optional[StrictStr] = Field(None, description='User real location')
    registration: Optional[datetime] = Field(
        None, description='User registration moment'
    )
    icq: Optional[StrictStr] = Field(None, description='User ICQ number')
    skype: Optional[StrictStr] = Field(None, description='User Skype login')
    original_picture_url: Optional[StrictStr] = Field(
        None, alias='originalPictureUrl', description='URL of profile picture original'
    )
    info: Optional[InfoBbText] = None
    settings: Optional[UserSettings] = None


class UserDetailsEnvelope(BaseModel):
    class Config:
        extra = Extra.forbid

    resource: Optional[UserDetails] = None
    metadata: Optional[Any] = Field(None, description='Additional metadata')
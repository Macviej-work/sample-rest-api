from enum import Enum
from pydantic import BaseModel, Field, field_validator

class Position(Enum):
    """
    Enum for the position of a soccer player.
    """
    GK = "goalkeeper"
    DEF = "defender"
    MID = "midfielder"
    FRW = "forward"

class Player(BaseModel):
    """
    Pydantic model for a soccer player.

    Attributes:
        id: The unique identifier of the player. (required)
        name: The name of the player. (required)
        age: The age of the player. (required, must be between 16 and 100)
        team: The team of the player. (optional)
        position: The position of the player. (optional)
        number: The number of the player. (optional, must be between 1 and 99)
        height: The height of the player. (optional, must be between 150 and 220)
        weight: The weight of the player. (optional, must be between 50 and 150)
        nationality: The nationality of the player. (optional)
        club: The club of the player. (optional)
    """
    id: int
    name: str = Field()
    age: int = Field(ge=16, le=100)
    team: str | None = None
    position: Position | None = None
    number: int | None = Field(default=None, ge=1, le=99)
    height: float | None = Field(default=None, ge=150, le=220)
    weight: float | None = Field(default=None, ge=50, le=150)
    nationality: str | None = None
    club: str | None = None

    @field_validator("name")
    @classmethod
    def normalize_name(cls, v: str) -> str:
        return v.title()
from fastapi import APIRouter, Body, status
from typing import Annotated
from models.player_model import Player

api_router = APIRouter()

@api_router.post(
    "/players",
    status_code=status.HTTP_201_CREATED,
    response_model=Player,
    tags=["players"]
    )
async def create_player(player: Annotated[Player, Body(description="The player to be created")]):
    saved_player = player
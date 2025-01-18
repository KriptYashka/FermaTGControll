import random
from typing import Any

from aiogram import Router, types, F

from routers.hello.views import move

router = Router(name=__name__)

@router.message(F.text.lower() == "иди")
async def hello_handler(msg: types.Message) -> Any:
    x, y = random.randint(-3, 3), random.randint(-3, 3)
    move(x, y)
    await msg.reply(f"{msg.from_user.username} вы передвинулись на {(x, y)}!")
import random
from typing import Any

from aiogram import Router, types, F

from routers.hello.views import move

router = Router(name=__name__)

@router.message(F.text.startswith("иди"))
async def hello_handler(msg: types.Message) -> Any:
    x, y = map(int, msg.text.split()[1:])
    move(x, y)
    await msg.answer(f"Передвигаемся в {x, y}")
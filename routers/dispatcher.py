from aiogram import Dispatcher
from routers.hello.router import router as router_hello


def create_dispatcher():
    dp = Dispatcher()
    dp.include_router(router_hello)
    return dp
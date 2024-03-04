from aiogram import Router
from . import set_lan
from . import orders
from . import search

router = Router()

router.include_routers(
    set_lan.router,
    orders.router,
    search.router
)
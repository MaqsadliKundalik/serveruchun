from aiogram import Router
from . import admins
from . import users

router = Router()

router.include_routers(
    admins.router,
    users.router
)

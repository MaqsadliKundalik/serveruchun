from aiogram import Router
from . import users
from . import admns

router = Router()
router.include_routers(
    admns.router,
    users.router
)
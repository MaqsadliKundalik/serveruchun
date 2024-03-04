from aiogram import Router
from . import registration_callback
from . import manage_users
from . import confirm_order
from . import set_lan
from . import times
router = Router()

router.include_routers(
    registration_callback.router,
    manage_users.router,
     confirm_order.router,
     set_lan.router,
     times.router
)
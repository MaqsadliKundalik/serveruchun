from aiogram import Router
from . import start
from . import additional_items
from . import settings
from . import main_menu
from . import products
from . import orders
from . import my_orders
from . import reports
from . import not_konow

router = Router()

router.include_routers(
    start.router,
    main_menu.router,
    additional_items.router,
    settings.router,
    products.router,
    orders.router,
    my_orders.router,
    reports.router,
     not_konow.router
)

from aiogram import Router
from . import start
from . import cancel
from . import add_product
from . import products
from . import del_products
from . import main_menu
from . import change_count_product
from . import users
from . import reports
from . import confirm_orders
from . import settings
# from . import not_konow

router = Router()

router.include_routers(
    start.router,
    cancel.router,
    main_menu.router,
    add_product.router,
    products.router,
    del_products.router,
    change_count_product.router,
    users.router,
    reports.router,
    confirm_orders.router,
    settings.router,
    # not_konow.router
)
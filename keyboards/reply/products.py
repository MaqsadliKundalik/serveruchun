from aiogram.utils.keyboard import ReplyKeyboardBuilder
from data import sqlPrompts
import words

def products_list_builder(lan):
    builder = ReplyKeyboardBuilder()
    if lan == "UZ": builder.button(text="🏠 Asosiy menyu")
    elif lan == "RU": builder.button(text="🏠 Главное меню")
    elif lan == "QA": builder.button(text="🏠 Tiykarǵı menyu")
    for i in sqlPrompts.get_products(): builder.button(text=i[1] + " - " + i[3])
    builder.adjust(1, 2)
    builder = builder.as_markup()
    builder.resize_keyboard = True
    builder.is_persistent = True
    return builder

def user_products_list_builder(lan, page):
    builder = ReplyKeyboardBuilder()
    if lan == "UZ": 
        builder.button(text="🏠 Asosiy menyu")
        builder.button(text="🛒 savat")
    elif lan == "RU":
        builder.button(text="🏠 Главное меню")
        builder.button(text="🛒 корзина")
    elif lan == "QA":
        builder.button(text="🏠 Tiykarǵı menyu")
        builder.button(text="🛒 sebet")
    
    products = sqlPrompts.get_products_page(page)
    all_products = sqlPrompts.get_products()
    for i in products: builder.button(text=i[1] + " - " + i[3])
    if len(all_products) > page * 200:
        builder.button(text="➡️")
    if len(all_products) > page * 200 > 200:
        builder.button(text="⬅️")
    builder.adjust(2)
    builder = builder.as_markup()
    builder.resize_keyboard = True
    builder.is_persistent = True
    return builder


def basket_menu_builder(orders, lan):
    builder = ReplyKeyboardBuilder()
    if lan == "UZ": builder.button(text="🏠 Asosiy menyu")
    elif lan == "RU": builder.button(text="🏠 Главное меню")
    elif lan == "QA": builder.button(text="🏠 Tiykarǵı menyu")
    for i in orders:
        builder.button(text=i)
    builder.adjust(1, 2)
    builder = builder.as_markup()
    builder.resize_keyboard = True
    builder.is_persistent = True
    return builder

def manage_products_builder(lan):
    builfer = ReplyKeyboardBuilder()
    for i in words.dict[lan]["manage_products"]["main_menus"]:
        builfer.button(text=i)
    builfer.adjust(2, 1)
    builfer = builfer.as_markup()  
    builfer.resize_keyboard = True
    return builfer
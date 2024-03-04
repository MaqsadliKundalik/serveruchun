from aiogram.utils.keyboard import InlineKeyboardBuilder
import words

def order_manage_menu_builder(lan, product_id):
    builder = InlineKeyboardBuilder()
    menu = words.dict[lan]["basket"]["order_manage_menu"]
    builder.button(text=menu[0], callback_data=f"manageOrder:changeson:{product_id}")
    builder.button(text=menu[1], callback_data=f"manageOrder:delorder:{product_id}")
    builder.adjust(1)
    return builder.as_markup()

def confirm_order_builder(lan, order_id):
    builder = InlineKeyboardBuilder()
    menu = words.dict[lan]["confirm_order"]["confirm_menu"]
    print(menu)
    builder.button(text=menu[0], callback_data=f"confirmorder:confirmed:{order_id}")
    builder.button(text=menu[1], callback_data=f"confirmorder:canceled:{order_id}")
    builder.adjust(1)
    return builder.as_markup()

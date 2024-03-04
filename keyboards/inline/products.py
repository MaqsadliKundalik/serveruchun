from aiogram.utils.keyboard import InlineKeyboardBuilder
import words

def add_order_menu_builder(lan, product_id):
    builder = InlineKeyboardBuilder()
    builder.button(text=words.dict[lan]["products_user"]["add_order_menu"], callback_data=f"addOrder:{product_id}")
    return builder.as_markup()    

def search_products(lan):
    builder = InlineKeyboardBuilder()
    text = words.dict[lan]["search_inline_mode"]
    builder.button(text=text, switch_inline_query_current_chat=" ")
    return builder.as_markup()

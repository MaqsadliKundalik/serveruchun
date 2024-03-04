from aiogram.utils.keyboard import InlineKeyboardBuilder
from data import sqlPrompts
import words

def users_list_menu_builder():
    builder = InlineKeyboardBuilder()
    for i in sqlPrompts.get_suers():
        if i[1]:
            builder.button(text=i[1], callback_data=f"manageusers:{i[0]}")
        else:
            sqlPrompts.del_user(i[0])

    builder.adjust(1)
    return builder.as_markup() 

def manage_user_menu(lan, user_id):
    builder = InlineKeyboardBuilder()
    menu_texts = words.dict[lan]["manage_users"]["manage_user_menu"]
    builder.button(text=menu_texts[0], callback_data=f"manageuser:delDB:{user_id}")
    builder.button(text=menu_texts[1], callback_data=f"manageuser:block:{user_id}")
    builder.button(text=menu_texts[2], callback_data=f"manageuser:active:{user_id}")
    builder.button(text=menu_texts[3], callback_data=f"manageuser:addadmin:{user_id}")
    builder.button(text=menu_texts[4], callback_data=f"manageuser:rmadmin:{user_id}")
    builder.button(text=menu_texts[5], callback_data=f"manageuser:changebalans:{user_id}")
    builder.button(text=menu_texts[6], callback_data=f"manageuser:userslist:{user_id}")
    builder.adjust(1, 2)
    return builder.as_markup()
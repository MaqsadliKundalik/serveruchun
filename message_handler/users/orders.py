from aiogram import Router, F, Bot
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.fsm.context import FSMContext
from aiogram.filters import and_f
from data import sqlPrompts
import keyboards
import words
import filters
import states
import utils

router = Router()

@router.message(filters.any.textInTuple("🛒 savat", "🛒 корзина", "🛒 sebet"))
async def basket_answer(message: Message, state: FSMContext):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    if sqlPrompts.get_orders():
        get_orders = sqlPrompts.get_wait_orders(message.from_user.id)
        orders = []

        for i in get_orders:
            product = sqlPrompts.get_productById(i[1])
            menu = f"{product[0]} - {product[2]}"
            if not menu in orders:
                orders.append(menu)
                
        await message.answer(message.text, reply_markup=keyboards.reply.products.basket_menu_builder(orders, lan))
        await state.set_state(states.orders.UserGetOerder.name)
    else:
        text = words.dict[lan]["basket"]["empty_basket"]
        await message.answer(text)

@router.message(states.orders.UserGetOerder.name)
async def get_order_name_answer(message: Message, state: FSMContext):
    if len(message.text.split(" - ")) == 2:
        product_name = message.text.split(" - ")[0]
        product_size = message.text.split(" - ")[1]
        product = sqlPrompts.get_product_by_name_and_size(product_name, product_size)
        orders = sqlPrompts.get_order_by_user_ID_and_product_ID(message.from_user.id, product[0])
        lan = sqlPrompts.get_user(message.from_user.id)[1]
        if product:
            for order in orders:
                media = MediaGroupBuilder()
                imgs_count = 0
                if product[3]: media.add_photo(product[3]); imgs_count += 1
                if product[4]: media.add_photo(product[4]); imgs_count += 1
                if product[5]: media.add_photo(product[5]); imgs_count += 1
                if product[6]: media.add_photo(product[6]); imgs_count += 1
                if product[7]: media.add_photo(product[7]); imgs_count += 1
                text = words.dict[lan]["basket"]["order_data"](product_name, product_size, order[1], product[2], order[2], order[0])
                if imgs_count:
                    await message.answer_media_group(media.build())
                await message.answer(text, reply_markup=keyboards.inline.orders.order_manage_menu_builder(lan, order[0]))
        else:
            text = words.dict[lan]["basket"]["not_found_order"]
            await message.answer(text)
    else:
        await message.answer("🤔")

@router.message(states.orders.ChangeOrderCount.soni)
async def change_order_count_soni_answer(message: Message, bot: Bot, state: FSMContext):
    if message.text.isdigit():
        order_count = int(message.text)
        context_data = await state.get_data()
        order_id = context_data.get("order_id")
        order = sqlPrompts.get_order_by_ID(order_id)
        product = sqlPrompts.get_productById(order[1])
        user = sqlPrompts.get_user(message.from_user.id)
        lan = sqlPrompts.get_user(message.from_user.id)[1]
        if order_count <= product[1] + order[2]:
            sqlPrompts.update_order(
                order_id,
                order_count
            )
            sqlPrompts.update_balans(
                message.from_user.id,
                user[3] - (order_count - order[2]) * product[3] if order[2] > order_count else user[3] + (order[2] - order_count) * product[3], 
            )
            sqlPrompts.update_product(
                order[1],
                soni=product[1] - (order_count - order[2]) if order[2] < order_count else product[1] + (order[2] - order_count), 
                is_soni=True
            )

            for i in sqlPrompts.get_admins():
                lan = sqlPrompts.get_user(i[0])[1]
                text = words.dict[lan]["changed_count_order_message"](order_id, user[0])
                await bot.send_message(chat_id=i[0], text=text)

            lan = sqlPrompts.get_user(message.from_user.id)[1]

            user = sqlPrompts.get_user(message.from_user.id)
            text = words.dict[lan]["basket"]["save_order"](user[3])
            await message.answer(text, reply_markup=keyboards.reply.main_menu.menu_builder(lan))
            await state.clear()
        else:
            text = words.dict[lan]["basket"]["error_order_count"]
            await message.answer(text)
    else:
        text = words.dict[lan]["basket"]["error_order_count"]
        await message.answer(text)
from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.fsm.context import FSMContext
from data import sqlPrompts
import filters
import words
import keyboards
import states

router = Router()

@router.message(filters.any.textInTuple("📦 Ónimler", "📦 Товары", "📦 Mahsulotlar"))
async def products_answer(message: Message, bot: Bot, state: FSMContext):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    user = sqlPrompts.get_user(message.from_user.id)
    limit = sqlPrompts.get_users_limit()[0]
    if user[3] > limit:
        text = words.dict[lan]["products_user"]["main_menu_text"]
        await state.update_data(part=1)
        await message.answer(text, reply_markup=keyboards.reply.products.user_products_list_builder(lan, 1))
        await message.answer("🔎", reply_markup=keyboards.inline.products.search_products(lan))
        await state.set_state(states.orders.UserGetPorduct.name)
    else:
        await message.answer(f"Balans: {user[3]} USD\nLimit: {limit} USD")

@router.message(states.orders.UserGetPorduct.name)
async def get_product_answer(message: Message, state: FSMContext):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    if len(message.text.split(" - ")) == 2:
        product_name = message.text.split(" - ")[0]
        product_size = message.text.split(" - ")[1]
        product = sqlPrompts.get_product_by_name_and_size(product_name, product_size)
        if product:
            await state.update_data(id=int(product[0]))
            media = MediaGroupBuilder()
            imgs_count = 0
            if product[3]: media.add_photo(product[3]); imgs_count += 1
            if product[4]: media.add_photo(product[4]); imgs_count += 1
            if product[5]: media.add_photo(product[5]); imgs_count += 1
            if product[6]: media.add_photo(product[6]); imgs_count += 1
            if product[7]: media.add_photo(product[7]); imgs_count += 1
            text = words.dict[lan]["products_user"]["product_data"](product_name, product_size, product[1], product[2])
            if imgs_count:
                await message.answer_media_group(media.build())
            await message.answer(text, parse_mode="HTML", reply_markup=keyboards.inline.products.add_order_menu_builder(lan, product[0]))
        else:
            text = words.dict[lan]["products_user"]["not_found_product"]
            await message.answer(text)
    else:
    
        data = await state.get_data()
        all_products = sqlPrompts.get_products()
        part = data.get("part")
        if message.text == "⬅️" and part > 1:
            await state.update_data(part=part - 1)
            text = words.dict[lan]["products_user"]["main_menu_text"]    
            await message.answer(text, reply_markup=keyboards.reply.products.user_products_list_builder(lan, part - 1))
        elif message.text == "➡️" and len(all_products) > (data.get("part") + 1) * 200:
            await state.update_data(part=part + 1)
            text = words.dict[lan]["products_user"]["main_menu_text"]    
            await message.answer(text, reply_markup=keyboards.reply.products.user_products_list_builder(lan, part + 1))
        else:                
            await message.answer("🤔")

@router.message(states.orders.UserGetPorduct.soni)
async def add_order_soni_answer(message: Message, bot: Bot, state: FSMContext):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    if message.text.isdigit():
        order_count = int(message.text)
        context_data = await state.get_data()
        product_id = context_data.get("id")
        product = sqlPrompts.get_productById(product_id)
        user = sqlPrompts.get_user(message.from_user.id)
        if order_count <= product[1]:
            sqlPrompts.add_order(
                message.from_user.id,
                product_id,
                order_count
            )
            sqlPrompts.update_balans(
                message.from_user.id,
                user[3] - order_count * product[3], 
            )
            sqlPrompts.update_product(
                product_id,
                soni=product[1] - order_count,
                is_soni=True
            )

            for i in sqlPrompts.get_admins():
                lan = sqlPrompts.get_user(i[0])[1]
                order_id = sqlPrompts.get_orders()[0][1]
                text = words.dict[lan]["products_user"]["new_order"](order_id)
                await bot.send_message(chat_id=i[0], text=text)

            lan = sqlPrompts.get_user(message.from_user.id)[1]

            user = sqlPrompts.get_user(message.from_user.id)
            text = words.dict[lan]["products_user"]["save_order"](user[3])
            await message.answer(text, reply_markup=keyboards.reply.main_menu.menu_builder(lan))
            await state.clear()
        else:
            text = words.dict[lan]["products_user"]["error_order_count"]
            await message.answer(text)
    else:
        text = words.dict[lan]["products_user"]["error_order_count"]
        await message.answer(text)
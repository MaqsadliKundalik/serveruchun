from aiogram import Router, F, Bot
from aiogram.filters import and_f, or_f
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.fsm.context import FSMContext
from data import sqlPrompts
import filters
import words
import states
import keyboards
import utils

router = Router()

@router.message(and_f(filters.admins.IsAdmin(), filters.any.textInTuple("Mahsulot qo'shish", "Добавить продукт", "Ónim qosıw")))
async def add_product_answer(message: Message, state: FSMContext):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    text = words.dict[lan]["add_product"]["send_name"]
    await message.answer(text, reply_markup=keyboards.reply.cancel.cancel_menu_builder(lan))
    await state.set_state(states.ProductsOperations.AddPorduct.name)

@router.message(states.ProductsOperations.AddPorduct.name)
async def add_product_name_answer(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    text = words.dict[lan]["add_product"]["saved_name"]
    await message.answer(text)
    text = words.dict[lan]["add_product"]["send_size"] 
    await message.answer(text, reply_markup=keyboards.reply.cancel.cancel_menu_builder(lan))   
    await state.set_state(states.ProductsOperations.AddPorduct.size)

@router.message(states.ProductsOperations.AddPorduct.size)
async def add_product_size_answer(message: Message, state: FSMContext):
    products = sqlPrompts.get_products()
    context_data = await state.get_data()
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    for product in products:
        if context_data.get("name") == product[1] and message.text == product[3]:
            text = words.dict[lan]["add_product"]["save_not_size"]
            await message.answer(text)
            break   
    else:
        await state.update_data(size=message.text)
        text = words.dict[lan]["add_product"]["saved_size"]
        await message.answer(text)
        text = words.dict[lan]["add_product"]["send_soni"]
        await message.answer(text, reply_markup=keyboards.reply.cancel.cancel_menu_builder(lan))
        await state.set_state(states.ProductsOperations.AddPorduct.soni)

@router.message(states.ProductsOperations.AddPorduct.soni)
async def add_product_soni_answer(message: Message, state: FSMContext):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    
    if message.text.isdigit():
        await state.update_data(soni=int(message.text))
        text = words.dict[lan]["add_product"]["saved_soni"]
        await message.answer(text)
        text = words.dict[lan]["add_product"]["send_price"]
        await message.answer(text)
        await state.set_state(states.ProductsOperations.AddPorduct.price)
    else:
        text = words.dict[lan]["add_product"]["send_digit"]
        await message.answer(text)

@router.message(states.ProductsOperations.AddPorduct.price)
async def add_product_soni_answer(message: Message, state: FSMContext):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    try:
        price = float(message.text)
        await state.update_data(price=price)
        text = words.dict[lan]["add_product"]["saved_price"]
        await message.answer(text)
        text = words.dict[lan]["add_product"]["send_img1"]
        await message.answer(text, reply_markup=keyboards.reply.add_products_menu.save_this_data_builder(lan))
        await state.set_state(states.ProductsOperations.AddPorduct.img1)
    except:
        text = words.dict[lan]["add_product"]["send_digit"]
        await message.answer(text)

@router.message(and_f(or_f(states.ProductsOperations.AddPorduct.img1, states.ProductsOperations.AddPorduct.img2, states.ProductsOperations.AddPorduct.img3, states.ProductsOperations.AddPorduct.img4, states.ProductsOperations.AddPorduct.img5), and_f(filters.admins.IsAdmin(), F.photo)))
async def add_product_img1_answer(message: Message, state: FSMContext):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    text = words.dict[lan]["add_product"]["saved_img"]
    send_img_mesage = await message.answer_photo(message.photo[0].file_id, caption=text)
    
    if await state.get_state() == "AddPorduct:img1": 
        await state.update_data(img1=message.photo[0].file_id)
        await state.set_state(states.ProductsOperations.AddPorduct.img2)
    elif await state.get_state() == "AddPorduct:img2": 
        await state.update_data(img2=message.photo[0].file_id)
        await state.set_state(states.ProductsOperations.AddPorduct.img3)
    elif await state.get_state() == "AddPorduct:img3": 
        await state.update_data(img3=message.photo[0].file_id)
        await state.set_state(states.ProductsOperations.AddPorduct.img4)
    elif await state.get_state() == "AddPorduct:img4":
        await state.update_data(img4=message.photo[0].file_id)
        await state.set_state(states.ProductsOperations.AddPorduct.img5)
    elif await state.get_state() == "AddPorduct:img5": 
        await state.update_data(img5=message.photo[0].file_id)
        await send_img_mesage.delete()
        await add_product_send_answer(message, state)

@router.message(and_f(or_f(states.ProductsOperations.AddPorduct.img1, states.ProductsOperations.AddPorduct.img2, states.ProductsOperations.AddPorduct.img3, states.ProductsOperations.AddPorduct.img4, states.ProductsOperations.AddPorduct.img5), filters.any.textInTuple("✅ Yuborish", "✅ Отправить", "✅ Jiberiw")))
async def add_product_send_answer(message: Message, state: FSMContext):
    
        data = await state.get_data()
        lan = sqlPrompts.get_user(message.from_user.id)[1]

        media = MediaGroupBuilder()
        imgs_count = 0
        if data.get('img1'): media.add_photo(data.get('img1')); imgs_count += 1
        if data.get('img2'): media.add_photo(data.get('img2')); imgs_count += 1
        if data.get('img3'): media.add_photo(data.get('img3')); imgs_count += 1
        if data.get('img4'): media.add_photo(data.get('img4')); imgs_count += 1
        if data.get('img5'): media.add_photo(data.get('img5')); imgs_count += 1
        
        text = words.dict[lan]["add_product"]["product_data"](data.get("name"), data.get("size"), data.get("soni"), data.get("price"))
        media.caption = text

        if imgs_count: await message.answer_media_group(media.build())
        else: await message.answer(text)

        text = words.dict[lan]["add_product"]["confirm_text"]
        await message.answer(text, reply_markup=keyboards.reply.add_products_menu.confirm_data_builder(lan))
        await state.set_state(states.ProductsOperations.AddPorduct.confirm)

@router.message(and_f(states.ProductsOperations.AddPorduct.confirm, filters.any.textInTuple("✅ Tasdiqlash", "✅ Подтверждение", "✅ Tastıyıqlaw")))
async def add_product_confirm_answer(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    product_id = sqlPrompts.add_product(
            data.get("name"),
            data.get("soni"),
            data.get("size"),
            data.get("price"),
            data.get("img1"),
            data.get("img2"),
            data.get("img3"),
            data.get("img4"),
            data.get("img5"),
        )
    text = words.dict[lan]["add_product"]["saved_product"](product_id)
    await message.answer(text, reply_markup=keyboards.reply.admin_menu.main_menu_builder(lan))
    text_dict = {
        "msg1": words.dict["UZ"]["new_product_message"](data.get("name")),
        "msg2": words.dict["RU"]["new_product_message"](data.get("name")),
        "msg3": words.dict["QA"]["new_product_message"](data.get("name")),
    }
    sending_users = await utils.send_text_message_to_users(sqlPrompts.get_suers_id(), text_dict["msg1"], text_dict["msg2"], text_dict["msg3"], bot)
    text = words.dict[lan]["sending_message_users_count"](sending_users)
    await message.answer(text)
    await state.clear()

from aiogram import Router, F, Bot
from aiogram.filters import and_f
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent, ChosenInlineResult
from data import sqlPrompts
from aiogram.fsm.context import FSMContext
import words
import states
import keyboards
import utils

router = Router()

@router.inline_query()
async def inline_query_reply(query: InlineQuery, state: FSMContext):
        name, size = None, None
        
        if len(query.query.split(" && ")) == 2:
            name = query.query.split(" && ")[0]
            size = query.query.split(" && ")[1]
        else:    
            name = query.query
            size = query.query

        products = sqlPrompts.get_products_for_inline_mode(name, size)
        results = []
        
        for i in products:
            results.append(
                InlineQueryResultArticle(
                    id=str(i[0]),
                    title=f"{i[1]} - {i[3]}",
                    description=f"💰 {utils.pulni_qismlash(i[4])} USD | 🔄 {i[2]}",
                    input_message_content=InputTextMessageContent(message_text=f"{i[1]} - {i[3]}")
                )
            )    
        try:
            await query.answer(results=results)
        except:
            await query.answer(results=[
                InlineQueryResultArticle(
                    id="nottfound",
                    title="503 Error",
                    input_message_content=InputTextMessageContent(message_text="503 Error")
                )
            ])









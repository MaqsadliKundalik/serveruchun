from aiogram.fsm.state import StatesGroup, State

class ReportDate(StatesGroup):
    date = State()

class FilteredReports(StatesGroup):
    type = State()
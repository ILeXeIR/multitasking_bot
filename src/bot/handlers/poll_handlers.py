from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


poll_router = Router()


class PollStates(StatesGroup):
    question_state = State()
    options_state = State()
    anonymous_state = State()
    multiple_answers_state = State()


@poll_router.message(Command(commands=["poll"]))
async def ask_poll_question(message: types.Message, state: FSMContext):
    await state.set_state(PollStates.question_state)
    await message.answer("Write a poll question.\n"
                         "Use /cancel to quit this command.")


@poll_router.message(PollStates.question_state)
async def get_poll_question(message: types.Message, state: FSMContext):
    # Get poll question, 1-300 characters
    question = message.text.strip()
    if 1 <= len(question) <= 300:
        await state.update_data(question=question)
        await state.set_state(PollStates.options_state)
        await message.answer("Add 1st option")
    else:
        await message.answer("Incorrect question size. Option may consist of "
                             "1-300 characters.\nPlease try again.")


@poll_router.message(PollStates.options_state)
async def get_poll_option(message: types.Message, state: FSMContext):
    # Add one answer option to the list of options
    # Limits: 2-10 options, 1-100 characters each
    poll_option = message.text.strip()
    if len(poll_option) < 1 or len(poll_option) > 100:
        await message.answer("Incorrect option size. Option may consist of "
                             "1-100 characters.\nPlease try again.")
        return None
    options = (await state.get_data()).get("options")
    if options is None:
        await state.update_data(options=[poll_option])
        await message.answer("Add 2nd option")
    elif poll_option.lower() == "next" and len(options) > 1:
        await state.set_state(PollStates.anonymous_state)
        await message.answer("Do you want to create an anonymous poll? (yes/no)")
    elif poll_option in options:
        await message.answer("Option must be unique. Add another")
    else:
        options.append(poll_option)
        await state.update_data(options=options)
        if len(options) == 10:
            await state.set_state(PollStates.anonymous_state)
            await message.answer("Do you want to create an anonymous poll?\n"
                                 "(yes/no)")
        else:
            await message.answer("Add another option or "
                                 "send 'next' to go to next step")


@poll_router.message(PollStates.anonymous_state)
async def set_poll_anonymous(message: types.Message, state: FSMContext):
    # Set 'is_anonymous' poll parameter
    is_anonymous = message.text.strip().lower()
    if is_anonymous == "yes":
        await state.update_data(is_anonymous=True)
    elif is_anonymous == "no":
        await state.update_data(is_anonymous=False)
    else:
        await message.answer("Answer may be 'yes' or 'no'.\n"
                             "Do you want to create an anonymous poll?")
        return None
    await state.set_state(PollStates.multiple_answers_state)
    await message.answer("Do you want to allow multiple answers? (yes/no)")


@poll_router.message(PollStates.multiple_answers_state)
async def create_poll(message: types.Message, state: FSMContext):
    # Set 'allows_multiple_answers' poll parameter and create a poll
    is_multiple = message.text.strip().lower()
    if is_multiple == "yes":
        await state.update_data(allows_multiple_answers=True)
    elif is_multiple == "no":
        await state.update_data(allows_multiple_answers=False)
    else:
        await message.answer("Answer may be 'yes' or 'no'.\n"
                             "Do you want to allow multiple answers? (yes/no)")
        return None
    poll_params = await state.get_data()
    await state.clear()
    await message.answer_poll(
        question=poll_params["question"],
        options=poll_params["options"],
        is_anonymous=poll_params["is_anonymous"],
        allows_multiple_answers=poll_params["allows_multiple_answers"]
    )

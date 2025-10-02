import asyncio
import django
import sys
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from asgiref.sync import sync_to_async

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'normativ.settings')
django.setup()

from course_2.models import Course

API_KEY = ""
TOKEN = "8294589794:AAFtZPv5HYekONB7xPakE6b7zm53J3jDWrQ"

bot = Bot(TOKEN)
dp = Dispatcher()


# conn = pg.connect(
#     dbname="postgres",
#     user="postgres",
#     password="201621",
#     host="localhost",
#     port="5432"
# )
# cursor = conn.cursor()

@sync_to_async
def get_products():
    return list(Course.objects.all())


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    # cursor.execute("SELECT title, price FROM course_course;")
    # infos = cursor.fetchall()
    infos = await get_products()

    if infos:
        text = "\n".join([f"{c.title} — {c.price} суммов" for c in infos])
        await message.answer(text)

    else:
        await message.answer("Курсов нету")


async def main():
    print("🤖 Бот запустился...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


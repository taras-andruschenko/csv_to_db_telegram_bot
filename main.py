import init_django_orm  # noqa: F401
import telebot
from config import TOKEN
from csv_to_db.models import Date, Name, Username
from datetime import datetime


def run_telegram_bot():
    bot = telebot.TeleBot(TOKEN)

    def update_db(csv_file) -> None:
        """This function decode a file and update data_base"""

        file = csv_file.decode("UTF-8")
        clear_file = file.split("\r\n")[1:-1]
        for i, row in enumerate(clear_file):
            column = row.split(";")
            current_date = datetime.strptime(column[0], "%d.%m.%Y").date()
            Date.objects.create(date=current_date)
            Name.objects.create(owner_name=column[1])
            Username.objects.create(user_name=column[2])

    @bot.message_handler(commands=["start"])
    def start(message) -> None:
        bot.send_message(message.chat.id, "Now you can add your csv-file")

    @bot.message_handler(content_types=["document"])
    def handle_csv_file(message) -> None:
        """
        This function receives a file from the telegram bot and
        tries to update the data in the database, if the data is correct,
        otherwise it throws an error.
        """
        try:
            file_info = bot.get_file(message.document.file_id)
            csv_file = bot.download_file(file_info.file_path)
            update_db(csv_file)
            bot.reply_to(
                message,
                "File received and database updated successfully",
            )

        except Exception:
            bot.reply_to(
                message,
                "Something went wrong, "
                "please check the file you are sending",
            )

    bot.polling(none_stop=True)


if __name__ == "__main__":
    run_telegram_bot()

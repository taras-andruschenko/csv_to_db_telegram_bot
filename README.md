# csv_to_db_telegram_bot

A simple Telegram bot that accepts files with a fixed structure, 
splits the columns of the file and writes to different database tables

# Installing using Github

    git clone https://github.com/taras-andruschenko/csv_to_db_telegram_bot.git
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python main.py

# How to use

    Find **@CsvtodbBot** in your telegram
    Send "/start" to the bot
    Just drop your csv-files via bot and check your data base 

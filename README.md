# Deployment
- Create a python virtual environment (up to you)
- Install dependencies using `pip install -r requirements.txt`
- Create a copy of `.env.example` using `cp .env.example .env`
- Modify `.env` file to represent your configuration
- Simply run `python main.py` 
- Text `/start` to the bot you've made through BotFather

## Database url
https://docs.sqlalchemy.org/en/20/core/engines.html#database-urls
Read above about database connection strings
#### Sqlite
Please note that sqlite does not work well with this bot and you will have issues. Use mysql or postgresql.
A `docker-compose.yml` has been provided to be make your life easier

## Generating session string
As this bot requires both an actual bot and a user bot you will have to generate a session string.
You can do this by simply running `python generate_session_string.py` and copy pasting the output 
to the .env file for `TG_USER_SESSSION`

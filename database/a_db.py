import aiosqlite
from database import sql_queries

# class AsyncDatabase:
#     def __init__(self, db_path='db.sqlite3'):
#         self.db_path = db_path
#
#     async def create_tables(self):
#         async with aiosqlite.connect(self.db_path) as db:
#             await db.execute(sql_queries.CREATE_USER_TABLE_QUERY)
#
#             await db.commit()
#             print("Database connected successfully")
#
#     async def execute_query(self, query, params=None, fetch="none"):
#         async with aiosqlite.connect(self.db_path) as db:
#             db.row_factory = aiosqlite.Row
#             cursor = await db.execute(query, params or ())
#
#             if fetch == "none":
#                 await db.commit()
#                 return
#             elif fetch == "all":
#                 data = await cursor.fetchall()
#                 return [dict(row) for row in data] if data else []


import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_user(conn, user):
    sql = ''' INSERT INTO users(id, gender, age, bio)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    return cur.lastrowid


from telegram import ParseMode

update.message.reply_text(
    'Привет! Я бот. Как дела?\n<b>Жирный текст</b>\n<i>Курсив</i>',
    parse_mode=ParseMode.HTML
)

update.message.reply_animation(animation='https://example.com/animation.gif')


update.message.reply_photo(photo='https://example.com/photo.jpg')


def create_profile(conn, profile):
    sql = ''' INSERT INTO profiles(user_id, profile_info)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, profile)
    conn.commit()
    return cur.lastrowid

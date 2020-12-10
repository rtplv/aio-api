import asyncio
import logging
import os

from dotenv import load_dotenv
from app.config.logger import get_logger_handler

load_dotenv()

# Logging
logging.basicConfig(level=logging.INFO)

app_logger = logging.getLogger('app')
app_logger.addHandler(get_logger_handler('app.log'))

api_server_logger = logging.getLogger('api_server')
api_server_logger.addHandler(get_logger_handler('api_server.log'))

# Main application event loop
main_loop = asyncio.get_event_loop()

# Main storage
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_DATABASE = os.getenv('DB_DATABASE')

# Optional: Database connections pool

# async def init_db_pool() -> Pool:
#     return await asyncpg.create_pool(
#         host=DB_HOST,
#         port=DB_PORT,
#         user=DB_USERNAME,
#         password=DB_PASSWORD,
#         database=DB_DATABASE,
#         min_size=1,
#         max_size=20,
#         max_inactive_connection_lifetime=5
#     )
#
#
# db_pool: Pool = asyncio.get_event_loop().run_until_complete(init_db_pool())

# db_utils.py

from sqlalchemy import create_engine
import os

DB_USER = os.environ.get('DB_USER', 'root')
DB_PASS = os.environ.get('DB_PASS', '')  # No password by default
DB_NAME = os.environ.get('DB_NAME', 'group14kroger')
INSTANCE_CONNECTION_NAME = os.environ.get('INSTANCE_CONNECTION_NAME', 'group14kroger:us-west2:group14kroger')

# Create the SQLAlchemy engine with a connection timeout
engine = create_engine(
    f'mysql+pymysql://{DB_USER}:{DB_PASS}@/{DB_NAME}?unix_socket=/cloudsql/{INSTANCE_CONNECTION_NAME}',
    pool_pre_ping=True,
    pool_recycle=3600,
    connect_args={'connect_timeout': 10}  # Timeout after 10 seconds
)

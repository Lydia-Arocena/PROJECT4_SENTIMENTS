import sqlalchemy as alch
import os
import dotenv

dotenv.load_dotenv()

password = os.getenv("pass_sql")
db_name = "proyecto_sentiments2"
connectionData = f"mysql+pymysql://root:{password}@localhost/{db_name}"
engine = alch.create_engine(connectionData)
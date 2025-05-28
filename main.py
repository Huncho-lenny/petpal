from db.connection import CONN
from cli import run
from models.owner import Owner
from models.pet import Pet

Owner.create_table()
Pet.create_table()

run()


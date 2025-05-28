from lib.db.connection import CONN, CURSOR
from lib.models.pet import Pet 

class Owner:
    all = []

    def __init__(self, name, id=None):
        self.id = id
        self.name = name
        Owner.all.append(self)

    def __repr__(self):
        return f"<Owner {self.id}: {self.name}>"


    def save(self):
        if self.id:
            CURSOR.execute("UPDATE owners SET name = ? WHERE id = ?", (self.name, self.id))
        else:
            CURSOR.execute("INSERT INTO owners (name) VALUES (?)", (self.name,))
            self.id = CURSOR.lastrowid
        CONN.commit()


    def pets(self):
        from lib.models.pet import Pet
        CURSOR.execute("SELECT * FROM pets WHERE owner_id = ?", (self.id,))
        rows = CURSOR.fetchall()
        return [Pet.instance_from_db(row) for row in rows]


    def add_pet(self, pet):
        pet.owner_id = self.id
        pet.save()


    @staticmethod
    def find_by_id(owner_id):
        CURSOR.execute("SELECT * FROM owners WHERE id = ?", (owner_id,))
        row = CURSOR.fetchone()
        return Owner.instance_from_db(row) if row else None


    @classmethod
    def instance_from_db(cls, row):
        id, name = row
        return cls(name=name, id=id)

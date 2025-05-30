from lib.db.connection import CURSOR, CONN

class Pet:
    CONN = None
    CURSOR = None

    VALID_TYPES = ['dog', 'cat', 'bird', 'fish', 'lizard', 'hamster']

    all = []

    def __init__(self, name, breed, age, owner_id, id=None):
        self.name = name
        self.breed = breed
        self.age = age
        self.owner_id = owner_id
        self.id = id
        Pet.all.append(self)

    def save(self, cursor):
        if self.id is None:
            cursor.execute(
                "INSERT INTO pets (name, breed, age, owner_id) VALUES (?, ?, ?, ?)",
                (self.name, self.breed, self.age, self.owner_id)
            )
            self.id = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE pets SET name=?, breed=?, age=?, owner_id=? WHERE id=?",
                (self.name, self.breed, self.age, self.owner_id, self.id)
            )

    @classmethod
    def get_by_owner(cls, owner_id, cursor):
        cursor.execute("SELECT * FROM pets WHERE owner_id = ?", (owner_id,))
        rows = cursor.fetchall()
        return [cls(row[1], row[2], row[3], row[4], row[0]) for row in rows]

    def __init__(self, name, pet_type, owner_id=None, id=None):
        self.id = id
        self.name = name
        self.pet_type = pet_type 
        self.owner_id = owner_id
        Pet.all.append(self)

    def __repr__(self):
        return f"<Pet {self.id}: {self.name} the {self.pet_type}>"

    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, value):
        if value.lower() not in Pet.VALID_TYPES:
            raise ValueError(f"{value} is not a valid pet type.")
        self._pet_type = value.lower()

    def save(self):
        if self.id:
            CURSOR.execute("UPDATE pets SET name = ?, pet_type = ?, owner_id = ? WHERE id = ?",
                           (self.name, self.pet_type, self.owner_id, self.id))
        else:
            CURSOR.execute("INSERT INTO pets (name, pet_type, owner_id) VALUES (?, ?, ?)",
                           (self.name, self.pet_type, self.owner_id))
            self.id = CURSOR.lastrowid
        CONN.commit()

    def delete(self):
        CURSOR.execute("DELETE FROM pets WHERE id = ?", (self.id,))
        CONN.commit()

    @classmethod
    def instance_from_db(cls, row):
        id, name, pet_type, owner_id = row
        return cls(name, pet_type, owner_id, id)

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM pets")
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM pets WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        return cls.instance_from_db(row) if row else None

    def owner(self):
        from models.owner import Owner
        return Owner.find_by_id(self.owner_id)

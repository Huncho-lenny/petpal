DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS owners;

CREATE TABLE owners (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE pets (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    pet_type TEXT NOT NULL,
    age INTEGER NOT NULL,
    owner_id INTEGER,
    FOREIGN KEY (owner_id) REFERENCES owners(id)
);

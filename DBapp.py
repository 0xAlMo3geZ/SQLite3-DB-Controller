import database

database.add_one()

stuff = [
    ('', '', ''),
    ('', '', ''),
]

database.add_many(stuff)

database.delete_one(str())

database.show_all()

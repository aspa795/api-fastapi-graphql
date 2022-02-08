from orator import DatabaseManager, Schema, Model

DATABASES = {
    "postgres": {
        "driver": "postgres",
        "host": "localhost",
        "database": "postgres",
        "user": "postgres",
        "password": "postgres",
        "prefix": "",
        "port": 5477
    }
}

db = DatabaseManager(DATABASES)
schema = Schema(db)
Model.set_connection_resolver(db)
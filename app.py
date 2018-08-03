from api.v1.endpoints import app
from database.create_tables import create_tables


# if __name__ == '__main__':
#     app.run(debug=True)


if __name__ == '__main__':
    # tables = Tables()
    # tables.data_create()
    # tables.data_set()
    # tables.data()
    create_tables().entries_table()
    app.run(debug=True)

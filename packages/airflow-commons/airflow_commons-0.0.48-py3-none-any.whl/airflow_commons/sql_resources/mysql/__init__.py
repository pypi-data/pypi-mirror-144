import os

here = os.path.abspath(os.path.dirname(__file__))

DELETE_SQL_FILE = os.path.join(here, "delete.sql")

SELECT_ALL_SQL_FILE = os.path.join(here, "select_all.sql")

SELECT_SQL_FILE = os.path.join(here, "select.sql")

GET_ROW_COUNT_SQL_FILE = os.path.join(here, "get_row_count.sql")

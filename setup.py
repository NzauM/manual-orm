# set up DB
import sqlite3

OURDB = sqlite3.connect('school.db')
OURCURSOR = OURDB.cursor()

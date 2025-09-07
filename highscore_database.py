"""
Name: highscore_database.py
Author: Andrew Peterson
Date: 10/23/2024
Purpose: Create a high score database
"""

# import libary
import sqlite3

DATABASE = 'highscore.db'

CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS highscore (
        plyr_id      INTEGER PRIMARY KEY,
        plyr_name   TEXT,
        plyr_score    INTEGER,
        plyr_date   TEXT
    );
    """

INSERT_SCORE = """
    INSERT INTO highscore (
    plyr_name,
    plyr_score,
    plyr_date
    ) VALUES (?, ?, ?)
"""

FETCH_ALL_SCORES = "SELECT * FROM highscore;"

FETCH_SCORE = "SELECT * FROM highscore WHERE plyr_id = ?;"

DELETE_SCORE = "DELETE FROM highscore WHERE plyr_id = ?"

# create the table
def create_table():
    with sqlite3.connect(DATABASE) as connection:
        # create a cursor object
        cursor = connection.cursor()

        # execute the scipt against database
        cursor.execute(CREATE_TABLE)

# insert scores
def insert_score(plyr_name, plyr_score, plyr_date):
    with sqlite3.connect(DATABASE) as connection:
         # create a cursor object
        cursor = connection.cursor()

        # execute the scipt against database
        cursor.execute(
            INSERT_SCORE,
            (plyr_name, plyr_score, plyr_date)
        )

# fetch all scores
def fetch_all_scores():
    with sqlite3.connect(DATABASE) as connection:
        # create a cursor object
        cursor = connection.cursor()

        # execute the scipt against database
        scores = cursor.execute(FETCH_ALL_SCORES). fetchall()

        return scores
    
def fetch_score(plyr_id: int):
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        scores = cursor.execute(FETCH_SCORE, (plyr_id, )).fetchall()

        return scores
    
def delete_score(plyr_id: int):
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute(DELETE_SCORE, (plyr_id, ))
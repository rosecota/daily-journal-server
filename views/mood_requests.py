import sqlite3
import json
from models import Mood


def get_all_moods():
    """Get all Moods
    """
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
		SELECT 
			* 
		FROM Mood
        """)

        # Initialize an empty list to hold all entry representations
        moods = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an entry instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Entry class above.
            mood = Mood(row['id'], row['label'])

            # Add the dictionary representation of the mood to the list
            moods.append(mood.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(moods)


def get_single_mood(id):
    """Get single Mood
    """
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT * FROM Mood m
        WHERE m.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        if data is None:
            return False

        # Create an Mood instance from the current row
        mood = Mood(data['id'], data['label'])

        return json.dumps(mood.__dict__)


def delete_mood(id):
    """Delete Mood
    """
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Mood
        WHERE id = ?
        """, (id, ))

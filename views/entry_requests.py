import sqlite3
import json
from models import Entry, Mood


def get_all_entries():
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
		SELECT
			j.id,
			j.concept,
			j.entry,
			j.date,
			j.mood_id,
			m.label label
		FROM JournalEntry j
		JOIN Mood m
			ON m.id = j.mood_id
        """)

        # Initialize an empty list to hold all entry representations
        entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an entry instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Entry class above.
            entry = Entry(row['id'], row['concept'], row['entry'],
                          row['date'], row['mood_id'])

            # Create a mood instance from the current row
            mood = Mood(row['id'], row['label'])
            # Add the dictionary representation of the location to the entry
            entry.mood = mood.__dict__

            # Add the dictionary representation of the entry to the list
            entries.append(entry.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(entries)


def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
			j.id,
			j.concept,
			j.entry,
			j.date,
			j.mood_id,
			m.label label
        FROM JournalEntry j
        JOIN Mood m
            ON m.id = j.mood_id
        WHERE j.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        if data is None:
            return False

        # Create an Entry instance from the current row
        entry = Entry(data['id'], data['concept'], data['entry'],
                      data['date'], data['mood_id'])

        # Create a mood instance from the current row
        mood = Mood(data['id'], data['label'])
        # Add the dictionary representation of the location to the entry
        entry.mood = mood.__dict__

        return json.dumps(entry.__dict__)

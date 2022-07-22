import sqlite3
import json
from models import Entry, Mood, Tag


def get_all_entries():
    """Get all Entries
    """
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

            tags = []

            db_cursor.execute("""
            SELECT
                e.tag_id,
                t.label
            FROM EntryTag e
            JOIN Tag t
                ON e.tag_id = t.id
            WHERE e.entry_id = ?
            """, (row['id'], ))

            tag_dataset = db_cursor.fetchall()

            # tag_dataset = query_entrytag_by_entry_id(row['id'])

            for data in tag_dataset:

                # Create tag instance and set properties from db
                tag = Tag(data['tag_id'], data['label'])

                # Add the dictionary representation of the Tag to the list
                tags.append(tag.__dict__)

            # Add tags to entry obj
            entry.tags = tags

            # Add the dictionary representation of the entry to the list
            entries.append(entry.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(entries)


def get_single_entry(id):
    """Delete single Entry
    """
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

        tags = []

        db_cursor.execute("""
        SELECT
            e.tag_id,
            t.label
        FROM EntryTag e
        JOIN Tag t
            ON e.tag_id = t.id
        WHERE e.entry_id = ?
        """, (data['id'], ))

        tag_dataset = db_cursor.fetchall()

        # tag_dataset = query_entrytag_by_entry_id(data['id'])

        for data in tag_dataset:

            # Create tag instance and set properties from db
            tag = Tag(data['tag_id'], data['label'])

            # Add the dictionary representation of the Tag to the list
            tags.append(tag.__dict__)

        # Add tags to entry obj
        entry.tags = tags

        return json.dumps(entry.__dict__)


def create_entry(new_entry):
    """Post entry
    """
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO JournalEntry
            ( concept, entry, date, mood_id )
        VALUES
            ( ?, ?, ?, ?)
        """, (new_entry['concept'], new_entry['entry'],
              new_entry['date'], new_entry['moodId'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the entry dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_entry['id'] = id

    return json.dumps(new_entry)


def delete_entry(id):
    """Delete Entry
    """
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM JournalEntry
        WHERE id = ?
        """, (id, ))


def get_entries_search(search_term):
    """Return Entries that contain search word"""

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
        WHERE j.entry LIKE (?)
        """, (f'%{search_term}%', ))

        entries = []
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

    return json.dumps(entries)


# def query_entrytag_by_entry_id(id):
#     with sqlite3.connect("./dailyjournal.sqlite3") as conn:
#         conn.row_factory = sqlite3.Row
#         db_cursor = conn.cursor()

#         db_cursor.execute("""
#             SELECT
#                 e.tag_id,
#                 t.label
#             FROM EntryTag e
#             JOIN Tag t
#                 ON e.tag_id = t.id
#             WHERE e.entry_id = ?
#             """, (id, ))

#         dataset = db_cursor.fetchall()

#     return dataset

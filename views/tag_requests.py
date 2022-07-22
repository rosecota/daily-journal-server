import sqlite3
import json
from models import Tag


def get_all_tags():
    """Get all Tags
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
		FROM Tag
        """)

        # Initialize an empty list to hold all entry representations
        tags = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an entry instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Entry class above.
            tag = Tag(row['id'], row['label'])

            # Add the dictionary representation of the tag to the list
            tags.append(tag.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(tags)


def get_single_tag(id):
    """Get single Tag
    """
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT * FROM Tag m
        WHERE m.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        if data is None:
            return False

        # Create an Tag instance from the current row
        tag = Tag(data['id'], data['label'])

        return json.dumps(tag.__dict__)


def delete_tag(id):
    """Delete Tag
    """
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Tag
        WHERE id = ?
        """, (id, ))

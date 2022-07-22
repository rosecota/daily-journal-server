-- DROP TABLE IF EXISTS Mood;
-- DROP TABLE IF EXISTS Tag;
-- DROP TABLE IF EXISTS JournalEntry;
-- DROP TABLE IF EXISTS EntryTag;


CREATE TABLE `JournalEntry` (
	`id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`concept`  TEXT NOT NULL,
	`entry` TEXT NOT NULL,
	`date` DATE,
	`mood_id` INTEGER,
	FOREIGN KEY(`mood_id`) REFERENCES `Mood`(`id`)
);

CREATE TABLE `Mood` (
	`id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`label`  TEXT NOT NULL
);

CREATE TABLE `Tag` (
	`id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`label`  TEXT NOT NULL
);

CREATE TABLE `EntryTag` (
	`id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`entry_id` INTEGER,
	`tag_id` INTEGER,
	FOREIGN KEY(`entry_id`) REFERENCES `JournalEntry`(`id`),
	FOREIGN KEY(`tag_id`) REFERENCES `Tag`(`id`)
);

INSERT INTO `Mood` VALUES (null, "Happy");
INSERT INTO `Mood` VALUES (null, "Unconcerned");
INSERT INTO `Mood` VALUES (null, "Tragic");
INSERT INTO `Mood` VALUES (null, "Ok");
INSERT INTO `Mood` VALUES (null, "TIL");

INSERT INTO `Tag` VALUES (null, "til");
INSERT INTO `Tag` VALUES (null, "faq");
INSERT INTO `Tag` VALUES (null, "client-side");
INSERT INTO `Tag` VALUES (null, "server-side");
INSERT INTO `Tag` VALUES (null, "javascript");
INSERT INTO `Tag` VALUES (null, "python");
INSERT INTO `Tag` VALUES (null, "kennels");
INSERT INTO `Tag` VALUES (null, "daily-journal");
INSERT INTO `Tag` VALUES (null, "levelup");



INSERT INTO `JournalEntry` VALUES (null, "Javascript", "I learned about loops today. They can be a lot of fun.\nI learned about loops today. They can be a lot of fun.\nI learned about loops today. They can be a lot of fun.", "Mon Jul 19 2022 10:10:47", 1 );
INSERT INTO `JournalEntry` VALUES (null, "Python", "Python is named after the Monty Python comedy group from the UK. I'm sad because I thought it was named after the snake", "Wed Jul 19 2022 10:10:47", 3 );
INSERT INTO `JournalEntry` VALUES (null, "Python", "Why did it take so long for python to have a switch statement? It's much cleaner than if/elif blocks", "Wed Jul 19 2022 10:10:47", 4 );

INSERT INTO `EntryTag` VALUES (null, 1, 1);
INSERT INTO `EntryTag` VALUES (null, 1, 2);
INSERT INTO `EntryTag` VALUES (null, 2, 2);
INSERT INTO `EntryTag` VALUES (null, 2, 3);





SELECT
    j.id,
    j.concept,
    j.entry,
    j.date,
    j.mood_id,
    m.label label
FROM JournalEntry j
JOIN Mood m
    ON m.id = j.mood_id;

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
WHERE j.entry LIKE 'pyt';

SELECT 
	e.tag_id,
	t.label
FROM EntryTag e
JOIN Tag t
	ON e.tag_id = t.id
WHERE e.entry_id = 1

INSERT INTO `EntryTag` VALUES (null, 2, 6);
INSERT INTO `EntryTag` VALUES (null, 3, 6);
INSERT INTO `EntryTag` VALUES (null, 5, 5);
INSERT INTO `EntryTag` VALUES (null, 5, 2);
INSERT INTO `EntryTag` VALUES (null, 6, 2);
INSERT INTO `EntryTag` VALUES (null, 6, 1);
INSERT INTO `EntryTag` VALUES (null, 6, 3);
INSERT INTO `EntryTag` VALUES (null, 6, 7);
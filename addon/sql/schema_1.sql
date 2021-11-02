CREATE TABLE "ky_source" (
	"ky_source_tid"	INTEGER NOT NULL UNIQUE,
	"sql_created_datetime"	TEXT NOT NULL,
	"sql_modified_datetime"	TEXT NULL,
	"source_name"	TEXT NOT NULL,
	INTEGER PRIMARY KEY("ky_source_tid" AUTOINCREMENT)
)

CREATE TABLE "ky_sentence" (
	"ky_sentence_tid"	INTEGER NOT NULL UNIQUE,
	"sql_created_datetime"	TEXT NOT NULL,
	"sql_updated_datetime"	TEXT NULL,
	"ky_source_tid"	INTEGER NOT NULL,
	"sentence_text"	TEXT NOT NULL,
	INTEGER PRIMARY KEY("ky_sentence_tid" AUTOINCREMENT)
)

CREATE TABLE "ky_sentence_feature" (
	"ky_sentence_feature_tid"	INTEGER NOT NULL UNIQUE,
	"sql_created_datetime"	TEXT NOT NULL,
	"sql_modified_datetime"	TEXT NULL,
	"ky_sentence_tid"	INTEGER NOT NULL,
	"feature"	TEXT NOT NULL,
	"feature_type"	TEXT NOT NULL,	
	"feature_order_index"	INTEGER NOT NULL UNIQUE,
	INTEGER PRIMARY KEY("ky_sentence_feature_tid" AUTOINCREMENT),	
	FOREIGN KEY("ky_sentence_tid") REFERENCES "ky_sentence"("ky_sentence_tid"),
)

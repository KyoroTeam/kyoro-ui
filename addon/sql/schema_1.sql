CREATE TABLE ky_error_log (
	ky_error_log_tid	INTEGER PRIMARY KEY,
	sql_created_datetime	TEXT NOT NULL,
	sql_modified_datetime	TEXT NULL,
	error_text	TEXT NOT NULL
);
CREATE TABLE ky_source (
	ky_source_tid	INTEGER PRIMARY KEY,
	sql_created_datetime	TEXT NOT NULL,
	sql_modified_datetime	TEXT NULL,
	source_name	TEXT NOT NULL
);
CREATE TABLE ky_sentence (
	ky_sentence_tid	INTEGER PRIMARY KEY,
	sql_created_datetime	TEXT NOT NULL,
	sql_updated_datetime	TEXT NULL,
	ky_source_tid	INTEGER NOT NULL,
	sentence_text	TEXT NOT NULL,
	FOREIGN KEY(ky_source_tid) REFERENCES ky_source(ky_source_tid)
);
CREATE TABLE ky_sentence_feature (
	ky_sentence_feature_tid	INTEGER PRIMARY KEY,
	sql_created_datetime	TEXT NOT NULL,
	sql_modified_datetime	TEXT NULL,
	ky_sentence_tid	INTEGER NOT NULL,
	feature	TEXT NOT NULL,
	feature_type	TEXT NOT NULL,	
	feature_order_index	INTEGER NOT NULL,
	FOREIGN KEY(ky_sentence_tid) REFERENCES ky_sentence(ky_sentence_tid)
	UNIQUE (ky_sentence_tid, feature_type, feature_order_index) ON CONFLICT REPLACE	
);

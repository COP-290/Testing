DROP TABLE IF EXISTS posts;

CREATE TABLE Tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tags varchar(255),
    content TEXT NOT NULL
)
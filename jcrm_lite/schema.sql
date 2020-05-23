DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS contacts;

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE contacts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  company_name TEXT NOT NULL,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  created_by_user_id INTEGER NOT NULL,
  updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_by_user_id INTEGER NOT NULL,
  FOREIGN KEY (created_by_user_id) REFERENCES users (id),
  FOREIGN KEY (updated_by_user_id) REFERENCES users (id)
);

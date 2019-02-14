CREATE TABLE "Users"(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserId CHAR(256) NOT NULL UNIQUE,
    Username CHAR(256) NOT NULL,
    FirstName CHAR(256) NOT NULL,
    Profiles TEXT,
    IsBanned BOOLEAN,
    WarningsAmount INT,
    IsPrivileged BOOLEAN
)

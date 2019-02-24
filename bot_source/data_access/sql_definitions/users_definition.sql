CREATE TABLE "Users"(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserId CHAR(256) NOT NULL UNIQUE,
    Username CHAR(256),
    FirstName CHAR(256),
    Profile CHAR(256),
    IsBanned BOOLEAN,
    WarningsAmount INT,
    IsPrivileged BOOLEAN
)

CREATE TABLE "Users"(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ChatId CHAR(256) NOT NULL,
    Username CHAR(256) NOT NULL,
    Profiles TEXT,
    IsBanned BIT,
    WarningsAmount INT,
    IsPrivileged BIT
)

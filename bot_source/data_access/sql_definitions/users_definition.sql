CREATE TABLE "Users"(
    Id IDENTITY PRIMARY KEY,
    ChatId CHAR(256) NOT NULL,
    Username CHAR(256) NOT NULL,
    Profiles TEXT,
    IsBanned BIT,
    WarningsAmount INT,
    IsPrivileged BIT
)

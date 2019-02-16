CREATE TABLE "Waves"(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Start DATE NOT NULL,
    BiddingStart DATE,
    AssuringStart DATE,
    Finish DATE,
    UsersProfiles TEXT,
    Posts TEXT,
    WaveState CHAR(256)
)
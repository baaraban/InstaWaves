CREATE TABLE "Waves"(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Start DATE NOT NULL,
    RegistrationStart DATE,
    ExecutionStart DATE,
    AssuringStart DATE,
    Finish DATE,
    UsersProfiles TEXT,
    Posts TEXT,
    WaveState CHAR(256)
)
class UserQueries:
    UPDATE = '''UPDATE Users 
                SET ChatId = ?,
                    Username = ?,
                    FirstName = ?,
                    Profiles = ?,
                    IsBanned = ?,
                    WarningsAmount = ?,
                    IsPrivileged = ?
                WHERE ID = ?'''

    INSERT_QUERY = '''INSERT INTO Users(ChatId, Username, FirstName, Profiles, IsBanned, WarningsAmount, IsPrivileged) 
                        VALUES(?, ?, ?, ?, ?, ?, ?)'''

    CHECK_USER_BANNED= '''SELECT ID FROM USERS WHERE 
                                Username = ? AND IsBanned = 1'''

    SELECT_BY_USERNAME = '''SELECT ID, ChatId, Username, FirstName, Profiles, IsBanned, WarningsAmount, IsPrivileged
                            FROM USERS WHERE 
                            Username = ?'''
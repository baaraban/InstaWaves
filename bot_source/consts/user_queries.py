class UserQueries:
    UPDATE = '''UPDATE Users 
                SET UserId = ?,
                    Username = ?,
                    FirstName = ?,
                    Profiles = ?,
                    IsBanned = ?,
                    WarningsAmount = ?,
                    IsPrivileged = ?
                WHERE ID = ?'''

    INSERT = '''INSERT INTO Users(UserId, Username, FirstName, Profiles, IsBanned, WarningsAmount, IsPrivileged) 
                        VALUES(?, ?, ?, ?, ?, ?, ?)'''

    CHECK_USER_BANNED= '''SELECT ID FROM USERS WHERE 
                                UserId = ? AND IsBanned = 1'''

    SELECT_BY_USER_ID = '''SELECT ID, UserId, Username, FirstName, Profiles, IsBanned, WarningsAmount, IsPrivileged
                            FROM USERS WHERE 
                            UserId = ?'''

    SELECT_BY_USERNAME = '''SELECT ID, UserId, Username, FirstName, Profiles, IsBanned, WarningsAmount, IsPrivileged
                                FROM USERS WHERE 
                                USERNAME = ?'''
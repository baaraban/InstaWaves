class WaveQueries:
    UPDATE = '''UPDATE Waves 
                SET Start = ?,
                    BiddingStart = ?,
                    AssuringStart = ?,
                    Finish = ?,
                    UsersProfiles = ?,
                    Posts = ?,
                    WaveState = ?
                WHERE ID = ?'''

    INSERT = '''INSERT INTO Waves
                (Start, BiddingStart, AssuringStart, Finish, UsersProfiles, Posts, WaveState) 
                VALUES(?, ?, ?, ?, ?, ?, ?)'''

    SELECT_BY_STATE = '''SELECT * FROM Waves
                         WHERE WaveState = ?'''

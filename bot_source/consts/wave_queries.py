class WaveQueries:
    UPDATE = '''UPDATE Waves 
                SET Start = ?,
                    RegistrationStart = ?,
                    ExecutionStart = ?,
                    AssuringStart = ?,
                    Finish = ?,
                    UsersProfiles = ?,
                    WaveState = ?
                WHERE ID = ?'''

    INSERT = '''INSERT INTO Waves
                (Start, RegistrationStart, ExecutionStart, AssuringStart, Finish, UsersProfiles, WaveState) 
                VALUES(?, ?, ?, ?, ?, ?, ?)'''

    SELECT_BY_STATE = '''SELECT * FROM Waves
                         WHERE WaveState = ?'''

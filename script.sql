CREATE TABLE [athletes] (
  [athlete_id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
  [name] VARCHAR(75) NOT NULL COLLATE NOCASE, 
  [group_id] INTEGER, 
  [birth_date] DATE NOT NULL, 
  [height] INT DEFAULT 0, 
  [weight] INT DEFAULT 0);


CREATE TABLE [groups] (
  [groud_id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
  [group_name] NVARCHAR(75) COLLATE NOCASE);


CREATE TABLE [workouts] (
  [workout_id] INTEGER NOT NULL, 
  [athlete_id] INTEGER NOT NULL, 
  [date1] DATE NOT NULL, 
  [start_time] TIME NOT NULL, 
  [length_time] INT NOT NULL, 
  [type] NVARCHAR(40) COLLATE NOCASE, 
  [mark] int);
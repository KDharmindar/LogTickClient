import sqlite3
import datetime
conn = sqlite3.connect('TimeTrack.db')
 
c = conn.cursor()
# c.execute('''
#           CREATE TABLE Project
#           (id INTEGER PRIMARY KEY ASC, name varchar(250) NOT NULL)
#           ''')
# c.execute('''
#           CREATE TABLE ProjectTask
#           (id INTEGER PRIMARY KEY ASC, name varchar(250),
#            project_id INTEGER NOT NULL,
#            FOREIGN KEY(project_id) REFERENCES Project(id))
#           ''')
#  
# c.execute('''INSERT INTO Project VALUES(1, 'SMC')''')
# c.execute('''INSERT INTO Project VALUES(2, 'EFM')''')
# c.execute('''INSERT INTO Project VALUES(3, 'BFS Capital')''')
# c.execute('''INSERT INTO ProjectTask VALUES(1, 'SMC Task 1', 1)''')
# c.execute('''INSERT INTO ProjectTask VALUES(2, 'SMC Task 2', 1)''')
# c.execute('''INSERT INTO ProjectTask VALUES(3, 'SMC Task 3', 1)''')
# c.execute('''INSERT INTO ProjectTask VALUES(4, 'SMC Task 4', 1)''')
# c.execute('''INSERT INTO ProjectTask VALUES(5, 'SMC Task 5', 1)''')
# c.execute('''INSERT INTO ProjectTask VALUES(6, 'EFM Task 1', 2)''')
# c.execute('''INSERT INTO ProjectTask VALUES(7, 'EFM Task 2', 2)''')
# c.execute('''INSERT INTO ProjectTask VALUES(8, 'EFM Task 3', 2)''')
# c.execute('''INSERT INTO ProjectTask VALUES(9, 'EFM Task 4', 2)''')
# c.execute('''INSERT INTO ProjectTask VALUES(10, 'BFS Task 1', 3)''')
# c.execute('''INSERT INTO ProjectTask VALUES(11, 'BFS Task 2', 3)''')
# c.execute('''INSERT INTO ProjectTask VALUES(12, 'BFS Task 3', 3)''')
# c.execute('''INSERT INTO ProjectTask VALUES(13, 'BFS Task 4', 3)''')
# c.execute('''INSERT INTO ProjectTask VALUES(14, 'BFS Task 3', 3)''')
# c.execute('''INSERT INTO ProjectTask VALUES(15, 'BFS Task 4', 3)''')

 
 
 
 datetime.datetime.date("2-oct-2017")

 
 
 
conn.commit()
conn.close()

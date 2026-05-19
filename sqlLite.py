import sqlite3
conn = sqlite3.connect('orgdb.sqlite')
curr = conn.cursor()
curr.execute('DROP TABLE IF EXISTS Counts')
curr.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    org = email.split('@')[1]
    curr.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row = curr.fetchone()
    if row is None:
        curr.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        curr.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
conn.commit()
sqlStr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
totalCount = 0
for row in curr.execute(sqlStr):
    totalCount += row[1]
    print(str(row[0]), row[1])
print(totalCount)
conn.close()
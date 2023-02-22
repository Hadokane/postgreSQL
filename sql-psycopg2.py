import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database (set/list)
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
# cursor.execute('select * from "Artist"')

# Query 2 - select only the "Name" from the "Artist" table
# cursor.execute('select "Name" from "Artist"')

# Query 3 - select only "Queen" from the "Artist" table
# cursor.execute('select * from "Artist" where "Name" = %s', ["Queen"])

# Query 4 - select only "ArtistID" #51 from the "Artist" table
# cursor.execute('select * from "Artist" where "ArtistId" = %s', [51])

# Query 5 - select only "ArtistID" #51 from the "Album" table
# cursor.execute('select * from "Album" where "ArtistId" = %s', [51])

# Query 6 - select all tracks where the composer is "Queen"
# cursor.execute('select * from "Track" where "Composer" = %s', ["Queen"])

# Query 7 - select all tracks where the composer is "Red Hot Chili Peppers"
cursor.execute(
    'select * from "Track" where "Composer" = %s', ["Red Hot Chili Peppers"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)

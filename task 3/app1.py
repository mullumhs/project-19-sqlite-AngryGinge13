import sqlite3

# Create a connection to a new database (or connect to an existing one)
conn = sqlite3.connect('movies.db')
# Create a cursor object
cursor = conn.cursor()

# Create the movies table

# Create the movies table

# Select all movies


movies = [

    ('The Shawshank Redemption', 'Frank Darabont', 1999, 9.3),

    ('Inception', 'Christopher Nolan', 2010, 8.8),

    ('The', 'Penaldo', 1999, 8.7),

    ('Interstellar', 'Christopher Nolan', 2014, 8.6)



]

cursor.executemany('''

INSERT INTO movies (title, director, year, rating)

VALUES (?, ?, ?, ?)

''', movies)



cursor.execute('SELECT * FROM movies')
all_movies = cursor.fetchall()
print("All movies:")
for movie in all_movies:
    print(movie)


cursor.execute('SELECT title, year FROM movies WHERE year > 2000')
recent_movies = cursor.fetchall()
print("\nMovies after 2000:")
for movie in recent_movies:
    print(f"{movie[0]} ({movie[1]})")



# Don't forget to close the connection when you're done!
conn.commit()
conn.close()
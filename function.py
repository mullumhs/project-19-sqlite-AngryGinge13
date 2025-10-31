import sqlite3



# Create a connection to a new database (or connect to an existing one)
conn = sqlite3.connect('movies.db')
# Create a cursor object
cursor = conn.cursor()



def select():
    cursor.execute('SELECT * FROM movies')
    all_movies = cursor.fetchall()
    print("All movies:")
    for movie in all_movies:
        print(movie)

def aftertwothousand():
    cursor.execute('SELECT title, year FROM movies WHERE year > 2000')
    recent_movies = cursor.fetchall()
    print("\nMovies after 2000:")
    for movie in recent_movies:
        print(f"{movie[0]} ({movie[1]})")
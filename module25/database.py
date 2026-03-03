import sqlite3
from models import Movie , MovieCreate

def create_connection():
    """Create a database connection"""
    connection = sqlite3.connect("movie.db")
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    """Creates tables if they dont exist"""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
    Create Table IF DONT EXIST movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    director TEXT NOT NULL)      
    """)
    connection.commit()
    connection.close()


def create_movie(movie: MovieCreate) -> int:
    """
    ADDS a new movie to the database
    :param movie:
    Args:
    movie(MovieCreate)
    Return:
    int: The id of the new created movie
    :return:
    """
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO movies (title , Director) Values(?,?)" , (movie.title , movie.director))
    connection.commit()
    movie_id = cursor.lastrowid
    connection.close()
    return movie_id


def read_movie():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * from movies")
    rows = cursor.fetchall()
    connection.close()
    movies = [Movie(id=row[0] , title=row[1], director=row[2]) for row in rows]
    return movies

def read_movie(movie_id , int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("Select * from movies where id = ?", (movie_id,) )
    row = cursor.fetchone()
    connection.close()
    if row is None:
        return None
    movies = [Movie(id=row[0], title=row[1], director=row[2])]


def update_movie():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE movies SET title =? , director = ? Where id=?", (movie.title, movie.director, movie_id))
    connection.commit()
    updated = cursor.rowcount
    connection.close()
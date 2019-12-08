# Psycopg2 basics

Psycopg is a very popular PostgreSQL database adapter for the Python programming language. It's full documentation can be seen [here](https://pypi.org/project/psycopg2/).

The function `connect()` creates a new database session and returns a new connection instance.
```python
import psycopg2

conn = psycopg2.connect(
    database="appstore_games",
    host="localhost",
    user="postgres_user",
    password="12345"
)
```

Cursors allows Python code to execute PostgreSQL command in a database session.
```python
curr = conn.cursor()
```

Tables can be created with the cursor.
```python
curr.execute("""CREATE TABLE members (
                    id serial PRIMARY KEY,
                    firstname varchar(32),
                    lastname varchar(32),
                    birthdate date
                )
            """)
```

It's also possible to remove a table.
```python
curr.execute("DROP TABLE members")
```

To make changes persistent in the database, we need to commit (queries are called transactions). Finally we can close the  connection.
```python
conn.commit()
conn.close()
``` 

This gives the following full code.

```python
import psycopg2

if __name__ == "__main__":
    conn = psycopg2.connect(
        database="appstore_games",
        host="localhost",
        user="postgres_user",
        password="12345"
    )

    curr = conn.cursor()
    
    curr.execute("""CREATE TABLE members (
                    id serial PRIMARY KEY,
                    firstname varchar(32),
                    lastname varchar(32),
                    birthdate date
                )
    """)
    
    conn.commit()
    conn.close()
```

## Inserting data
Data can be inserted into a table with the following synthax.
```python
curr.execute("""
            INSERT INTO members(firstname, lastname, birthdate) VALUES
            ('Eric', 'Clapton', '1945-13-30'),
            ('Joe', 'Bonamassa', '1977-05-08')
""")
```
## Delete data
Data can alo be deleted.  
```python
curr.execute("""DELETE FROM members 
                WHERE lastname LIKE 'Clapton'
""")
```

## Showing table content
We must use the `fetchall` function to gather all the result in a list of tuples.
```python
...
curr.execute("""SELECT * FROM members""")
response = curr.fetchall()
for row in response:
    print(row)
conn.close()
```
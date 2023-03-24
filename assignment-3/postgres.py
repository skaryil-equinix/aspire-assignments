import psycopg2

# connect to the PostgreSQL database
conn = psycopg2.connect(database="postgres") #, user="your_username", password="your_password", host="your_host")# port="your_port")
cur = conn.cursor()


table_name = "employees"
cur.execute(f"SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = '{table_name}')")
table_exists = cur.fetchone()[0]

# if the table exists, drop it
if table_exists:
    cur.execute(f"DROP TABLE {table_name}")
    # commit the changes
    conn.commit()

table_name = "departments"
cur.execute(f"SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = '{table_name}')")
table_exists = cur.fetchone()[0]


# if the table exists, drop it
if table_exists:
    cur.execute(f"DROP TABLE {table_name}")
    # commit the changes
    conn.commit()



table_name = "departments"

# create the departments table
cur.execute(f"""
CREATE TABLE {table_name} (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL

)
""")

# commit the changes
conn.commit()

table_name = "employees"

# create the employees table
cur.execute(f"""
CREATE TABLE {table_name} (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    department_id INTEGER NOT NULL REFERENCES departments(id)
)
""")

# commit the changes
conn.commit()

# define the SQL query to insert values into the table
sql = """
INSERT INTO departments (id, name)
VALUES (%s, %s)
"""

# define the values to insert into the table
values = [(100,"Computer"),
          (300,"BioTech"),
          (200,"Commerce")]

# execute the SQL query with the values
cur.executemany(sql, values)

# commit the changes
conn.commit()


# define the SQL query to insert values into the table
sql = """
INSERT INTO employees (id, first_name, last_name, email, department_id)
VALUES (%s, %s, %s, %s, %s)
"""

# define the values to insert into the table
values = [(1,"John", "Doe", "john.doe@example.com", 100),
          (2,"Jane", "Smith", "jane.smith@example.com", 200),
          (3,"Bob", "Johnson", "bob.johnson@example.com", 100)]

# execute the SQL query with the values
cur.executemany(sql, values)

# commit the changes
conn.commit()



# close the cursor and the database connection
cur.close()
conn.close()

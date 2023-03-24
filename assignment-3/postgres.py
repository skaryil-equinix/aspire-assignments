import psycopg2

class PostgresDB():


    def __init__(self) -> None:

        self.conn = psycopg2.connect(database="postgres") #, user="your_username", password="your_password", host="your_host")# port="your_port")
        self.cur = self.conn.cursor()

    def create_table(self, table_name, columns):

        # define the SQL query to create the table
        sql = f"CREATE TABLE {table_name} ({', '.join([f'{column[0]} {column[1]}' for column in columns])})"

        # execute the SQL query to create the table
        self.cur.execute(sql)

        # commit the changes
        self.conn.commit()


    # def create_table(self,table_name, query):
        
    #     self.cur.execute(f"SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = '{table_name}')")
    #     table_exists = self.cur.fetchone()[0]

    #     if not table_exists:
    #         # # create the departments table
    #         # self.cur.execute(f"""
    #         # CREATE TABLE {table_name} (
    #         #     id SERIAL PRIMARY KEY,
    #         #     name VARCHAR(50) NOT NULL
    #         # )
    #         # """)
    #         self.cur.execute(query)
    #         self.conn.commit()

    def insert_table(self, table_name, values):

        sql = f"INSERT INTO TABLE {table_name} VALUES ({', '.join([val for val in values])})"

        # execute the SQL query to create the table
        self.cur.execute(sql)

        # commit the changes
        self.conn.commit()


    def drop_table(self, table_name):

        self.cur.execute(f"SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = '{table_name}')")
        table_exists = self.cur.fetchone()[0]

        if  table_exists:

            self.cur.execute(f"DROP TABLE {table_name}")
            self.conn.commit()


postgres = PostgresDB()

postgres.drop_table('departments')




dept_columns = [('id','SERIAL PRIMARY KEY'),
               ('name','VARCHAR(50) NOT NULL')]

# # create the departments table
# query =  f"""
#     CREATE TABLE {table_name} (
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(50) NOT NULL
#     )
#     """

emp_columns = [('id', 'SERIAL PRIMARY KEY'),
    ('first_name', 'VARCHAR(50) NOT NULL'),
    ('last_name', 'VARCHAR(50) NOT NULL'),
    ('email', 'VARCHAR(50) NOT NULL UNIQUE'),
    ('department_id', 'INTEGER NOT NULL REFERENCES departments(id)')]

# # create the employees table
# query = f"""
# CREATE TABLE {table_name} (
#     id SERIAL PRIMARY KEY,
#     first_name VARCHAR(50) NOT NULL,
#     last_name VARCHAR(50) NOT NULL,
#     email VARCHAR(50) NOT NULL UNIQUE,
#     department_id INTEGER NOT NULL REFERENCES departments(id)
# )
# """

# values = [(100,"Computer"),
#           (300,"BioTech"),
#           (200,"Commerce")]

# # define the SQL query to insert values into the table
# sql = """
# INSERT INTO departments (id, name)
# VALUES (%s, %s)
# """

# define the values to insert into the table
values = [(100,"Computer"),
          (300,"BioTech"),
          (200,"Commerce")]

# define the values to insert into the table
values = [(1,"John", "Doe", "john.doe@example.com", 100),
          (2,"Jane", "Smith", "jane.smith@example.com", 200),
          (3,"Bob", "Johnson", "bob.johnson@example.com", 100)]

# # execute the SQL query with the values
# cur.executemany(sql, values)

# # commit the changes
# conn.commit()


# # define the SQL query to insert values into the table
# sql = """
# INSERT INTO employees (id, first_name, last_name, email, department_id)
# VALUES (%s, %s, %s, %s, %s)
# """

# # define the values to insert into the table
# values = [(1,"John", "Doe", "john.doe@example.com", 100),
#           (2,"Jane", "Smith", "jane.smith@example.com", 200),
#           (3,"Bob", "Johnson", "bob.johnson@example.com", 100)]

# # execute the SQL query with the values
# cur.executemany(sql, values)

# # commit the changes
# conn.commit()



# # close the cursor and the database connection
# cur.close()
# conn.close()

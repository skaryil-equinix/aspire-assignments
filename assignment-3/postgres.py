import psycopg2

class PostgresDB():

    # connect to the DB
    def __init__(self) -> None:

        self.conn = psycopg2.connect(database="postgres") #, user="your_username", password="your_password", host="your_host")# port="your_port")
        self.cur = self.conn.cursor()

    # create a table 
    def create_table(self, table_name, columns):

        # define the SQL query to create the table
        sql = f"CREATE TABLE {table_name} ({', '.join([f'{column[0]} {column[1]}' for column in columns])})"

        # execute the SQL query to create the table
        self.cur.execute(sql)

        # commit the changes
        self.conn.commit()


    # insert multiple rows into a table
    def insert_table(self, table_name, values):

        for vals in values:

            sql = f"INSERT INTO {table_name} VALUES ({', '.join(['%s'] * len(vals))})"
            print(sql)

            self.cur.execute(sql, tuple(vals))

            # commit the changes
            self.conn.commit()


    # drop a table if it exists
    def drop_table(self, table_name):

        self.cur.execute(f"SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = '{table_name}')")
        table_exists = self.cur.fetchone()[0]

        if table_exists:
            self.cur.execute(f"DROP TABLE {table_name}")
            self.conn.commit()
        else:
            print("Does not exist")


# Instantiating the Class object
postgres = PostgresDB()

# DROP the tables before execution
postgres.drop_table('employees')
postgres.drop_table('departments')


# CREATE the required tables
dept_columns = [('id','SERIAL PRIMARY KEY'),
               ('name','VARCHAR(50) NOT NULL')]
postgres.create_table('departments', dept_columns)


emp_columns = [('id', 'SERIAL PRIMARY KEY'),
    ('first_name', 'VARCHAR(50) NOT NULL'),
    ('last_name', 'VARCHAR(50) NOT NULL'),
    ('email', 'VARCHAR(50) NOT NULL UNIQUE'),
    ('department_id', 'INTEGER NOT NULL REFERENCES departments(id)')]
postgres.create_table('employees', emp_columns)


# INSERT values to the created tables
values = [(100,"Computer"),
          (300,"BioTech"),
          (200,"Commerce")]
postgres.insert_table('departments', values)


values = [(1,"John", "Doe", "john.doe@example.com", 100),
          (2,"Jane", "Smith", "jane.smith@example.com", 200),
          (3,"Bob", "Johnson", "bob.johnson@example.com", 100)]
postgres.insert_table('employees', values)

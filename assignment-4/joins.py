import psycopg2

class Joins():

    def __init__(self, src_table, tgt_table):

        self.conn = psycopg2.connect(database="postgres")
        self.cur = self.conn.cursor()
        self.source_table = src_table
        self.target_table = tgt_table

    def left_join(self, src_cols, tgt_cols, conditions):
        
        if len(src_cols)!=len(tgt_cols) or len(src_cols)!=len(conditions):
            print("No. of source columns and no. of target columns do not match in join condition")
            return
        
        query = f"\nSELECT * FROM {self.source_table} LEFT JOIN {self.target_table} ON ({' AND '.join([f'{self.source_table}.{src_cols[i]}{conditions[i]}{self.target_table}.{tgt_cols[i]}' for i in range(len(src_cols))])});"
        print(query)

        # execute the SQL query
        self.cur.execute(query)

        results = self.cur.fetchall()
        for row in results:
            print(row)


    def right_join(self, src_cols, tgt_cols, conditions):

        if len(src_cols)!=len(tgt_cols) or len(src_cols)!=len(conditions):
            print("No. of source columns and no. of target columns do not match in join condition")
            return
        
        query = f"\nSELECT * FROM {self.source_table} RIGHT JOIN {self.target_table} ON ({' AND '.join([f'{self.source_table}.{src_cols[i]}{conditions[i]}{self.target_table}.{tgt_cols[i]}' for i in range(len(src_cols))])});"
        print(query)

        # execute the SQL query
        self.cur.execute(query)

        results = self.cur.fetchall()
        for row in results:
            print(row)

    def inner_join(self, src_cols, tgt_cols, conditions):

        if len(src_cols)!=len(tgt_cols) or len(src_cols)!=len(conditions):
            print("No. of source columns and no. of target columns do not match in join condition")
            return
        
        query = f"\nSELECT * FROM {self.source_table} INNER JOIN {self.target_table} ON ({' AND '.join([f'{self.source_table}.{src_cols[i]}{conditions[i]}{self.target_table}.{tgt_cols[i]}' for i in range(len(src_cols))])});"
        print(query)

        # execute the SQL query
        self.cur.execute(query)

        results = self.cur.fetchall()
        for row in results:
            print(row)

    def full_outer_join(self, src_cols, tgt_cols, conditions):

        if len(src_cols)!=len(tgt_cols) or len(src_cols)!=len(conditions):
            print("No. of source columns and no. of target columns do not match in join condition")
            return
        
        query = f"\nSELECT * FROM {self.source_table} FULL OUTER JOIN {self.target_table} ON ({' AND '.join([f'{self.source_table}.{src_cols[i]}{conditions[i]}{self.target_table}.{tgt_cols[i]}' for i in range(len(src_cols))])});"
        print(query)

        # execute the SQL query
        self.cur.execute(query)

        results = self.cur.fetchall()
        for row in results:
            print(row)


joins = Joins('source', 'target')

src_cols = ['id', 'name']
tgt_cols = ['id', 'name']
conditions = ['=', '=']

joins.full_outer_join(src_cols, tgt_cols, conditions)

joins.left_join(src_cols, tgt_cols, conditions)

joins.left_join(src_cols, tgt_cols, conditions)

joins.inner_join(src_cols, tgt_cols, conditions)

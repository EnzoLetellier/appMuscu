import sys

sys.path.insert(1, 'C:\\Users\\enzol\\appMuscu\\perfsmuscu\\src\\perfsmuscu\\packages')

import psycopg2



conn = psycopg2.connect(
            host = 'localhost',
            database = 'muscu',
            user = 'postgres',
            password = 'enzo',
            client_encoding='UTF8'
        )

cursor = conn.cursor() 
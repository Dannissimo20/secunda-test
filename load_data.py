import os
import psycopg2

def execute_sql_file(file_path):
    """Выполняет SQL команды из файла"""
    database_url = os.getenv("DSN")
    
    conn = psycopg2.connect(database_url)
    cursor = conn.cursor()
    
    with open(file_path, 'r') as f:
        sql_commands = f.read()
        cursor.execute(sql_commands)
    
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    execute_sql_file("/app/init-data.sql")
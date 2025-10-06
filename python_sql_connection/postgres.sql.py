import psycopg2

def connect_to_postgres():
    try:
        connection = psycopg2.connect(
            host="jdbc:postgresql://localhost:5432/rohitkushah",
            database="rohitkushah",
            user="rohitkushah",
            password="Palak@1999"
        )
        print("Connection successful")
        return connection
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

if __name__ == "__main__":
    conn = connect_to_postgres()
    if conn:
        conn.close()
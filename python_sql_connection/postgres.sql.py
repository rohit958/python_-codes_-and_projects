# ...existing code...
import psycopg2
from urllib.parse import quote_plus

if __name__ == "__main__":
    user = "rohitkushah"
    password = quote_plus("Palak@1999")  # '@' becomes '%40'
    host = "localhost"
    port = 5432
    dbname = "rohitkushah"

    dsn = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
    with psycopg2.connect(dsn) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            row = cur.fetchone()
            if row:
                print(row[0])
# ...existing code...
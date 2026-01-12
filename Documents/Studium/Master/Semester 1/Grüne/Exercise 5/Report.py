import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------
# 1. Verbindung zur PostgreSQL-Datenbank
# -------------------------------------------------
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",      # ggf. anpassen
    user="postgres",          # ggf. anpassen
    password="3fBe4AdG!PSQL"       # ggf. anpassen
)

# -------------------------------------------------
# 2. SQL-Abfrage (Report 1)
# -------------------------------------------------

cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM vw_rental_analysis")
print(f"Total records: {cursor.fetchone()[0]}")
query = """
SELECT film_category,
        COUNT(*) AS total_rentals,
        SUM(rental_amount) AS total_revenue
FROM vw_rental_analysis
GROUP BY film_category
ORDER BY total_rentals DESC;
"""

df = pd.read_sql(query, conn)
conn.close()

# -------------------------------------------------
# 3. Balkendiagramm erstellen
# -------------------------------------------------
plt.figure(figsize=(10, 6))
plt.bar(df["film_category"], df["total_rentals"])
plt.xlabel("Film Category")
plt.ylabel("Total Number of Rentals")
plt.title("Rentals by Film Category")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# -------------------------------------------------
# 4. Chart anzeigen
# -------------------------------------------------
plt.show()
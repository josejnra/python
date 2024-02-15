import duckdb

if __name__ == "__main__":
    try:
        conn = duckdb.connect("local.db")

        conn.sql("CREATE TABLE IF NOT EXISTS test (i INTEGER)")
        conn.sql("INSERT INTO test VALUES (42)")
        conn.table("test").show()
        conn.close()
    finally:
        # Note: connections also closed implicitly when they go out of scope
        conn.close()

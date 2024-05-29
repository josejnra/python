import duckdb

if __name__ == "__main__":
    # Conecta ao banco de dados DuckDB
    con = duckdb.connect(':memory:')

    parquet_path = '/workspaces/files/*.parquet'
    df = con.read_parquet(parquet_path)

    # Cria uma tabela no banco de dados DuckDB a partir do arquivo Parquet
    # con.sql(f"CREATE TABLE card_requests AS SELECT * FROM parquet_scan('{parquet_path}')")

    # Executa uma consulta SQL na tabela criada
    # print(con.sql('SELECT * FROM card_requests'))

    rows, cols = df.shape
    print(rows, cols)

    con.sql("SELECT * FROM df limit 5").show()

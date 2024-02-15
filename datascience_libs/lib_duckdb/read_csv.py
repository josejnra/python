import duckdb
from duckdb import DuckDBPyRelation


def read_csv(path: str) -> DuckDBPyRelation:
    return duckdb.read_csv(path, header=False, delimiter=",")


if __name__ == "__main__":
    df = read_csv("/workspaces/python/python-basics/arquivos_texto/500amostras.csv")
    df.show()

    rows, cols = df.shape
    print(rows, cols)

    duckdb.sql("SELECT * FROM df limit 5").show()
    duckdb.sql("SELECT sum(column0) FROM df").show()

    duckdb.sql("SELECT 42").fetchall()  # Python objects
    duckdb.sql("SELECT 42").df()  # Pandas DataFrame
    duckdb.sql("SELECT 42").pl()  # Polars DataFrame
    duckdb.sql("SELECT 42").arrow()  # Arrow Table
    duckdb.sql("SELECT 42").fetchnumpy()  # NumPy Arrays

    duckdb.sql("SELECT * FROM df").write_parquet("out.parquet", compression="snappy")

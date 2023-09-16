from typing import Any, Dict, Iterable, List
import itertools

import dask.dataframe as dd
from dask.dataframe.core import DataFrame

PARQUET_FOLDER_PATH = "my_folder"


def dataframe_from_dict() -> DataFrame:
    """creates a Dask DataFrame from a Python Dictionary"""
    data = {
        "name": ["jose", "lucy", "max"],
        "age": [23, 25, 19]
    }

    return dd.from_dict(data, npartitions=2)


def parquet_from_dataframe(dataframe: DataFrame, path: str = PARQUET_FOLDER_PATH) -> None:
    """write dataframe as parquet"""
    dataframe.to_parquet(path=path, engine="fastparquet", overwrite=True, compression="snappy", write_index=False)


def read_from_parquet(path: str) -> DataFrame:
    """read parquet files"""
    return dd.read_parquet(path, engine="pyarrow-dataset")


def list_from_dataframe(df: DataFrame) -> Iterable[Dict[str, List[Any]]]:
    """Records from a dataframe"""
    all_partitions = list(df.map_partitions(lambda x: x.to_dict(orient="records")))
    return itertools.chain.from_iterable(all_partitions)


if __name__ == "__main__":
    df = dataframe_from_dict()

    print(df.compute())

    parquet_from_dataframe(df)

    df = read_from_parquet(f"{PARQUET_FOLDER_PATH}/*.parquet")

    print(list(list_from_dataframe(df)))

    print(len(df.index))
    print(df.dtypes)

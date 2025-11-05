import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq


filename_ = "data.data.parquet"


def save_pq(df: pd.DataFrame, filename_) -> None:
    df.to_parquet(filename_, index=False)


def read_parquet(filename_) -> pd.DataFrame:
    df2 = pd.read_parquet(filename_).set_index("index")
    return df2


def save2(df: pd.DataFrame, filename_) -> None:
    # Convert pandas to arrow table
    table = pa.Table.from_pandas(df)
    pq.write_table(table, filename_)

import pandas as pd


def load_dataset(path: str) -> pd.DataFrame:
    """Load the dataset and return a pandas DataFrame."""
    df = pd.read_csv(path)
    return df


def inspect_data(df: pd.DataFrame) -> None:
    print("Dataset preview:")
    print(df.head(), "\n")
    print("Columns:", list(df.columns))
    print("Row count:", len(df), "\n")


def filter_and_sort(df: pd.DataFrame) -> pd.DataFrame:
    """Filter items by category and sort by price."""
    filtered = df[df["category"] == "Widgets"]
    sorted_df = filtered.sort_values(by="price")
    return sorted_df


def aggregate_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Group by category and compute summary statistics."""
    summary = df.groupby("category").agg(
        total_quantity=("quantity", "sum"),
        average_price=("price", "mean"),
        item_count=("id", "count"),
    )
    return summary.reset_index()


def main() -> None:
    df = load_dataset("data.csv")
    inspect_data(df)

    print("Filtered and sorted records:")
    sorted_df = filter_and_sort(df)
    print(sorted_df, "\n")

    print("Aggregated summary:")
    summary = aggregate_summary(df)
    print(summary)


if __name__ == "__main__":
    main()

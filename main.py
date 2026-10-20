import pandas as pd


# load the CSV data into a DataFrame
df = pd.read_csv("sales.csv")

def main():

    print("Hello from working-with-data!")
    # Preview the first few rows of the DataFrame
    print("Initial data:\n", df.head())

    # # Add a new column for total order value
    df["total_value"] = df["quantity"] * df["price"]
    # Save the updated DataFrame to a new CSV file
    df.to_csv("sales_with_total_value.csv", index=False)
    print("Data with total order value:\n", df.head())

    # Reload the CSV to confirm changes if saved in the original csv file
# df2 = pd.read_csv('sales_data.csv')

# Preview the updated data
# print("Updated data:\n", df2.head())


if __name__ == "__main__":
    main()

import pandas as pd

# Load the JSON data into a DataFrame
df = pd.read_json("user_data.json")


def main():
    print("Original data:")
    print(df.head())

    # Add a new column 'is_active' with all values set to True
    df["is_active"] = True
    print("Data with 'is_active' column:\n", df.head())

    # Save the updated DataFrame to a new JSON file
    df.to_json("user_data_with_is_active.json", orient="records", indent=2) 
    print("Updated data saved to 'user_data_with_is_active.json'")
    print("Final data:")
    print(df.head())
    print("Script finished.")
    

if __name__ == "__main__":
    main()



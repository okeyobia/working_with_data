import requests

# Define the API URL to interact with
API_URL = "https://fakestoreapi.com/products/1"  

def main():
    print("Script started.")
    # Here you can add code to interact with the API
    
    # Send a GET request to the API
    response = requests.get(API_URL)

    # Check if the request was successful
    if response.status_code == 200:
        # Pass the JSON response 
        print("API response received successfully:")
        print(response.json())
    else:
        print(f"Failed to fetch data from API. Status code: {response.status_code}")

    print("Script finished.")

if __name__ == "__main__":
    main()
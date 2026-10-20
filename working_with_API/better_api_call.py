import requests

API_URL = "https://fakestoreapi.com/products/1"  # Define the API URL to interact with

def main():
   try:
       response = requests.get(API_URL, timeout=10)  # Set a timeout for the request
       response.raise_for_status()  # Raise an exception for HTTP errors
       print("API response received successfully:")
       data = response.json()
       title = data.get("title", "No title found") # Extract the title from the JSON response
       print(f"Product title: {title}")
   except requests.exceptions.RequestException as e:
       # Catches ConnectionError, Timeout, HTTPError, etc.
       print(f"Failed to fetch data from API: {e}")

if __name__ == "__main__":
    main()
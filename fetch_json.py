import requests

# URLs of the JSON files
url1 = "https://github.com/mitthu786/tvepg/raw/main/tataplay/tsdataWc.json"
url2 = "https://github.com/mitthu786/tvepg/raw/main/tataplay/tsdata.json"

# Make GET requests to fetch the JSON data
response1 = requests.get(url1)
response2 = requests.get(url2)

# Check if requests were successful (status code 200)
if response1.status_code == 200 and response2.status_code == 200:
    # Parse JSON data
    json_data1 = response1.json()
    json_data2 = response2.json()

    # Now you can work with json_data1 and json_data2
    # For example, print the content
    print("Content of tsdataWc.json:")
    print(json_data1)
    print("\nContent of tsdata.json:")
    print(json_data2)
else:
    print("Failed to fetch JSON data. Check the URLs or your internet connection.")

import requests
import time

# Create a list to store all the JSON responses
json_responses = []

# Start recording the execution time
start_time = time.time()

for comic_id in range(1, 201):
    # Construct the URL for the JSON file
    url = f"https://xkcd.com/{comic_id}/info.0.json"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Append the JSON response to the list
        json_responses.append(response.json())
    else:
        print(f"Failed to download JSON for comic {comic_id}")

# Save all the JSON responses in a single file
file_name = "all_comics.json"
with open(file_name, "w") as file:
    file.write(str(json_responses))

# Calculate the execution time
execution_time = time.time() - start_time

print(f"All JSON responses saved in {file_name}")
print(f"Execution time: {execution_time} seconds")

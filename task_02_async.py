import asyncio
import aiohttp
import time

async def download_data(session, data_id):
    # Construct the URL for downloading the data
    url = f"https://xkcd.com/{data_id}/info.0.json"

    # Send a GET request to the URL
    async with session.get(url) as response:
        if response.status == 200:
            # Retrieve the data from the response
            data = await response.json()
            return data
        else:
            print(response.status)
            print(f"Failed to download data with ID {data_id}")
            return None

async def main():
    # Create a list to store all the tasks
    tasks = []
    async with aiohttp.ClientSession() as session:
        for data_id in range(1, 201):
            # Create a task for each data download
            task = asyncio.create_task(download_data(session, data_id))
            tasks.append(task)

        # Wait for all the tasks to complete
        downloaded_data = await asyncio.gather(*tasks)

    # Save all the downloaded data in a single file
    file_name = "all_data.json"
    with open(file_name, "w") as file:
        file.write(str(downloaded_data))

    print(f"All data saved in {file_name}")

# Record the execution time
start_time = time.time()

# Run the asyncio event loop
asyncio.run(main())

# Calculate the execution time
execution_time = time.time() - start_time
print(f"Execution time: {execution_time} seconds")

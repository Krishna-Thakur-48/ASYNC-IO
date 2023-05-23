import asyncio
import time
import aiohttp

async def fetch_data(url):
    # Asynchronously fetch data from the specified URL
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    # Define a list of IDs for data retrieval
    id_list = [1, 2, 3]

    # Generate a list of coroutines for data retrieval
    coroutines = [fetch_data(f'https://example.com/api/data?id={id}') for id in id_list]

    # Record the current time before executing the coroutines
    start_time = time.time()

    # Schedule the coroutines to run concurrently using asyncio.gather
    await asyncio.gather(*coroutines)

    # Calculate the execution time by subtracting the start time from the current time
    execution_time = time.time() - start_time

    # Display the execution time
    print('Total Execution Time: {0}'.format(execution_time))

# Run the main coroutine
asyncio.run(main())

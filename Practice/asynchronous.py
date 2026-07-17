import asyncio
import time

async def fetch_data_async(db_id):
    print(f"Starting fetch from DB {db_id}..")

    # Use AWAIT so the event loop can switch to other tasks during this sleep
    await asyncio.sleep(2)
    print(f"Finished DB {db_id}!")
    return f"Data {db_id}"

async def main():
    start_time = time.time()

    #Schedules all three fetches to run concurrently
    results = await asyncio.gather(
        fetch_data_async(1),
        fetch_data_async(2),
        fetch_data_async(3)
    )

    end_time = time.time()
    print(f"Fetched results: {results}")
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

asyncio.run(main())

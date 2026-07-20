import asyncio
import time

async def fetch_data(user_id):
    print(f"Fetching data for User {user_id}")

    await asyncio.sleep(2)
    print(f"Received data for User {user_id}!")

async def main():
    start_time = time.time() 

    await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

asyncio.run(main())
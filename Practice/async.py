import aiohttp
import asyncio
import time 

start_time = time.time()

async def main():
    async with aiohttp.ClientSession() as session:
         for i in range(1,151):
            url = 'https://pokeapi.co/api/v2/pokemon/' + str(i)
            async with session.get(url) as resp:
                pokemon = await resp.json()
                print(pokemon['name'])


asyncio.run(main())
end_time = time.time()
print('Execution in second',(end_time-start_time)) 

# Execution in second 6.688 secs
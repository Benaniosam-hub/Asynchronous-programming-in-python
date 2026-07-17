import requests
import time 

start_time = time.time()

for i in range(1,151):
    url = 'https://pokeapi.co/api/v2/pokemon/' + str(i)
    resp = requests.get(url)
    pokemon = resp.json()
    print(pokemon['name'])

end_time = time.time()
print('Execution in second',(end_time-start_time)) 

# Execution in second 17.811 secs
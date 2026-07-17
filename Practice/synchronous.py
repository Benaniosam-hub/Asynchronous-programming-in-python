import time 

def fetch_data(db_id):
    print(f"Starting fetch from DB {db_id}...")
    time.sleep(2)
    print(f"Finished DB {db_id}!")
    return f"Data {db_id}"

def main():
    start_time = time.time()

    data1 = fetch_data(1)
    data2 = fetch_data(2)
    data3 = fetch_data(3)

    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

main()
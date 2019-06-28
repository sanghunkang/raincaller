from threading import Thread

def count_string(distribution, job):
    # Function to run on thread
    for c in job:
        if c not in distribution:
            distribution[c] = 1
        elif c in distribution:
            distribution[c] += 1

def threads():
    threads = []
    # for i, job in enumerate(jobs[:1]):
    for i, job in enumerate(jobs):
        thread = Thread(name=f"Job{i}", target=count_string, args=(distribution, job))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

def allocate_jobs():
    jobs = []
    jobs.append([2, int(ws.max_row/NUM_JOBS)])
    for i in range(1, NUM_JOBS):
        jobs.append([int(i*ws.max_row/NUM_JOBS), int((i+1)*ws.max_row/NUM_JOBS)])
    
    return jobs

def get_distribution():
    distribution = {}
    # Count an
    jobs = allocate_jobs()
    


    return distribution


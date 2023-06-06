import multiprocessing

#bind = "127.0.0.1:8000"  # Change the IP and port as needed
workers = multiprocessing.cpu_count() * 2 
worker_class = "gthread"  # For better concurrency with Django 3.0+
timeout = 120

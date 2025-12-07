from locust import HttpUser, task, between

from w5.fib import fibonacci

# https://docs.locust.io/en/stable/writing-a-locustfile.html#writing-a-locustfile
# https://docs.locust.io/en/stable/running-in-docker.html#running-in-docker
class FibonacciUser(HttpUser):
    # Tiempo de espera entre requests (2 a 5 segundos)
    wait_time = between(1, 5)

    @task
    def fib_task(self):
        # Llama al endpoint de Fibonacci con n=10
        self.client.get("/fib", params={"n": 10})

    @task
    def fib_cached_task(self):
        self.client.get("/fib-cached", params={"n": 15})
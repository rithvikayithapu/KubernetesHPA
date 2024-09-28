from locust import HttpUser, task, between

class HelloServiceUser(HttpUser):
    wait_time = between(1, 5) # Wait time between requests
    
    @task
    def get_hello(self):
        headers = {'Content-Type': 'text/html'}
        self.client.get("/", headers=headers)
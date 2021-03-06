import os
import random
from uuid import uuid4

from locust import HttpLocust, TaskSet, task


CAT_FRACTION = os.getenv("CAT_FRACTION", 0.75)


class VotingTaskSet(TaskSet):

    @task
    def vote(self):
        voter_id = uuid4().hex
        vote = "a" if (random.uniform(0, 1) < CAT_FRACTION) else "b"
        self.client.post("/",
                         cookies={"voter_id": voter_id},
                         data={"vote": vote})


class VotingLocust(HttpLocust):
    task_set = VotingTaskSet
    min_wait = 5
    max_wait = 10

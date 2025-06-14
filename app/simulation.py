import random
from app.user import GymUser
import simpy

class SimulationRunner:
    def __init__(self, config):
        from app.environment import GymEnvironment
        self.env_wrapper = GymEnvironment(config)
        self.config = config
        #self.exercise = simpy.Resource(self.env_wrapper.env, capacity=config["num_exercises"]) // bez strategii

        if config["strategy"] == "FIFO":
            self.exercise = simpy.Resource(self.env_wrapper.env, capacity=config["num_exercises"])
        elif config["strategy"] == "priority":
            self.exercise = simpy.PriorityResource(self.env_wrapper.env, capacity=config["num_exercises"])
        else:
            self.exercise = simpy.Resource(self.env_wrapper.env, capacity=config["num_exercises"])

        self.env_wrapper.stats = {"all": 0, "trained": 0, "left": 0, "max_users": 0, "current_users": 0}

    def user_arrivals(self):
        i = 1
        while (self.env_wrapper.env.now < self.config["day_minutes"] - max(self.config["training_duration"])):
            time_of_day = self.env_wrapper.env.now
            if time_of_day < 720:
                interval = self.config["arrival_rate"]["morning"]
            elif time_of_day < 1020:
                interval = self.config["arrival_rate"]["afternoon"]
            else:
                interval = self.config["arrival_rate"]["evening"]

            yield self.env_wrapper.env.timeout(random.expovariate(1.0 / interval))
            user = GymUser(self.env_wrapper, f"User{i}", self.exercise, self.config)
            self.env_wrapper.env.process(user.workout())
            i += 1

    def run(self):
        self.env_wrapper.env.process(self.user_arrivals())
        self.env_wrapper.run(until=self.config["day_minutes"])
        print("\n⏱ KONIEC DNIA – siłownia zamknięta!")

        print(f"Wszyscy użytkownicy siłowni: {self.env_wrapper.stats['all']}")
        print(f"Użytkownicy, którzy ukończyli trening: {self.env_wrapper.stats['trained']}\nUżytkownicy, którzy zrezygnowali z powodu oczekiwania na ćwiczenie: {self.env_wrapper.stats['left']}\nLiczba użytkowników siłowni podczas największego ruchu: {self.env_wrapper.stats['max_users']}")
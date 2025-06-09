import random

class GymUser:
    def __init__(self, env_wrapper, name, exercise_resource, config):
        self.env = env_wrapper.env
        self.stats = env_wrapper.stats
        self.name = name
        self.exercise = exercise_resource
        self.strategy = config["strategy"] #strategia do zaimplementowania w workout
        self.config = config
        # Wylosuj długość treningu od razu, aby określić priorytet
        self.training_duration = random.randint(*self.config["training_duration"])
        self.priority = self.training_duration if self.strategy == "priority" else None

    def workout(self):
        arrival_time = self.env.now
        self.stats["current_users"] += 1

        if self.strategy == "priority":
            req = self.exercise.request(priority=self.priority)
        else:
            req = self.exercise.request()


        with req as request:
            result = yield request | self.env.timeout(self.config["max_wait_time"])

            if req in result:
                if self.stats["current_users"] > self.stats["max_users"]:
                    self.stats["max_users"] = self.stats["current_users"]

                print(f"{self.name} started workout at {self.format_time(arrival_time)}")
                yield self.env.timeout(self.training_duration)

                print(f"{self.name} finished at {self.format_time(self.env.now)} and worked out {self.training_duration} minutes")
                self.stats["trained"] += 1
            else:
                print(f"{self.name} left (waited too long) at {self.format_time(self.env.now)}")
                self.stats["left"] += 1

        self.stats["current_users"] -= 1

    @staticmethod
    def format_time(time):
        h = int((time + 360) // 60)
        m = int((time + 360) % 60)
        return f"{h:02d}:{m:02d}"


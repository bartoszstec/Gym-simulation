CONFIG = {
    "num_exercises": 10,
    "day_minutes": 960,
    "arrival_rate": {
        "morning": 20,   # np. co 2 minuty użytkownik
        "afternoon": 5,
        "evening": 3,
    },
    "training_duration": (30, 90),  # min i max minut
    "max_wait_time": 15,  # po ilu minutach rezygnują
    "strategy": "FIFO"  # lub "priority", "reject_long_wait"
}
CONFIG = {
    "num_exercises": 10,    # liczba stanowisk ćwiczeniowych
    "day_minutes": 960,     # czas trwania symulacji
    "arrival_rate": {       # częstotliwość przyjeżdżania w zależności od pory dnia
        "morning": 20,
        "afternoon": 5,
        "evening": 2,
    },
    "training_duration": (30, 90),  # minimalna i maksymalna długość treningu
    "max_wait_time": 15,            # czas, po którym użytkownicy rezygnują z ćwiczeń w minutach
    "strategy": "FIFO"              # strategia kolejkowania "FIFO" lub "priority"
}
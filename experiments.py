# experiments.py
import csv
from app.config import CONFIG
from app.simulation import SimulationRunner


def run_experiments(num_runs=30, output_file="results.csv"):
    results = []

    for i in range(num_runs):
        print(f"\n▶️ Symulacja nr {i + 1}")
        sim = SimulationRunner(config=CONFIG)
        sim.run()

        stats = sim.env_wrapper.stats
        filtered_stats = {
            "run": i + 1,
            "all": stats.get("all", 0),
            "trained": stats.get("trained", 0),
            "left": stats.get("left", 0),
            "max_users": stats.get("max_users", 0)
        }

        results.append(filtered_stats)

    # Zapisz wyniki do pliku CSV
    with open(output_file, mode="w", newline="") as f:
        fieldnames = ["run", "all", "trained", "left", "max_users"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"\n📄 Wyniki zapisane do pliku: {output_file}")

run_experiments()
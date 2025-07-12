# experiments.py
import csv
from app.config import CONFIG
from app.simulation import SimulationRunner
import matplotlib.pyplot as plt
import pandas as pd


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

# Wczytaj dane z pliku CSV
df = pd.read_csv("results.csv")

# Utwórz figurę i osie
fig, ax = plt.subplots(figsize=(16, 6))
ax.set_xlim(1, df["run"].max()) #limity wykresu (od 1 dnia do końca danych)

# Wykresy liniowe dla każdej kategorii
ax.plot(df["run"], df["all"], label="liczba wszystkich użytkowników",color='blue', linestyle='solid')
ax.plot(df["run"], df["trained"], label="liczba użytkowników, którzy ukończyli trening", color='green')
ax.plot(df["run"], df["left"], label="liczba użytkowników, którzy opuścili trening", color='orange')
ax.plot(df["run"], df["max_users"], label="liczba użytkowników przy największym zatłoczeniu", color='red')
ax.axhline(
    CONFIG["num_exercises"],
    color="black",
    linestyle="--",
    linewidth=1,
    label=f"stanowiska ćwiczeniowe ({CONFIG['num_exercises']})"
)
strategy_text = f"Strategia kolejkowania: {CONFIG['strategy']}"
ax.text(
    0.98, 0.95,
    strategy_text,
    transform=ax.transAxes,
    fontsize=12,
    ha='right',
    va='top',
    bbox=dict(facecolor='white', alpha=0.7, edgecolor='gray')
)

# Etykiety i tytuł
ax.set_xlabel("Dzień")
ax.set_ylabel("Osoby")
ax.set_title("Wykres zatłoczenia siłowni w zależności od dnia")

# Legenda i siatka
ax.legend()
ax.grid(True)

# Optymalizacja układu i wyświetlenie
fig.tight_layout()
plt.show()
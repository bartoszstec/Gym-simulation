from app.config import CONFIG
from app.simulation import SimulationRunner

if __name__ == "__main__":
    sim = SimulationRunner(config=CONFIG)
    sim.run()
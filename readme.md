# Gym-simulation
Simulation of traffic movement on gym depending on time.

# Description
The simulation aims to represent the gym's operation in a realistic way, taking into account the dynamics of the influx of customers, limited hardware resources (training stations) and various queue management strategies. The model was implemented in **Python** using the **SimPy** library, which allows for conducting discrete event simulations in time.

The simulation time covers the entire day of the gym's operation - from opening to closing (by default 16 hours, i.e. 960 minutes).

## Output Graph (Basic Configuration)
![Graph from running basic configuration simmulation](assets/wykres.jpg)

## Run simmulation
To run simmulation i suggest opening Visual Studio Code, then PowerShell and creating new virtual environment in main folder of application:
```bash
python -m venv venv
```
then activate that environment and install needed packages from file named: `requirements.txt`.
```bash
venv\Scripts\activate  # On Windows  
source venv/bin/activate  # On macOS/Linux  
pip install -r requirements.txt
```
Finally to run app type in Powershell:
1. Run simmulation once:
```bash
python main.py
```
2. Run simmulation multiple times and present graph:
```bash
python experiments.py
```
## Configuration
You can change configuration of simmulation to your liking by changing parameters in file named: `app\config.py`.
## 🔧 Basic configuration present as below:
```python
CONFIG = {
    "num_exercises": 11,
    "day_minutes": 960,
    "arrival_rate": {
        "morning": 20,
        "afternoon": 5,
        "evening": 2,
    },
    "training_duration": (30, 90),
    "max_wait_time": 15,
    "strategy": "priority"
}
```

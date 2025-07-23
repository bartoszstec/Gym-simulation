# Gym-simulation
Simulation of traffic movement on gym depending on time.

## Description
The simulation aims to represent the gym's operation in a realistic way, taking into account the dynamics of the influx of customers, limited hardware resources (training stations) and various queue management strategies. The model was implemented in **Python** using the **SimPy** library, which allows for conducting discrete event simulations in time.

The simulation time covers the entire day of the gym's operation - from opening to closing (by default 16 hours, i.e. 960 minutes).

## Run simmulation
TO run simmulation i suggest creating new virtual environment in main folder of application:
```bash
python -m venv venv
```
then activate that environment and install needed packages from file named: `requirements.txt`.
```bash
venv\Scripts\activate  # On Windows  
source venv/bin/activate  # On macOS/Linux  
pip install -r requirements.txt
```

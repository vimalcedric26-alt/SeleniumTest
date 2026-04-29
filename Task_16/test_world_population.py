import time
from Task_16.population_clock import WorldPopulation
import pytest

def test_live_world_population(setup):
    world_population = WorldPopulation(setup)
    world_population.start()
    print("\nPress CTRL + C to stop monitoring...\n")
    try:
        while True:
            population = world_population.get_world_population()
            print(f"Live Population: {population}")
            time.sleep(3)
    except KeyboardInterrupt:
        pytest.skip("Monitoring stopped manually by user")
def main():
    try:
        data = []
        with open("world_population.csv", 'r') as f:
            lines = f.readlines()
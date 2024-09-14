import random
while True:
    print("Troy is playing chess!")
    print("Jack is also playing chess!")
    print(f"{"Troy" if random.randint("1", "2") == "1" else "Jack"} had won the game!")
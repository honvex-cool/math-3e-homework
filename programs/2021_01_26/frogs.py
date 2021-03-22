#!/usr/bin/python3

import random

FROG_PONDS = 3
PRINCESS_PONDS = 1
FROGS_TO_PRINCESSES_RATIO_IN_POND = 2
LUCKY_POND_PROBABILITY = PRINCESS_PONDS / (PRINCESS_PONDS + FROG_PONDS)
PRINCESS_PROBABILITY_IN_POND = 1 / (1 + FROGS_TO_PRINCESSES_RATIO_IN_POND)

def decision(probability):
    return random.random() < probability

def get_random_pond():
    return decision(LUCKY_POND_PROBABILITY)

def kiss_random_from(has_princesses):
    return decision(PRINCESS_PROBABILITY_IN_POND) if has_princesses else False

def simulate(sample_count):
    samples = 0
    lucky_pond_count = 0
    second_is_princess_count = 0
    while samples < sample_count:
        pond = get_random_pond()
        kiss = kiss_random_from(pond)
        if not kiss:
            samples += 1
            if pond:
                lucky_pond_count += 1
            next_kiss = kiss_random_from(pond)
            if next_kiss:
                second_is_princess_count += 1
    return lucky_pond_count / sample_count, second_is_princess_count / sample_count


n = int(input("How many times to sample: "))

lucky_pond, second_is_princess = simulate(n)

print("The Prince kisses a random frog from a random pond")
print("It turns out to be just an ordinary frog")
print("Probability that there are any frogs in this pond:", lucky_pond)
print("Probability that the next frog from this pond is a princess:", second_is_princess)


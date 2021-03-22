#!/usr/bin/python3

# helicopters.py

def sector_success(helicopter_count, failure_probability, sector_probability):
    return (1 - failure_probability**helicopter_count) * sector_probability

def probability_of_success(
    partition,
    first_sector_probability,
    second_sector_probability,
    helicopter_effectiveness
):
    failure = 1 - helicopter_effectiveness
    return sector_success(partition[0], failure, first_sector_probability) \
            + sector_success(partition[1], failure, second_sector_probability)

def helicopter_partition(
    number_of_helicopters,
    first_sector_probability,
    second_sector_probability,
    helicopter_effectiveness
):
    success = lambda partition: probability_of_success(
            partition,
            first_sector_probability,
            second_sector_probability,
            helicopter_effectiveness
        )
    optimal_partition = max(
        ((h, number_of_helicopters - h) for h in range(0, number_of_helicopters + 1)),
        key=success
    )
    return optimal_partition, success(optimal_partition)

print(
    "Optimal helicopter partition {} yields probability {}".format(
        *helicopter_partition(
            20,
            1.0 / 3.0,
            1.0 / 6.0,
            1 - 0.5**0.1
        )
    )
)


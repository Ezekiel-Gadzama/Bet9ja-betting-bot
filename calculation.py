import numpy as np

number_of_trials = 5
starting_stake = 10
average_odd = 1.5
amount_to_use = 15000


def stake_distribution_starting_stake():
    all_stakes = []
    all_stakes.append(100)
    starting_stake = all_stakes[0]
    for count in range(2, number_of_trials + 1):
        new_stake = int(
            (np.sum(all_stakes) + (starting_stake * (average_odd - 1) * count)) / (average_odd - 1))
        all_stakes.append(new_stake)
    num = (amount_to_use + (amount_to_use * 0.15)) / np.sum(all_stakes)
    for i in range(len(all_stakes)):
        all_stakes[i] = int(all_stakes[i] * num)
    print(all_stakes)
    return all_stakes


list_of_stakes = stake_distribution_starting_stake()
first = list_of_stakes[0]
daily = 5 # 60  # number of matches it can bet in a day
rate = ((((first * average_odd) - first) * daily) / sum(list_of_stakes)) + 1
print(f"daily Win rate is: {rate} and monthly is {rate ** 30} and profit will be {((rate ** 30) * amount_to_use) - amount_to_use}")

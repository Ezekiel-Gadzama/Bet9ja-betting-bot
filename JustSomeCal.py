from itertools import combinations
import math


# Function to calculate profit ratio
def calculate_profit_ratio(n, win_rate, odd_per_match, stake_per_bet, comb):
    # Calculate number of matches won and lost
    num_wins = math.floor(win_rate * n)
    num_losses = n - num_wins

    # Calculate total combinations for nC3
    total_combinations = math.comb(n, comb)

    # Calculate combinations of winning bets for num_winsC3
    winning_combinations = math.comb(num_wins, comb)

    # Calculate losing combinations
    losing_combinations = total_combinations - winning_combinations
    
    # Calculate total money won excluding stake
    winnings = (((odd_per_match ** comb) - 1) * stake_per_bet)
    if comb > 4:
         increase = (comb - 4) * 5
    else:
         increase = 0

    total_money_won = winning_combinations * (winnings + (increase/100 * winnings))

    # Calculate total money lost
    total_money_lost = losing_combinations * stake_per_bet

    # Calculate profit
    profit = total_money_won - total_money_lost

    # Calculate initial total stake
    initial_total_stake = total_combinations * stake_per_bet

    # Calculate profit ratio
    profit_ratio = profit / initial_total_stake

    return profit_ratio, total_combinations, winning_combinations, losing_combinations, profit

def calculate_arbitrage(odd1, odd2, total_stake):
    # Check if arbitrage exists
    if (1/odd1 + 1/odd2) >= 1:
        return "No arbitrage opportunity."

    # Calculate stakes for both outcomes
    stake1 = total_stake * (1/odd1) / (1/odd1 + 1/odd2)
    stake2 = total_stake * (1/odd2) / (1/odd1 + 1/odd2)

    # Calculate returns for both outcomes
    return1 = stake1 * odd1
    return2 = stake2 * odd2

    # Calculate profit
    profit = return1 - total_stake  # Profit will be the same for return2

    return {
        "Stake on outcome 1": stake1,
        "Stake on outcome 2": stake2,
        "Total stake": total_stake,
        "Return (either outcome)": return1,
        "Profit": profit
    }


# Function to find the best n for maximizing profit ratio
def find_best_n(max_n, win_rate, odd_per_match, stake_per_bet):
    best_n = 0
    best_profit_ratio = -float('inf')
    best_profit = 0
    best_total_combinations = 0
    best_winning_combinations = 0
    best_losing_combinations = 0
    best_comb = 0

    for n in range(1, max_n + 1):
        for comb in range (n):
                profit_ratio, total_combinations, winning_combinations, losing_combinations, profit = calculate_profit_ratio(n,
                                                                                                                            win_rate,
                                                                                                                            odd_per_match,
                                                                                                                            stake_per_bet,comb)
                







                
                i = 1
                while n - comb + i <= n:
                    new_comb = n - comb + i
                    i += 1
                    if(new_comb > n):
                        continue
                    new_win_rate = 0.7
                    new_odd_per_match = 1.43
                    new_profit_ratio, new_total_combinations, new_winning_combinations, new_losing_combinations, new_profit = calculate_profit_ratio(n,
                                                                                                                                                new_win_rate,
                                                                                                                                                new_odd_per_match,
                                                                                                                                                stake_per_bet, new_comb)
                    odd1 = profit_ratio + 1  # First odd

                    odd2 = new_profit_ratio + 1   # Second odd

                    new_total_stake = 200  # Total amount you want to stake
                    if odd1 > 1 and odd2 > 1:
                        print(f"odd 1: {odd1}  and odd 1: {odd2}  with {profit_ratio}  and  {new_profit_ratio}")
                        arbitrage = calculate_arbitrage(odd1, odd2, new_total_stake)
                        if isinstance(arbitrage, str):
                            print(f"arbitrage: {arbitrage}")
                        else:
                            print(f"Stake on outcome 1: {arbitrage['Stake on outcome 1']:.2f}")
                            print(f"Stake on outcome 2: {arbitrage['Stake on outcome 2']:.2f}")
                            print(f"Total stake: {arbitrage['Total stake']:.2f}")
                            print(f"Return (either outcome): {arbitrage['Return (either outcome)']:.2f}")
                            print(f"Profit: {arbitrage['Profit']:.2f}")











                if profit_ratio > best_profit_ratio:
                    best_profit_ratio = profit_ratio
                    best_n = n
                    best_profit = profit
                    best_total_combinations = total_combinations
                    best_winning_combinations = winning_combinations
                    best_losing_combinations = losing_combinations
                    best_comb = comb
                    # print(f"Profit : {profit}  in {n}  and comb {comb}")


    return best_n, best_profit_ratio, best_profit, best_total_combinations, best_winning_combinations, best_losing_combinations, best_comb


# Parameters
max_n = 200  # You can adjust this to test higher values of n
win_rate = 0.4
odd_per_match = 2.7
stake_per_bet = 10
# Find the best n and profit ratio
best_n, best_profit_ratio, best_profit, best_total_combinations, best_winning_combinations, best_losing_combinations, best_comb = find_best_n(
    max_n, win_rate, odd_per_match, stake_per_bet)

print(f"Best n: {best_n}")
print(f"Best comb: {best_comb}")

print(f"The deal is {math.floor(win_rate * best_n)}C{best_comb}")
print(f"Best Profit Ratio: {best_profit_ratio * 100:.2f}%")
print(f"Total Profit: {best_profit}")
print(f"Total Combinations ({best_n}C{best_comb}): {best_total_combinations}")
print(f"Winning Combinations: {best_winning_combinations}")
print(f"Losing Combinations: {best_losing_combinations}")
print(f"Total money needed is {best_total_combinations * stake_per_bet}")

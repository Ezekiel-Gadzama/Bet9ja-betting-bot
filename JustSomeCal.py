def calculate_arbitrage(odd1, odd2, total_stake):
    # Check if arbitrage exists
    if (1/odd1 + 1/odd2) >= 1:
        print("No arbitrage opportunity.") 

    # Calculate stakes for both outcomes
    stake1 = total_stake * (1/odd1) / (1/odd1 + 1/odd2)
    stake2 = total_stake * (1/odd2) / (1/odd1 + 1/odd2)

    # Calculate returns for both outcomes
    rate = 0.7
    return1 = (stake1 * (1-rate)) * odd1
    return2 = (stake2 + (stake1 * rate)) * odd2

    # Calculate profit
    profit1 = return1 - total_stake  # Profit will be the same for return2
    profit2 = return2 - total_stake  # Profit will be the same for return2

    return {
        "Stake on outcome 1": stake1,
        "Stake on outcome 2": stake2,
        "Total stake": total_stake,
        "Return (either outcome)": return2,
        "Profit 1": profit1,
        "Profit 2": profit2

    }

# Example usage
odd1 = 2.7  # First odd
odd2 = 1.43  # Second odd
total_stake = 100  # Total amount you want to stake

arbitrage = calculate_arbitrage(odd1, odd2, total_stake)
if isinstance(arbitrage, str):
    print(arbitrage)
else:
    print(f"Stake on outcome 1: {arbitrage['Stake on outcome 1']:.2f}")
    print(f"Stake on outcome 2: {arbitrage['Stake on outcome 2']:.2f}")
    print(f"Total stake: {arbitrage['Total stake']:.2f}")
    print(f"Return (either outcome): {arbitrage['Return (either outcome)']:.2f}")
    print(f"Profit 1: {arbitrage['Profit 1']:.2f}")
    print(f"Profit 2: {arbitrage['Profit 2']:.2f}")

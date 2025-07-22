#!/usr/bin/env python3
'''
Author:         @midnightslacker
Last Update:    07/22/2025
Description:    Runs multiple ECF Fantasy Football draft order simulations
                to calculate the average draft position for each owner.
'''

import random
import argparse
from collections import defaultdict

def run_draft_simulation(owners):
    """Shuffles the list of owners to simulate a single draft order."""
    random.shuffle(owners)
    return owners

def main(num_runs):
    """
    Runs the draft simulation a specified number of times and calculates
    the average draft position for each owner.
    """
    # A list of all team owners
    owners = ['Director', 'Gruver', 'Ressler', 'Christ', 'Shawn', 'Jairus', 'Void', 'Scuba', 'Nick A', 'Adam', 'Hunt', 'Donch']

    # A dictionary to store the draft position for each owner from every run
    # defaultdict(list) initializes a new list for any new key
    owner_picks = defaultdict(list)

    print(f"Running {num_runs} draft simulations...\n")

    # Run the simulation for the specified number of times
    for _ in range(num_runs):
        # Get the shuffled order for the current run
        shuffled_owners = run_draft_simulation(owners[:]) # Use a copy of the list

        # Record the pick number for each owner
        for i, owner in enumerate(shuffled_owners):
            # The pick number is the index + 1
            pick_number = i + 1
            owner_picks[owner].append(pick_number)

    # Calculate the average pick for each owner
    average_positions = {}
    for owner, picks in owner_picks.items():
        average_positions[owner] = sum(picks) / len(picks)

    # Sort the owners by their average position, from lowest to highest
    sorted_owners = sorted(average_positions.items(), key=lambda item: item[1])

    # Print the final sorted results
    print("--- Average Draft Position Results ---")
    for i, (owner, avg_pick) in enumerate(sorted_owners, 1):
        print(f"{i:<3} {owner:<10} (Average Pick: {avg_pick:.2f})")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Run a fantasy football draft lottery simulation."
    )
    parser.add_argument(
        'num_runs',
        type=int,
        help="The number of times to run the simulation."
    )
    args = parser.parse_args()

    main(args.num_runs)

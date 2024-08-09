import os
import csv

election_data_csv = os.path.join("..", "Resources", "election_data.csv")

total_votes = 0
candidate_votes = []
percentages = []

with open(election_data_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]
        candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1

for candidate, vote_count in candidate_votes():
    percentages[candidate] = (vote_count/total_votes) * 100

winner = max(candidate_votes, key = candidate_votes.get)


print("Election Results")
print("-------------------")
print(f"Total Votes: {total_votes}")
print("-------------------")
print("Candidates:")
print(f"{candidate}: {percentages[candidate]}")
print(f"Winner: {winner}")

with open("analysis.txt") as file:
    print("Election Results")
    print("-------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------")
    print("Candidates:")
    print(f"{candidate}: {percentages[candidate]}")
    print(f"Winner: {winner}")
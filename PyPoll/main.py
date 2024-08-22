import os
import csv

# Path to CSV file
election_csv = os.path.join('Resources', 'election_data.csv')

# Creating lists to store data
ballot_id = []
candidate_count = {}
all_can = []

# Open CSV file
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Read header row
    next(csvreader)

    # Read each row after header
    for row in csvreader:

        # Total number of votes
        ballot_id.append(row[0])
        total_votes = len(ballot_id)
        #print(total_votes)

        # Complete list of candidates
        candidate = row[2]
        
        # Number of times candidiate appears on ballot
        if candidate in candidate_count:
            candidate_count[candidate] += 1
        else:
            candidate_count[candidate] = 1
    
    # Calculate how many votes each candidate has and get the percentage
    for can, votes in candidate_count.items():
        each_candidate = (f"{can}: {votes}")
        #print(each_candidate)
        split_can = each_candidate.split(': ')
        percent = (votes/ total_votes * 100)
        #print(percent)
        format_can = (f"{split_can[0]}: {percent:.3f}% ({split_can[1]})")
        all_can.append(format_can)

    # Winner of the election based on popular vote
    winner = max(candidate_count, key=candidate_count.get)
    #print(winner)

# Print results
print('Election Results')
print('----------------------------')
print(f'Total Votes: {total_votes}')
print('----------------------------')
for candidate_info in all_can:
    print(candidate_info)
print('----------------------------')
print(f'Winner: {winner}')
print('----------------------------')

# File path and write data as text file
analysis_path = os.path.join('Analysis', 'PyPoll.txt')
with open(analysis_path, 'w') as file:
    file.write('Election Results\n')
    file.write('----------------------------\n')
    file.write(f'Total Votes: {total_votes}\n')
    file.write('----------------------------\n')
    for candidate_info in all_can:
        file.write(f'{candidate_info}\n')
    file.write('----------------------------\n')
    file.write(f'Winner: {winner}\n')
    file.write('----------------------------\n')
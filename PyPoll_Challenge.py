# The data we need to retrieve
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote
# Add our dependencies.
import os
import csv
#Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Create a list for the counties (NEW)
county_options = []
county_votes = {}
# County name that had the largest turnout (NEW)
winning_county = ""
winning_county_votes = 0
winning_county_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the county name from each row(NEW)
        county_name = row[1]
        # If the county does not match any existing county add it the county list.
        if county_name not in county_options:
            # Add the county name to the county list.
            county_options.append(county_name)
            # And begin tracking that candidate's voter count.
            county_votes[county_name] = 0
        # Add a vote to that county's count
        county_votes[county_name] += 1
        
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate add it the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
# Open txt file to print results
with open(file_to_save, "w") as txt_file:
    election_results = (
            f'\nElection Results\n'
            f'----------------------------\n'
            f'Total Votes: {total_votes:,}\n'
            f'----------------------------\n'
            f'\nCounty Votes:\n')
    print(election_results, end='')
    # Print results in txt file
    txt_file.write(election_results)
	
    # Print county list (NEW)
    for county in county_votes:
        # Retrieve vote count and percentage.
        votes = county_votes[county]
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each county, their voter count, and percentage to the
        # terminal.
        county_results = (f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_results, end='')
        # Print results in txt file
        txt_file.write(county_results)
            
        # Find county with largest turnout(NEW)
        if (votes > winning_county_votes) and (vote_percentage > winning_county_percentage):
            winning_county_votes = votes
            winning_county = county
            winning_county_percentage = vote_percentage

            # Print the winning county' results to the terminal.
    winning_county_summary = (
        f"----------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"----------------------------\n")

    print(winning_county_summary, end='')
    # Print results in txt file
    txt_file.write(winning_county_summary)

    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each candidate, their voter count, and percentage to the
        # terminal.
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results, end='')
        # Print results in txt file
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------\n")

    print(winning_candidate_summary, end='')
    # Print results in txt file
    txt_file.write(winning_candidate_summary)
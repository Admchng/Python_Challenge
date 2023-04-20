#import modules
import csv
import os

#sets the file path
file_to_load = os.path.join("resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")


total_votes = 0
candidate_votes = 0
percentage_won = 0
candidates = 0
candidates_won = ""
total_won = 0

#read the csv file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    print(type(file_reader))
    headers = next(file_reader)
    print(headers)

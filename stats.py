import json

# Load the JSON files
files = [
    "attack_result/result_6_actors_dynamic.json",
    "attack_result/result_6_actors_quest10_dynamic.json",
    "attack_result/result_6_actors_quest10_early_dynamic.json",
    "attack_result/result_6actors_early_dynamic.json"
]

# Function to count successes (score == 5) and total iterations
def count_successes(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    successes = 0
    total_iterations = 0
    
    for attack in data['data']:
        for attempt in attack['attempts']:
            total_iterations += 1
            if attempt.get('final_score') == 5:
                successes += 1
    
    return successes, total_iterations

# Calculate successes and iterations for each file
for file in files:
    successes, total_iterations = count_successes(file)
    print(f"File: {file}, Successes: {successes}, Total Iterations: {total_iterations}")

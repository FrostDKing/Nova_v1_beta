import json
import os

def savedata(prompt, response, file_path=r'path'):
    data = []

    # Check if file exists
    if os.path.exists(file_path):
        # Read existing data
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                pass  # If file is empty or not valid JSON, start with an empty list

    # Add new entry
    data.append([f"User:{prompt}", f"Response:{response}"])

    # Write updated data back to file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def read_data(file_path=r"path"):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError:
                return []  # Return an empty list if the file is empty or contains invalid JSON
    return []  # Return an empty list if the file does not exist

#def delete_history(file_path=r'path'):
    data = read_data(file_path)
    
    if len(data) > 20:
        while len(data) > 20:
            data.pop(0)
            with open(r"C:\projects\project P\jarvis\data\previous_covos.json", 'w') as file:
                json.dump(data, file, indent=4)

        with open(file_path,"w") as file:
            json.dump(data, file, indent=4)

def remember(prompt,file_path=r"path"):
    data = []

    # Check if file exists
    if os.path.exists(file_path):
        # Read existing data
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                pass  # If file is empty or not valid JSON, start with an empty list

    # Add new entry
    data.append([f"User:{prompt}"])

    # Write updated data back to file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
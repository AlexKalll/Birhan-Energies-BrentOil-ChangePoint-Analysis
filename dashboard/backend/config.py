import os

# Get the directory of the current script (dashboard/backend/)
script_dir = os.path.dirname(__file__)

# Define the project root as the parent directory of the backend folder
PROJECT_ROOT = os.path.abspath(os.path.join(script_dir, '..', '..'))

# Define paths for data files relative to the project root
PROCESSED_DATA_PATH = os.path.join(PROJECT_ROOT, 'data', 'processed', 'processed_data.csv')
EVENTS_FILE_PATH = os.path.join(PROJECT_ROOT, 'data', 'events', 'key_events.csv')

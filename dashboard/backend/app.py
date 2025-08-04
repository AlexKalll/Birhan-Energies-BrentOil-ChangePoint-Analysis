from flask import Flask
from flask_cors import CORS
import argparse
from api import get_data, get_events

# --- Flask App Initialization ---
app = Flask(__name__)
# Enable CORS for the frontend to access this API
CORS(app)

# --- Register API Endpoints ---
app.add_url_rule('/api/data', view_func=get_data, methods=['GET'])
app.add_url_rule('/api/events', view_func=get_events, methods=['GET'])

# --- Main entry point ---
if __name__ == '__main__':
    # Use argparse to allow specifying the port from the command line
    parser = argparse.ArgumentParser(description='Run the Flask backend server.')
    parser.add_argument('-p', '--port', type=int, default=3000, 
                        help='Port number to run the server on (default: 3000)')
    args = parser.parse_args()
    
    # Run the Flask app on the specified port
    app.run(port=args.port)

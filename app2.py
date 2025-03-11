# Import necessary modules
from flask import Flask   # Flask is a lightweight web framework for Python
import os                 # For accessing environment variables
import subprocess         # For executing shell commands
import pytz               # For handling timezones
from datetime import datetime  # For getting the current time

# Create a Flask web application
app = Flask(__name__)   # Fixed _name_ to __name__

# Define a route to handle requests to "/htop"
@app.route("/htop")
def htop():
    # Define a custom name to display on the page
    full_name = "Keshavraj"
    
    # Get the current system username from environment variables
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"
    
    # Set the timezone to Asia/Kolkata (Indian Standard Time)
    ist = pytz.timezone("Asia/Kolkata")
    
    # Get the current server time in IST format
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S IST")

    try:
        # Execute the 'top' command to get system performance details (first 20 lines)
        top_output = subprocess.getoutput("top -b -n 1 | head -20")
    except Exception as e:
        # If an error occurs while executing the command, display the error message
        top_output = f"Error fetching top output: {str(e)}"

    # Return an HTML response with system information and top output
    return f"""
    <html>
    <head><title>HTop Output</title></head>
    <body>
        <h1>System Information</h1>
        <p><b>Name:</b> {full_name}</p>
        <p><b>Username:</b> {username}</p>
        <p><b>Server Time (IST):</b> {server_time}</p>
        <h2>Top Output</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

# Run the Flask app when the script is executed directly
if __name__ == "__main__":   # Fixed _name_ to __name__
    # Start the Flask development server
    app.run(host="0.0.0.0", port=8080, debug=True)

from flask import Flask, jsonify, request
from flask_cors import CORS
from scraping import scrapingLink

"""
Description:
    Main file for the Flask API server.

Parameters:
    None

Returns:
    JSON response

Specifications:
    1. Establishes a connection to the Flask app.
    2. Establishes GET route of the API.
        - Sends a GET request to the API containing verfication message..
    3. Establishes Post route of the API.
        - Sends a POST request to the API with a JSON article link.
        - Calls the scrapingLink function and unpacks the results.
        - Verifies the response data.
"""

# Create a new Flask app
app = Flask(__name__)

# Allow CORS to be acessed from any origin (for testing purposes)
CORS(app, origins='*')

# Test get route for the API
@app.route('/api', methods=['GET'])
def api():

    # Return a JSON response
    return jsonify({'message': 'Get request received! Flask server is running!'})


# Define a POST route for the API
@app.route('/api/link', methods=['POST'])
def receive_link():

    # Get the JSON data from the request
    data = request.get_json()

    # Check if there is any data
    if not data or 'link' not in data:
        return jsonify({'status': 'failure', 'message': 'Invalid request'}), 400
    
    # Get the link from the data
    link = data['link']

    # Call the scrapingLink function and unpack the results
    title, date, publisher, body = scrapingLink(link)
    
    # Check if the scraping was successful and return the scraped data
    if title and date and publisher and body:
        return jsonify({
            'status': 'success',
            'title': title,
            'date': date,
            'publisher': publisher,
            'body': body
        })
    else:
        return jsonify({'status': 'failure', 'message': 'Failed to scrape and validate article.'}), 400


# Define a GET route for the API
if __name__ == '__main__':
    app.run(debug=True, port=8080)

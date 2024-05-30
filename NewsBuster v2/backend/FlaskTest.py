import unittest
import json
from backend.main import app

"""
Description:
    Test class for the Flask API server.

Parameters:
    None

Returns:
    none

Specifications:
    1. Set up the Flask app for testing.
    2. Test the GET route of the API.
    3. Test the POST route of the API.
"""
# Define a class for the Flask app test
class TestFlaskApp(unittest.TestCase):

    # Set up the Flask app for testing
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test the GET route of the API
    def test_api_get(self):

        # Send a GET request to the API
        response = self.app.get('/api')

        # Load the response data as JSON
        data = json.loads(response.data)

        # Verify the response data
        self.assertEqual(data['message'], 'Get request received! Flask server is running!')
        
    
    # Test the POST route of the API
    def test_api_post(self):
        
        # Send a POST request to the API with a JSON article link
        response = self.app.post('/api/link', json={'link': 'https://www.cnn.com/2020/04/30/politics/lobbying-coronavirus-outbreak/index.html'})
        
        # Load the response data as JSON
        data = json.loads(response.data)
        
        # Verify the response data
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['title'], 'Federal lobbying soars to near-record as industries scramble to shape coronavirus response')
        self.assertEqual(data['date'],'2020-04-30' )
        self.assertEqual(data['publisher'],'https://www.cnn.com')
        
        # Tests only the beginning of the body text for simplicity
        self.assertEqual(data['body'].startswith('CNN — Federal lobbying spending soared nearly $903 million')) 

    # Test the POST route of the API with a failure
    def test_api_link_failure(self):

        # Send a POST request to the API with an invalid JSON article link
        response = self.app.post('/api/link', json={'link': 'hellofromdev'})

        # Load the response data as JSON
        data = json.loads(response.data)
        
        # Verify the response data
        self.assertEqual(data['status'], 'failure')
        self.assertEqual(data['message'], 'Failed to scrape and validate article.')

# Run the tests
if __name__ == '__main__':
    unittest.main()
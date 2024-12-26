import requests

# Test 1: Verify Homepage Response
def test_homepage_response():
    response = requests.get('http://localhost:8080')  # URL of your app
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    print("Test 1 Passed: Homepage is accessible")

# Test 2: Validate Content on Homepage
def test_homepage_content():
    response = requests.get('http://localhost:8080')
    assert "WebSocket Chat" in response.text, "Title 'WebSocket Chat' not found"
    print("Test 2 Passed: Homepage contains expected content")

# Run tests
if __name__ == "__main__":
    test_homepage_response()
    test_homepage_content()

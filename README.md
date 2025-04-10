# 🧪 API Testing with Python Requests
This project demonstrates API testing using Python's **requests library**. It includes basic tests against two public APIs: JSONPlaceholder and httpbin. The tests cover various HTTP methods like GET, POST, PUT, and DELETE, validating status codes and responses.

## 📁 Project Structure
├ requestPractice.py          // API testing using JSONPlaceholder

├ httpbinPractice.py          // API testing using httpbin

├ README.md               // Documentation

## 🚀 How to Run
### Clone the repository (or download the files):
- git clone your-repo-url
- cd repo-name
- Make sure Python 3 is installed

### Install dependencies (only requests is needed):
- pip install requests

### Run the scripts:
- python Practice.py
- python httpbinPractice.py

## 📜 Script Details
### requestPractice.py (using JSONPlaceholder)
Performs a variety of API actions:

- GET request: Retrieves a single post and checks for correct ID and title.

- GET all posts: Iterates through all posts to validate content for a specific ID.

- POST request: Sends a new post and verifies a 201 status code.

- PUT request: Updates a post using a previous response as payload.

- DELETE request: Deletes a post and confirms successful deletion.

Each action checks HTTP status codes to ensure proper behavior.

### httpbinPractice.py (using httpbin)
- Sends a simple GET request to /get

 🔎 Verifies

- The response status is 200

- The Host header is correctly set to "httpbin.org"

- Displays your IP (origin)


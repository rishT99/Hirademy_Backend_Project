
# Hirademy Backend Project

Welcome to the Hirademy Backend Project repository! This project is a backend application developed for managing assistants using CRUD APIs. It includes database models, API endpoints, testing with Postman, and a demo recording showcasing the application's functionality.

## Technology Stack
- **Programming Language:** Python
- **Framework:** Flask
- **Database:** SQLite

## Application Requirements
- Implement CRUD APIs (POST, GET, PUT, DELETE) for managing Assistants.
- Define database model(s) for the Assistant, including fields such as id, name, mobile, email, salary, city, country, department, and role.

## API Endpoints
- **POST /assistant:** Creates a new record in the database and returns the id of the assistant.
- **GET /assistant/<assistant_id>:** Retrieves the details of the assistant with the specified id.
- **PUT /assistant/<assistant_id>:** Updates the details of the assistant with the specified id.
- **DELETE /assistant/<assistant_id>:** Deletes the record of the assistant with the specified id.

## Postman Collection and Testing
- The Postman collection file `Hirademy_Backend_Postman_Collection.json` contains requests for testing the implemented API endpoints.
- Test each API endpoint to ensure proper functionality and error handling.


## Running the Application Locally
1. Clone this repository to your local machine
2. Navigate to the project directory:
   ```
   cd Hirademy_Backend_Project
   ```
3. Install the required dependencies:
   ```
   pip install Flask
   ```
4. Run the Flask application:
   ```
   python app.py
   ```
5. Access the application in your web browser at `http://127.0.0.1:5000`.

## Using the Postman Collection
1. Import the Postman collection file `Hirademy_Backend_Postman_Collection.json` into Postman.
2. Use the collection to test each API endpoint.


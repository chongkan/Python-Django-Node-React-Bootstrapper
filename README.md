# Python-Django-Node-React-Bootstrapper

Auto Project Structure Generator: Python script to automate the generation of a web project folder structure with Docker, Django (backend), and React (frontend) based on a project name. Accelerate project setup with a standardized directory layout.
   ```
myapp
├── backend
│   ├── Dockerfile
│   ├── manage.py
│   ├── myapp
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── requirements.txt
└── frontend
    ├── Dockerfile
    ├── public
    │   ├── index.html
    │   └── favicon.ico
    ├── src
    │   ├── App.js
    │   ├── index.js
    │   └── components
    │       ├── Header.js
    │       └── Footer.js
    ├── package.json
    └── package-lock.json

   ```
## Project Setup

Follow these steps to set up the project:

1. Clone this repository to your local machine.

2. Open a terminal or command prompt.

3. Navigate to the directory where you cloned the repository.

4. Run the following command to generate the project structure, replacing `your_project_name` with your desired project name:
   ```
   python generate_structure.py your_project_name
   ```

5. The project structure will be created with the provided project name, replacing "myapp" in the template.

6. Once the structure is generated, you can proceed with the following steps.

## Backend Setup

To set up the backend part of the project:

1. Open a terminal or command prompt.

2. Navigate to the `backend` directory:
   ```
   cd your_project_name/backend
   ```

3. Build the backend Docker image:
   ```
   docker build -t your_project_name-backend -f Dockerfile.backend .
   ```

4. Run the backend container:
   ```
   docker run -d -p 8000:8000 --name your_project_name-backend-container your_project_name-backend
   ```

5. The backend container will start, and you can access it at http://localhost:8000.

## Frontend Setup

To set up the frontend part of the project:

1. Open a new terminal or command prompt.

2. Navigate to the `frontend` directory:
   ```
   cd your_project_name/frontend
   ```

3. Build the frontend Docker image:
   ```
   docker build -t your_project_name-frontend -f Dockerfile.frontend .
   ```

4. Run the frontend container:
   ```
   docker run -d -p 3000:3000 --name your_project_name-frontend-container your_project_name-frontend
   ```

5. The frontend container will start, and you can access it at http://localhost:3000.

Now you have the backend and frontend parts of your project set up and running, allowing you to interact with your web application.

Please note that these steps assume you have Docker and Python installed on your machine.

Feel free to customize the instructions or add more details specific to your project as needed.

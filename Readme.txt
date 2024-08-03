# Project Build and Deployment Instructions
=========================================

This project uses Docker for build automation. Follow the instructions below to build and run the Docker container.

## Prerequisites:
--------------
1. Docker

## Build and Run Instructions:
---------------------------
###1. Open a terminal and navigate to the root directory of the project.

###2. Build the Docker image:

   docker build -t my_flask_app .

###3. Run the Docker container:

   docker run -p 5000:5000 my_flask_app

#This will:
- Build the Docker image with the application.
- Run the unit tests inside the Docker container.
- Start the Flask application inside the Docker container.

Access the Flask application at:

   http://localhost:5000/cats
# Setup requirements
- Create a venv for the project and install the libraries in requirements.txt  

         cd house_price_api 
         pip install -r ./requirements.txt  

# Launch the service
- Run the project (from house_price_api folder):  
         
          uvicorn app.main:app --host localhost --port 8000 

- Navigate to localhost:8000/docs to see the API documentation and test the endpoints
- Navigate to localhost:8000/redoc to see the alternative API documentation and test the endpoints
- Navigate to localhost:8000/metrics to see the metrics  
  
# Run the tests
- Run the tests (from house_price_api folder):  

          pytest

# Deploy with docker-compose
Or to deploy in containers with Prometheus and Grafana monitoring
- install docker compose
- run in the project root
    
        docker compose up

- Navigate to localhost:8000/* for API endpoints as above
- Navigate to localhost:8080 to see the Prometheus dashboard
- Navigate to localhost:3000 to see the Grafana dashboard (Username: admin, Password: admin  

# CI/CD 
- The project is configured with a basic continuous integration pipeline using Github Actions
- The pipeline runs the tests and the docker-compose deployment
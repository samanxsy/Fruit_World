# Fruit_World
A single page application to learn all you need about the fruits!

[![CI](https://github.com/samanxsy/Fruit_World/actions/workflows/CI.yaml/badge.svg)](https://github.com/samanxsy/Fruit_World/actions/workflows/CI.yaml)

## Getting Started
These instructions will get you a copy of the project to run it on your local machine for development and testing purposes.

### Prerequisites

- Python 3.10
- Flask
- Pandas
- Numpy

### Installing 

1. clone the repository to your local machine:
  - git clone https://github.com/samanxsy/Fruit_World.git
2. Install the requirements
- ```
  pip install -r requirements.txt
  ```
3. Run the test with pytest
```
pytest
```
4. Run the app on your localhost
```
gunicorn app.server:app
```

### Build With
- Python - Programming Language
- Flask - Web framework
- Pandas - data manipulation software 

### app view

![Fruitworld](https://user-images.githubusercontent.com/118216325/217236716-7c26945f-65eb-42c0-836c-5e464d63ddcd.png)

### Containerization
- To run the application in a container, follow these steps: 

  - build the container image using the docker file:
  ```
  docker build -t fruit-world:v1.0 .
  ```
  - Run the container using this command:
  ```
  docker run -p 5000:5000 fruit-world:v1.0
  ```
### Author
 - Samanxsy (Saman Saybani)
 
### Acknowledgments
 - All the fruits data are from <https://fruityvice.com/>

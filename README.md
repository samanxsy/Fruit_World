# Fruit_World
A single page application to learn all you need about the fruits!

## Getting Started
These instructions will get you a copy of the project to run it on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Flask
- Pandas

### Installing 

1. clone the repository to your local machine:
  - git clone https://github.com/samanxsy/Fruit_World.git
2. Install the requirements
- ```
  pip install -r requirements.txt
  ```
3. Run the program

### Build With
- Python - Programming Language
- Flask - Web framework
- Pandas

### app view

![Fruitworld](https://user-images.githubusercontent.com/118216325/217236716-7c26945f-65eb-42c0-836c-5e464d63ddcd.png)

### Containerization
- If you want to run the application in a container, follow these steps: 
- If you don't have docker installed visit: <https://www.docker.com/>

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

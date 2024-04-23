# Pre-Requisites
Before getting started, ensure you have Docker Desktop installed.

## Installation Steps

1. **Install Docker Desktop**: If you haven't already, download and install Docker Desktop from [here](https://www.docker.com/products/docker-desktop).

## Running RabbitMQ

Once Docker Desktop is installed, run the following command in your terminal:

docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
This command will set up and start RabbitMQ with the management plugin enabled.

🎉 That's it! RabbitMQ is now up and running.

## Running the Files
After RabbitMQ is running, execute the following three files:

publish.py: Publishes messages.
notify.py: Notified the email in terminal when there is data in queued
report.py: Generate Report in terminal when there is data in queued

## Accessing the Management Plugin
You can access the RabbitMQ management plugin by visiting http://localhost:15672/. This provides a web-based interface for managing and monitoring your RabbitMQ instance.

## Happy messaging! 🐇📨
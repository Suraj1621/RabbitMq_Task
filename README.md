# Python RabbitMQ Communication Services

This repository contains a pair of Python services for message exchange via RabbitMQ. One service acts as a publisher, while the other serves as a sender. These services are designed to showcase a simple yet effective communication pattern using RabbitMQ within a Python environment.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Overview

- **Publisher Service**: A Python script (`PublisherService.py`) that publishes messages to a RabbitMQ queue.
- **Sender Service**: Another Python script (`SenderService.py`) that consumes messages from the same RabbitMQ queue and processes them accordingly.

## Prerequisites

Before running the services, ensure you have the following prerequisites installed:

- Python 3.x
- RabbitMQ server (can be installed locally or accessed remotely)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Suraj1621/python-rabbitmq-services.git
   ```

2. Navigate to the project directory:

   ```bash
   cd python-rabbitmq-services
   ```

3. Install the required Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Before running the services, make sure to configure the RabbitMQ connection settings in both the `PublisherService.py` and `SenderService.py` scripts. Update the host, port, username, password, and queue details as per your RabbitMQ setup.

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

## License

This project is licensed under the [MIT License](LICENSE).

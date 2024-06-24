# Flask WOL App

This is a simple Flask application for sending Wake-on-LAN (WOL) packets to wake up computers on your local network. I created this project to provide a web interface for waking up devices remotely.

## Features

- Send WOL packets to specified MAC addresses.
- Simple and user-friendly web interface.
- Dockerized for easy deployment.

## Technologies Used

- Python
- Flask
- Docker

## Screenshots

![grafik](https://github.com/han-link/flask-wol-app/assets/115926359/64bb0a54-8157-4614-9a77-687cebea9baf)

![grafik](https://github.com/han-link/flask-wol-app/assets/115926359/9fb41c36-7fa1-4eef-b636-3036335f5788)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/han-link/flask-wol-app.git
   ```

   ```bash
   cd flask-wol-app
   ```

3. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   ```

   ```bash
   source venv/bin/activate
   ```

4. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Configure your WOL settings in `config.py`.

7. Run the application:

   ```bash
   python run.py
   ```

## Docker

To run the application using Docker:

1. Build the Docker image:

   ```bash
    docker build -t flask-wol-app .
    ```

3. Run the Docker container:

    ```bash
    docker run -d -p 5000:5000 flask-wol-app
    ```

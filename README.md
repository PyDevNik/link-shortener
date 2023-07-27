# Link Shortener
## Simple URL Shortening service

Link Shortener is a simple URL shortening service that allows users to create short and memorable aliases for long URLs. This project was developed by [PyDevNik](https://github.com/PyDevNik) as part of a personal learning project. The main goal of this project is to provide a straightforward and easy-to-use URL shortening solution.

## How It Works

The Link Shortener application takes a long URL as input and generates a short, unique alias for it. When a user accesses the short URL, the service redirects them to the original long URL. This way, users can share shorter links that are easier to remember and manage.

## Features

- URL shortening: Convert long URLs into short, custom aliases.

## Getting Started

### Prerequisites

- Python (version 3.X)
- Flask
- MongoDB

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/PyDevNik/link-shortener.git
   cd link-shortener
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the application:

   ```bash
   cd app
   python app.py
   ```

2. Open your web browser and go to `http://localhost:5000` to access the Link Shortener service.

### Configuration

You can customize certain aspects of the application by modifying the `config.py` file. For example, you can change the base URL, set link expiration policies, or enable/disable custom aliases.

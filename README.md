
![Tracking](https://github.com/user-attachments/assets/4bfefa5b-5530-489c-ba1d-ea32cc6b2079)

# OrderSync

This project is a web application developed as part of a summer training program to address issues observed in the order flow within the company. The idea emerged from identifying inefficiencies in how orders were managed and tracked. This application serves as a suggested solution to streamline the order management process, making it easier to connect between departments, manage orders effectively, and inform customers about the status of their orders.

## Features

- **View Orders**: Display the latest orders with relevant details such as order number, name, description, department, and state.
- **Add Orders**: Easily add new orders to the system.
- **Edit Orders**: Modify existing orders as needed.
- **Delete Orders**: Remove orders from the system to maintain an accurate record.
- **Order History**: Access a history of completed orders with a view-only option to see order details.
- **API Integration**: Provides an API endpoint to check order statuses without the need for manual messaging or waiting for responses, enhancing customer experience.

## Future Enhancements

This application serves as the first feature in a broader vision for order management. Future ideas may include advanced analytics, automated notifications, improved user interfaces, user management, and enhanced security measures to further improve usability and functionality.


## Getting Started

Follow these steps to set up and run the project:

1. Ensure you have Docker installed on your machine.

2. Ensure you start Docker.

3. Open a terminal and navigate to the project directory.

4. Run the following commands:

   ```bash
   docker-compose down
   docker-compose up --build
   
This will start the application.

Open your web browser and go to http://localhost:5000.

### `.env` file:

Before you start you must provide a `.env` file that conform to
the following keys and structure.

```ini
# configurations used by the docker compose file

# web configurations
WEB_PORT=5000

# db configurations
DB_PORT=3306
INIT_FILE=./resources (or where you keep the .sql build script)
HOSTNAME=test
MYSQL_DATABASE=root
MYSQL_ROOT_PASSWORD=changeme
MYSQL_USER=dbuser
MYSQL_PASSWORD=changeme
SCHEMA=schema_name
```

## Author
Salman Saleh Alkhalifah


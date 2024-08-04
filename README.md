![Tracking](https://github.com/user-attachments/assets/4bfefa5b-5530-489c-ba1d-ea32cc6b2079)

# OrderSync

**OrderSync** is a web application developed during a summer training program to address inefficiencies observed in the order flow within the company. This application serves as a solution to streamline the order management process, facilitating effective communication between departments and keeping customers informed about their order statuses.

## Features

- **View Orders**: Easily display the latest orders with essential details such as order number, name, description, department, and state.
- **Add Orders**: Quickly add new orders to the system.
- **Edit Orders**: Modify existing orders as needed.
- **Delete Orders**: Remove orders from the system to maintain an accurate record.
- **Order History**: Access a history of completed orders with a view-only option to see order details.
- **API Integration**: Check order statuses through an API endpoint, enhancing the customer experience by eliminating the need for manual messaging or waiting for responses.

## Future Enhancements

OrderSync aims to evolve with the following features:
- **Advanced Analytics**: Implement data analysis tools for better insights.
- **Improved User Interfaces**: Revamp the UI for a more intuitive experience.
- **User Management**: Introduce features for managing user roles and permissions.
- **Enhanced Security Measures**: Strengthen security protocols for data protection.
- **Department Order Management**: Provide tools for departments to manage their orders efficiently, including assigning responsibilities and tracking progress.
- **Basic Department Communication**: Facilitate inter-department communication with a chat feature, allowing file and image sharing.

## Getting Started

To set up and run the project, follow these steps:

1. Ensure Docker is installed on your machine.
2. Start Docker.
3. Open a terminal and navigate to the project directory.
4. Run the following commands:

   ```bash
   docker-compose down
   docker-compose up --build
This will start the application. Once it's running, open your web browser and go to http://localhost:5000.

### Environment Configuration
Before starting the application, create a .env file in the project directory with the following keys and structure:

```ini
# configurations used by the docker compose file

WEB_PORT=5000
DB_PORT=3306
INIT_FILE=./resources
HOSTNAME=test1
MYSQL_DATABASE=order_tracking
MYSQL_ROOT_PASSWORD=changeme
MYSQL_USER=dbuser1
MYSQL_PASSWORD=changeme
SCHEMA=order_tracking
SECRET_KEY=my_secret_key_here
```


## Author
Salman Saleh Alkhalifah

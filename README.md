
# Digital Products Platform

This project is a comprehensive platform for managing and distributing digital products. It offers features such as user authentication, product listing and management, subscription handling, and more, making it ideal for e-commerce businesses or creators who want to sell digital content.

## Features

- **User Authentication**: Users can sign up, log in, manage profiles, and handle account details.
- **Digital Product Management**: Administrators can add, edit, and delete digital products. Products can be categorized, and associated metadata is stored to improve searchability and organization.
- **Subscription Plans**: The platform supports various subscription models, allowing users to subscribe to specific tiers or plans that grant access to premium content or products.
- **Dynamic User Dashboard**: Users can view their purchased products, active subscriptions, and account details through an intuitive dashboard.
- **Media Handling**: Securely upload, manage, and deliver digital files (e.g., e-books, software, videos) to users.
- **Scalable Infrastructure**: The project is designed with scalability in mind, supporting large numbers of users and products.

## Project Structure

- **`manage.py`**: Django's command-line utility for administrative tasks. You will use it to run the server, migrate databases, and manage your application.
- **`products/`**: Contains the core logic for digital product management. This includes models for products, views for product-related pages, and templates for rendering product lists and details.
- **`users/`**: Handles user accounts, authentication, and profile management. This includes user models, registration and login views, and templates for user account-related pages.
- **`subscription/`**: Manages subscription plans and user subscription states. Includes the logic for creating subscription tiers, billing cycles, and integration with payment gateways.
- **`templates/`**: Contains HTML templates used across the platform, following the Django templating system for dynamic content rendering.
- **`static/`** & **`staticfiles/`**: Holds static assets like CSS, JavaScript, and images. These files are used to style the frontend and provide interactivity.
- **`media/`**: Stores uploaded media files, including digital products like e-books, videos, and software files, which are delivered to users upon purchase.
- **`.vscode/`**: Configuration files for Visual Studio Code to help streamline development within the IDE.
- **`LICENCE`**: The license file governing the terms under which this project can be used, copied, or modified.

## Requirements

- **Python 3.8+**
- **Django 3.x or higher**
- **PostgreSQL or SQLite for database management**
- **Redis or a similar caching system for handling sessions and caching**
- **Environment variables for sensitive data management** (such as API keys, database credentials)

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   ```

2. **Install dependencies**:

   Make sure to install all necessary Python packages by running:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:

   - Rename `.template.env` to `.env`.
   - Update the variables inside the `.env` file with your specific configuration, including database credentials, secret keys, and third-party API information.

4. **Apply database migrations**:

   The platform uses Django's migration system to handle database schemas. Run the following to apply the necessary migrations:

   ```bash
   python manage.py migrate
   ```

5. **Run the server**:

   Once everything is set up, you can start the local development server:

   ```bash
   python manage.py runserver
   ```

6. **Static files management**:

   Make sure to collect static files to serve them correctly:

   ```bash
   python manage.py collectstatic
   ```

## Usage

After setting up the project, you can access the platform at `http://127.0.0.1:8000/`. From there, you can:

- **Create products**: Through the admin dashboard, add new digital products, set prices, and categorize them.
- **Manage users**: Add and manage user accounts, subscriptions, and permissions.
- **Handle subscriptions**: Create subscription tiers and manage user access based on their subscription level.

## Deployment

This platform is built to be deployed on cloud-based platforms such as **Heroku**, **AWS**, or **DigitalOcean**. A **Procfile** and **runtime.txt** are provided for Heroku deployment, ensuring that your platform runs smoothly in a production environment.

To deploy:

1. Ensure all environment variables are set correctly on the hosting platform.
2. Run database migrations in the production environment:

   ```bash
   heroku run python manage.py migrate
   ```

3. Collect static files for production:

   ```bash
   heroku run python manage.py collectstatic --noinput
   ```

## Contributing

We welcome contributions from the community. If you'd like to contribute, please follow these guidelines:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push your branch (`git push origin feature-branch`).
5. Create a pull request.

## License

This project is licensed under the terms of the [LICENSE](LICENCE) file. You are free to use, modify, and distribute the software within the terms of the license.

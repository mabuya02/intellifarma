# SMART FARMING

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Database Configuration](#database-configuration)
- [Flask-Mail Setup](#flask-mail-setup)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

A Regression Model to Optimize Crop Selection for Kenya’s Staple Food Farmers.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/mabuya02/intellifarma.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-project
    ```

3. (Optional) Create and activate a virtual environment:

    ```bash
    python -m venv venv      # Create a virtual environment
    source venv/bin/activate  # Activate on Linux or macOS
    .\venv\Scripts\activate   # Activate on Windows
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```
5. Copy the .env.example to .env
    ```
    cp .env.example .env
    ```
6. Run the secret.py file to generate the secrete key then copy and paste it to your environment file
   ```
   python3 secret.py
   ```
   Copy paste the secret key into you env file
Certainly! Here's the information formatted into a README:

---
# Database Configuration

## Environment Variables

These variables are used to configure the database connection for your Flask application.

- `DB_HOST`: Set the host address of your database server.
- `DB_USERNAME`: Specify the username for database access.
- `DB_PASSWORD`: Enter the password for the specified database user.
- `DB_NAME`: Name of the database to be connected.

## Flask-Migrate

Flask-Migrate is a Flask extension that handles SQLAlchemy database migrations. Once you have configured your database details in your environment variables or a configuration file, you can use Flask-Migrate to manage database changes, migrations, and updates.

To use Flask-Migrate:

1. **Initialize Migrations**: Run the following command to initialize migrations in your Flask app:
    ```
    flask db init
    ```

2. **Generate a Migration**: When you make changes to your database models, generate a migration script using:
    ```
    flask db migrate -m "Your migration message"
    ```

3. **Apply the Migration**: Apply the generated migration script to update the database:
    ```
    flask db upgrade
    ```

Make sure to replace the placeholder values (DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME) with your actual database configuration.
 
## Flask-Mail Setup

Flask-Mail is a Flask extension used for sending emails from your Flask application. To set up Flask-Mail in your project, configure the following parameters in your environment variables or configuration file:

# Configuration Parameters

- `MAIL_SERVER`: The SMTP server address for your email provider.
- `MAIL_PORT`: The port number for the SMTP server (usually 587 for TLS).
- `MAIL_USERNAME`: Your email address used for sending emails.
- `MAIL_PASSWORD`: The password associated with your email account.
- `MAIL_USE_TLS`: Set to `True` to enable TLS encryption.
- `MAIL_USE_SSL`: Set to `False` to disable SSL.

Example Configuration (in `.env` file):

```dotenv
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME="your-email@gmail.com"
MAIL_PASSWORD="your-email-password"
MAIL_USE_TLS=True
MAIL_USE_SSL=False
```

Usage in Flask Application:

To use Flask-Mail within your Flask application, instantiate the `Mail` object with your app:


Remember to replace `'your-email@gmail.com'`with your actual email credentials.
You will obtain the email password from [generating an your-email-password](https://support.google.com/mail/answer/185833?hl=en) for the email you're using 

## Directory Structure
```plaintext 
intellifarma/
│
├── app/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── db_operations.py
│   ├── models.py
│   ├── routes.py
│   ├── services.py
│
├── migrations/
|
├── ml_model/
|   ├── smart_farmingmodel.py
│
├── venv/
│
├── .env
├── .env.example
├── .gitignore
├── config.py
├── LICENSE
├── README.md
├── requirements.txt
├── run.py
├── secret.py
```

## Contributing

If you would like to contribute to the project, follow these steps:

1. Fork the project.
2. Create your feature branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Open a pull request.

## License

This project is licensed under the [Your License Name] - see the [LICENSE.md](LICENSE.md) file for details.


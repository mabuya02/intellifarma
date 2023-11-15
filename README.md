# INTELLIFARMA

## Table of Contents

- [Installation](#installation)
- [Database Setup](#database-setup)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)
- [License](#license)

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
# Database Setup
SQLite (Default)
By default, the project uses SQLite as its database. No additional setup is required for SQLite.

PostgreSQL
If you want to use PostgreSQL as your database, follow these steps:

Install PostgreSQL on your machine.

Create a PostgreSQL database for your project.

Update the DATABASE_URL in your project's configuration. For example, in your .env file or as an environment variable:
```
DATABASE_URL=postgresql://your-username:your-password@localhost/your-database
```
Run the database migrations:
```
flask db upgrade
```

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

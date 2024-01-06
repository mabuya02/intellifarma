import secrets


class TerminalColors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

def create_env_file():
    # Path to .env.example and the new .env file
    env_example_path = '.env.example'
    env_file_path = '.env'
    
    print("\n")
    print(f"{TerminalColors.GREEN}---------------------------- Smart Payroll---------------------------------")
    print("\n")
    print("Configure your database to start using the application.")
    print("\n")

    # Read the .env.example file
    with open(env_example_path, 'r') as env_example:
        env_data = env_example.readlines()
        

    # Generate a secret key
    secret_key = secrets.token_hex(16)
    
 
    

    # Prompt the user for database credentials
    db_host = input("-> Enter the host address of your database server: ")
    db_port = input("-> Enter port address of you database server: ")
    db_username = input("-> Enter the username for database access: ")
    db_password = input("-> Enter the password for the specified database user: ")
    db_name = input("-> Enter the name of the database: ")

    
    for i in range(len(env_data)):
        if 'DB_HOST=' in env_data[i]:
            env_data[i] = f"DB_HOST=\"{db_host}\"\n"
        elif 'DB_PORT=' in env_data[i]:
            env_data[i] = f"DB_PORT=\"{db_port}\"\n\n"
        elif 'DB_USERNAME=' in env_data[i]:
            env_data[i] = f"DB_USERNAME=\"{db_username}\"\n"
        elif 'DB_PASSWORD=' in env_data[i]:
            env_data[i] = f"DB_PASSWORD=\"{db_password}\"\n"
        elif 'DB_NAME=' in env_data[i]:
            env_data[i] = f"DB_NAME=\"{db_name}\"\n"
        elif 'SECRET_KEY=' in env_data[i]:
            env_data[i] = f"SECRET_KEY=\"{secret_key}\"\n"
    
    print("\n")        
    print("-------------------------Mail Configuration-----------------------------------")
    print("\n")
    print("Configure your Flask-Mail to start using the application.") 
    print("\n") 
      
    mail_server=input("-> Enter you mail server: ")
    mail_port=input("-> Enter your mail port: ")
    mail_username=input("-> Enter your email address: ")
    mail_password=input("-> Enter your email password: ")
    mail_use_tls=input("-> TLS configuration (True / False): ")
    mail_use_ssl=input("-> SSL configuration (True / False): ")
    
    
    for j in range(len(env_data)):
        if 'MAIL_SERVER=' in env_data[j]:
            env_data[j] = f"MAIL_SERVER=\"{mail_server}\"\n"
        elif 'MAIL_PORT=' in env_data[j]:
            env_data[j] = f"MAIL_PORT=\"{mail_port}\"\n\n"
        elif 'MAIL_USERNAME=' in env_data[j]:
            env_data[j] = f"MAIL_USERNAME=\"{mail_username}\"\n"
        elif 'MAIL_PASSWORD=' in env_data[j]:
            env_data[j] = f"MAIL_PASSWORD=\"{mail_password}\"\n"
        elif 'MAIL_USE_TLS=' in env_data[j]:
            env_data[j] = f"MAIL_USE_TLS=\"{mail_use_tls}\"\n"
        elif 'MAIL_USE_SSL=' in env_data[j]:
            env_data[j] = f"MAIL_USE_SSL=\"{mail_use_ssl}\"\n"

    # Write the updated data to .env file
    with open(env_file_path, 'w') as env_file:
        env_file.writelines(env_data)
    print("\n")
    print("------------------------.env file created successfully.------------------------")

if __name__ == "__main__":
    create_env_file()

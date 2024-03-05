import hvac

# export HCP_CLIENT_ID=I4aYTuWFiJY0Dawz3bnCbam6UbDL75a7
# export HCP_CLIENT_SECRET=6Ew8ksFYKGQomS7jKikNv6z-1UysoccfW6AsVVUalIJOhU1HcS-unJxs98kGJn9i

# Initialize the Vault client
client = hvac.Client(url='http://vault-server-url:8200', token='your_vault_token')

# Path to the secret you want to retrieve
secret_path = 'secret/myapp/database'

try:
    # Retrieve the secret
    secret_data = client.read(secret_path)

    if secret_data is not None and 'data' in secret_data:
        # Extract the secret values
        secret_values = secret_data['data']

        # Do something with the secret values
        username = secret_values.get('username')
        password = secret_values.get('password')

        print("Username:", username)
        print("Password:", password)
    else:
        print("No data found at path:", secret_path)

except hvac.exceptions.InvalidPath:
    print("Invalid path:", secret_path)

except hvac.exceptions.Unauthorized as e:
    print("Authentication failed:", e)

except Exception as e:
    print("An error occurred:", e)

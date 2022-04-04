import json

# Enter your keys/secrets as strings in the following fields
credentials = {}
credentials['API_TOKEN'] = 'Qv0bf7i5Tsz7WUkjC2b9mOyHQ'
credentials['API_SECRET'] = 'sTvO1ofdG9T4EhlOSg4TOyMUk5ynF04h4vasgsrUCUfXdWK38j'
credentials['BEARER_TOKEN'] = 'AAAAAAAAAAAAAAAAAAAAAK9baAEAAAAAn0HM6TuTaIXCwfmpjbtXbC8zoP4%3DxmCHkdT6cW0wrM3vbWpkmH4AZkf4WIpkxiEAQcVJGC5AGBVlnl'
credentials['ACCESS_TOKEN'] = '1030131938428891136-7jhjuiKBpu6D99wrI5XvQ9Pqb6CgX5'
credentials['ACCESS_SECRET'] = 'gztTN2o8I8dM9Fd60RipOZssyUDYx044gmgGFrnkY63gf'

# Save the credentials object to file
with open("twitter/twitter_credentials.json", "w") as file:
    json.dump(credentials, file)
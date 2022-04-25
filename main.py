import pyshorteners

long_url = input("Enter the URL to shorten: ")

type_bitly = pyshorteners.Shortener(api_key="e260d7c67dc0f511e0187f426a57a8e971026ce8")
short_url = type_bitly.bitly.short(long_url)

print(f"The shortened URL is : {short_url}")


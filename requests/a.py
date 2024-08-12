import requests
from io import BytesIO
from PIL import Image

# URL of the image to download
url = r"https://upload.wikimedia.org/wikipedia/commons/1/15/Cat_August_2010-4.jpg"

# Send a GET request to the URL to retrieve the image
response = requests.get(url)

# Convert the response content into an image
img = Image.open(BytesIO(response.content))

# Display the image in a window
img.show()

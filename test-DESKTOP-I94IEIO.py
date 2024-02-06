import webbrowser
import time

# Replace 'https://example.com' with the URL you want to visit
url = 'https://aumscb.amrita.edu/cas/login?service=https%3A%2F%2Faumscb.amrita.edu%2Faums%2FJsp%2FCore_Common%2Findex.jsp'

# Infinite loop to keep visiting the link every 5 seconds
while True:
    # Open the URL in the default web browser
    webbrowser.open(url)

    # Wait for 5 seconds before visiting the link again
    time.sleep(5)

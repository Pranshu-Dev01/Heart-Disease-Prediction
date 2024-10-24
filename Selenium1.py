from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the Chrome WebDriver
driver = webdriver.Chrome(executable_path='path/to/chromedriver')

# Open the web application
driver.get('http://localhost:5000')  # Replace with your app's URL

# Fill in the input fields
driver.find_element(By.NAME, 'age').send_keys('63')  # Example input
driver.find_element(By.NAME, 'sex').send_keys('1')   # Example input

# Submit the form
driver.find_element(By.NAME, 'submit').click()

# Wait for the result to load
time.sleep(5)

# Capture the output
result = driver.find_element(By.ID, 'result').text
print("Prediction Result:", result)

# Close the browser
driver.quit()

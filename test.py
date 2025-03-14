import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize ChromeDriver with Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the webpage
driver.get("")

# Locate the username field by its ID and type the username
username_field = driver.find_element("id", "email")
username_field.send_keys("")  # Replace 'YourUsername' with actual input

# Locate the password field by its ID and type the password
password_field = driver.find_element("id", "password")
password_field.send_keys("")  # Replace 'YourPassword' with actual input

# Optionally, submit the form (if a submit button exists)
submit_button = driver.find_element(By.XPATH, "//button[@type='submit' and @aria-label='Submit']")
submit_button.click()

# Using CSS Selector
link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//a[@href="/power-ai"]'))
)
link.click()

input_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[class*="bg-[#F3F3F3"]'))
)
input_field.send_keys("Tell me more about AI Agents")

# Wait for the button to be clickable and click it
button =  driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/div/div[2]/div/div/div[2]/form/div/button')
button.click()

# Pause for 10 seconds before closing
time.sleep(60)

# Quit the browser after interaction
driver.quit()

'''
Using home page url (https://remote.co/), we extract urls of all categories,
then visit each category, there we find jobs in that category, we extract all the 
urls of jobs, then visit each url and extract details.
'''
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from get_selenium_driver import get_selenium_driver
from job_details import details_of_each_job_in_a_category
import boto3

# Function to store data in DynamoDB
def store_in_dynamodb(job_listings):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('job_listings_scraper')

    # Storing job listings in DynamoDB
    for category, jobs in job_listings.items():
        for job in jobs:
            table.put_item(Item=job)

driver = get_selenium_driver()
base_url = "https://remote.co/"
driver.get(base_url)
time.sleep(5) # Waiting for the page to load
job_listings = {}

# Categories are located under card, so we find all <a> elements with class "card"
try:
    job_category_card = driver.find_elements(By.CSS_SELECTOR, "a.card")
    # Store the href attributes of these elements in a list
    job_category_url_list = [a.get_attribute("href") for a in job_category_card]

    # Visit each category one by one
    for job_category_url in job_category_url_list:
        job_category = job_category_url.split('/')[-2]
        job_listings[job_category] = details_of_each_job_in_a_category(driver, job_category_url)
except (NoSuchElementException, StaleElementReferenceException, TimeoutException) as e:
    job_listings = {"Error": 'No category exists'}

print("Job Details scraped are as follows")
print("-------------------")
print(job_listings)
# Storing job listings in DynamoDB. Uncomment below line to use that.
# store_in_dynamodb(job_listings)
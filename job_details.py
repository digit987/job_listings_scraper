import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from get_selenium_driver import get_selenium_driver

def details_of_each_job_in_a_category(driver, job_category_url):
    driver.get(job_category_url)  # Visiting the URL
    time.sleep(5) # Waiting for the page to load

    try:
        # To get all jobs in a category, we find all <a> elements with class "card m-0 border-left-0 border-right-0 border-top-0 border-bottom"
        jobs_in_category = driver.find_elements(By.CSS_SELECTOR, "a.card.m-0.border-left-0.border-right-0.border-top-0.border-bottom")

        # Store the href attributes of these elements in a list
        url_of_jobs_in_category = [a.get_attribute("href") for a in jobs_in_category]
        time.sleep(5) # Waiting for the page to load
        
        job_details = []
        for each_job_url in url_of_jobs_in_category:
            driver.get(each_job_url)
            time.sleep(5) # Waiting for the page to load

            # Getting job title and company name
            try:
                job_and_company = driver.find_element(By.CSS_SELECTOR, "h1.font-weight-bold").text

                '''
                job_and_company gives us, for example, "Paid Digital Marketing Specialist at Colibri Group".
                Splitting it gives us title and company name
                '''

                job_and_company = job_and_company.split("at")
                job_title = job_and_company[0]
            except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
                job_title = "Job Title not found"

            # Getting location
            try:
                location = driver.find_element(By.CSS_SELECTOR, "div.location_sm.row > div.col-10.col-sm-11.pl-1").text
            except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
                location = "Location not found"

            # Getting salary
            try:
                salary = driver.find_element(By.CSS_SELECTOR, "div.salary_sm.row > div.col-10.col-sm-11.pl-1").text
            except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
                salary = "Salary not found"

            # Getting "time since posted"
            try:
                time_since_posted = driver.find_element(By.CSS_SELECTOR, "div.date_tags.row > div.col-10.col-sm-11.pl-1").text.split(" ago")[0] + " ago"
            except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
                time_since_posted = "Time since posted not found"

            # Getting company name
            try:
                company_name = driver.find_element(By.CSS_SELECTOR, "div.company_sm > div.name_sm > div.co_name").text
            except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
                company_name = "Company name not found"

            # Getting company logo url
            try:
                company_logo = driver.find_element(By.CSS_SELECTOR, "img.job_company_logo").get_attribute("src")
            except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
                company_logo = "Company logo not found"

            # Getting to parent job description container that contains other elements
            try:
                job_description_div = driver.find_element(By.CSS_SELECTOR, 'div.job_description')

                '''
                If successful, we move to other details inside "job description" that contains
                job description, job category, position overview, what you'll do, What you'll need to succeed
                '''

                # Getting job category
                try:
                    paragraphs = job_description_div.find_elements(By.CSS_SELECTOR, 'p')
                    job_category = paragraphs[4].text.split(": ")[0]
                except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
                    job_category = "Job category not found"

                # Getting job description
                try:
                    job_description = job_description_div.find_element(By.CSS_SELECTOR, 'div:nth-child(7)').text
                except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
                    job_description = "Job description not found"

                # Getting position overview
                try:
                    position_overview = job_description_div.find_element(By.CSS_SELECTOR, 'div:nth-child(10)').text
                except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
                    position_overview = "Position overview not found"

                # Getting what you'll do
                try:
                    what_you_will_do_list = job_description_div.find_element(By.CSS_SELECTOR, 'ul:nth-child(12)').find_elements(By.CSS_SELECTOR, 'li')
                    what_you_will_do = [item.text for item in what_you_will_do_list]
                except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
                    what_you_will_do = "What you will do not found"

                # Getting what you'll need to succeed
                try:
                    what_you_will_need_to_succeed_list = job_description_div.find_element(By.CSS_SELECTOR, 'ul:nth-child(14)').find_elements(By.CSS_SELECTOR, 'li')
                    what_you_will_need_to_succeed = [item.text for item in what_you_will_need_to_succeed_list]
                except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
                    what_you_will_need_to_succeed = "What you will need to succeed not found"

            except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
                job_description_div = "Job description not found"

            job_details.append(
                {
                    "job_category_url": job_category_url,
                    "job_url": each_job_url,
                    "job_title": job_title,
                    "location": location,
                    "salary": salary,
                    "time_since_posted": time_since_posted,
                    "company_name": company_name,
                    "company_logo": company_logo,
                    "job_category": job_category,
                    "job_description": job_description,
                    "position_overview": position_overview,
                    "what_you_will_do": what_you_will_do,
                    "what_you_will_need_to_succeed": what_you_will_need_to_succeed
                }
            )
    except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
        job_details.append({})
    
    return job_details

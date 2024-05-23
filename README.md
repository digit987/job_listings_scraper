# Remote Job Scraper

This project scrapes remote job listings from remote.co and stores them in DynamoDB.

## Setup

1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Ensure you have Chrome and ChromeDriver installed.
4. Set up AWS credentials for DynamoDB access.

## Running the Scraper

Run `python main.py` to scrape job listings and store them in DynamoDB.

## File Structure

- `main.py`: Main script to initiate scraping and DynamoDB storage.
- `job_details.py`: Functions to scrape details of each job listing.
- `get_selenium_driver.py`: Helper function to get a Selenium driver instance.
- `requirements.txt`: List of Python dependencies.
- `README.md`: Project documentation.

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

## Sample Output

{'marketing': [{'job_category_url': 'https://remote.co/remote-jobs/marketing/', 'job_url': 'https://remote.co/job/paid-digital-marketing-specialist-22/', 'job_title': 'Paid Digital Marketing Specialist ', 'location': 'Location: Remote, US', 'salary': 'Salary: $0', 'time_since_posted': 'Posted: 8 hours ago', 'company_name': 'Colibri Group', 'company_logo': 'https://remoteco.s3.amazonaws.com/wp-content/uploads/2023/09/01080102/Colibri-Logo-150x150.jpeg', 'job_category': 'Marketing', 'job_description': 'Colibri Group is building the future of professional education. Today, millions of licensed professionals start and advance their careers through the companys online and in-person learning solutions for licensing, continuing education, test preparation and professional development. Headquartered in St. Louis, Missouri, Colibri Group provides a holistic learning experience for students and professionals to achieve more and thrive throughout their careers in real estate, financial services, teacher education, healthcare, valuation and property services, among other professions. Visit colibrigroup.com for more information.', 'position_overview': 'The Colibri team is seeking a Paid Digital Marketing Specialist to help drive awareness, marketing qualified leads, and revenue at a target ROAS to our brand, SimpleNursing. This position is responsible for managing, expanding, and testing ad campaigns across search, social, display and YouTube. This fully remote position will report to the Director of Marketing for SimpleNursing.', 'what_you_will_do': ['Support the strategy, design, execution, and reporting of multi-channel paid advertising campaign activities.', 'Manage existing paid advertising campaigns across all paid advertising channels (search, social, display, and youtube), to achieve awareness, lead volume, and Revenue volume at a target cumulative ROAS.', 'Expand paid ad campaigns through audience, keyword, and competitive research.', 'Improve efficiency of campaign spend via A/B testing of ad copy, video content, campaign settings, campaign structure, bidding, and more optimizations.', 'Measure, analyze, and report on campaign performance as required and deliver regular campaign performance briefs to marketing leadership.', 'Leverage data to ascertain logical marketing segments and identify tactics to drive measurable business growth.'], 'what_you_will_need_to_succeed': ['3-5 years experience in paid digital demand generation role.', 'Experience conducting keyword research, building ad-groups, and optimizing campaigns toward down-funnel metrics.', 'Strong working knowledge of at least one of the following ad platforms: Google Ads, Microsoft/Bing Ads, Meta Ads, Tik Tok Ads.', 'Exceptional analytical skills of large data sets paired with a strong proficiency in Microsoft Excel/Google SheetsProven creative thinking that can generate and execute innovative marketing ideas for integrated campaigns.', 'Knowledge of marketing KPIs, such as ROAS, CPC, CPM, CTR, CVR, CPM and more.', 'A curious mindset to consistently A/B test and build a testing plan based on results.', 'Communication skills; demonstrable experience presenting results and recommendations to stakeholdersSelf-directed with an ability to work independently and cross-functionally; strong organizational and time-management skills a must.', 'Experience setting up, improving, and monitoring conversion tracking accuracy is a plus']}]}

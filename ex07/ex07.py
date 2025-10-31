import requests
from bs4 import BeautifulSoup
import sys
from datetime import datetime

def search_jobs():
    url = 'https://www.juniors.ro/jobs'

    try:
        print('Finding jobs from juniors.ro...')
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        job_list = soup.find('ul', class_="job_list")

        if not job_list:
            print('No jobs found.')
            return

        list_jobs = job_list.find_all('li', class_="job")

        if not list_jobs:
            print('No list of jobs found.')

        jobs = []
        for job in list_jobs[:7]:
            try:
                title = job.find('div', class_='job_header_title')
                company = job.find('strong', string='Companie:')
                tech = job.find('ul', class_='job_tags')
                location_and_postdate = title.find('strong') if title else None

                job_title = title.find('h3').text.strip() if title and title.find('h3') else 'N/A'

                company_name = 'N/A'
                if company:
                    company_name = company.parent.text.replace('Companie:', '').strip()

                if tech:
                    job_technologies = job.find('ul', class_ = 'job_tags')
                    technologies = [tech.text.strip() for tech in job_technologies if tech.text.strip()]

                if location_and_postdate:
                    location_and_postdate = location_and_postdate.text.strip()

                    string = location_and_postdate.split('|')

                    if len(string) >= 2:
                        location = string[0].strip()
                        post_date = string[1].strip()
                    else:
                        location = location_and_postdate
                        post_date = 'N/A'
                else:
                    location = 'N/A'
                    post_date = 'N/A'

                job_data = {
                    'title': job_title,
                    'company': company_name,
                    'location': location,
                    'technologies': technologies,
                    'post_date': post_date
                }

                jobs.append(job_data)

            except Exception as e:
                print(f"Error parsing job listing: {e}")
                continue

        print("\n" + "=" * 80)
        print("TOP 7 OPEN POSITIONS (Most Recent First)")
        print("=" * 80 + "\n")

        for i, job in enumerate(jobs, 1):
            print(f"#{i}")
            print(f"Job Title: {job['title']}")
            print(f"Company: {job['company']}")
            print(f"Location: {job['location']}")
            print(f"Technologies: {', '.join(job['technologies']) if job['technologies'] else 'Not specified'}")
            print(f"Posted: {job['post_date']}")
            print("-" * 80 + "\n")

        if not jobs:
            print("No jobs were successfully parsed. Please check the website structure.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    search_jobs()














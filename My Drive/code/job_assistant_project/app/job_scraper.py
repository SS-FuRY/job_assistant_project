from bs4 import BeautifulSoup
import requests

def search_jobs(role, location):
    jobs = []

    base_url = "https://www.indeed.com/jobs"
    params = {
        "q": role,
        "l": location,
        "limit": 10
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(base_url, params=params, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    for job_card in soup.find_all('a', class_='tapItem'):
        title = job_card.find('h2', class_='jobTitle')
        company = job_card.find('span', class_='companyName')
        location = job_card.find('div', class_='companyLocation')
        link = "https://www.indeed.com" + job_card.get('href')

        if title and company and location:
            jobs.append({
                "title": title.text.strip(),
                "company": company.text.strip(),
                "location": location.text.strip(),
                "link": link
            })

    return jobs

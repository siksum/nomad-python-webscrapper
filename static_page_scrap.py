import requests
from bs4 import BeautifulSoup

all_jobs = []

def get_page_number(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser", )
    return len(soup.find("div", class_="pagination").find_all("span", class_="page"))

def scrape_page(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser", )
    # jobs = soup.find("section", id="category-2")
    jobs = soup.find("section", class_="jobs").find_all("li")[:-1]

    for job in jobs:
        if job.find("span", class_="title") and job.find("span", class_="region") :
            title = job.find("span", class_="title").text   
            region = job.find("span", class_="region").text
            company, position, _ = job.find_all("span", class_="company")
            company = company.text
            position = position.text
            link = job.find("a")["href"]
            job_data = {
                "title": title,
                "region": region,
                "company": company,
                "position": position,
                "link": "https://weworkremotely.com" + link
            }
            all_jobs.append(job_data)
url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"

scrape_page(url)

print(all_jobs)
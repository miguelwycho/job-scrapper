from bs4 import BeautifulSoup
import requests
from models.job import JobModel

def get_job_from_info_jobs():
    p = "analista"
    cidade = 'sao-paulo'
    URL = "https://www.infojobs.com.br/vagas-de-emprego-"+ p +"-em-" + cidade + ".aspx"
    
    page = requests.get(URL+p)
    soup = BeautifulSoup(page.content,'html.parser')
    results = soup.find(id='ctl00_phMasterPage_cGrid_divGrid')
    job_elems = results.find_all('div',class_='element-vaga')
    job_list:[JobModel] = []
    for job_elem in job_elems:
        company_elem = job_elem.find('div', class_='vaga-company')
        title_elem = job_elem.find('a', class_='vagaTitle')
        area_elem = job_elem.find('p',class_='area')
        location_elem = job_elem.select('p > span', class_='location2')[1]
        desc_elem = job_elem.find('div',class_='vagaDesc')
        # url_elem = job_elem.find('div > a', class_='vagaDesc')[0]['href']
        title = title_elem['title']
        company = company_elem.text.strip()
        area = area_elem['title']
        location = location_elem['title']
        description  = desc_elem.text.strip()
        new_job = JobModel(title,company,location,description,'url_elem',area)
        job_list.append(new_job)
    return job_list



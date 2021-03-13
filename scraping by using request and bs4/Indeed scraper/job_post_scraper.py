#import all required modules/libraries
import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup  
from time import sleep
        
#get_url funct will return url
def get_url(jobName="",city="",jobType="",daysOld=""):
    jobName = jobName.replace(' ','+')
    template = 'https://pk.indeed.com/jobs?q='+f'{jobName}&l={city}&jt={jobType}&fromage={daysOld}'
    return template
 
#get_record funct will return extracted data in form of tuple     
def get_record(item):
    
    jobTitle = item.h2.a.get('title')

    link = 'https://pk.indeed.com'+item.h2.a.get('href')

    company = item.find('span','company').text.strip()

    city_Name = item.find('div','recJobLoc').get('data-rc-loc') 

    summary = item.find('div','summary') # .strip() function use to remove extra white spaces
    summary = summary.text.strip()

    daysOld = item.find('span','date').text

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    current_date = datetime.today().strftime('%d/%m/%y')

    try:
        salaryRange = item.find('span','salary').text.strip()
    except AttributeError:
        salaryRange = ""
        
    result = (current_date,current_time,jobTitle,company,city_Name,salaryRange,summary,daysOld,link)
    
    return result

#main funct
def main(jobName="",city="",jobType="",daysOld=""):
    records = []
    url = get_url(jobName,city,jobType,daysOld)
    
    while True:
        r = requests.get(url)   
        sleep(3)
     
        soup = BeautifulSoup(r.text,'html.parser')

        results = soup.find_all('div','jobsearch-SerpJobCard')#results variable contain all the results selectors
    
        for item in results:
            record = get_record(item)
            records.append(record)
            
        try:
            url = 'https://pk.indeed.com'+soup.find('a',{"aria-label":'Next'}).get('href')
        except AttributeError:
            break
            
    with open(f'{jobName}_result.csv','w',newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Extract Date','Extract Time','Job Name','Company Name','City Name','Job Salary','Description','Job Posted Time Ago','Job Url'])
        writer.writerows(records)

#code initialize
if __name__ == '__main__':
    jobName = input('Enter The name of job : ')
    city  = input('Enter The name of city : ')
    jobType = input('Enter the Job type : ')
    daysOld = input('how Old job posted : ')

    main(jobName,city,jobType,daysOld)
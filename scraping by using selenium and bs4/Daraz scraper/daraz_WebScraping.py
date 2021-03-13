#importing all required modules/libraries
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

#get_url will return url
def get_url(search_term,no):
    search_term = search_term.replace(' ','+')
    template = 'https://www.daraz.pk/catalog/?&page='+f'{no}&q={search_term}'
    return template

#extract_record will return extracted data in form of tuple
def extract_record(item):
    name = item.find('div','c16H9d').text#.strip() 

    link = item.find('a',{"age":'0'}).get('href')
    
    try:
        price = item.find('span',class_='c13VH6').get_text() #item.find('span','a-offscreen')
    except AttributeError:
        price = 'N/A'
    

# if we only need tags then we dont need to use find function
    try:
        r1 = item.find_all('i','c3EEAg')#item.find('i').text 1
        r2 = item.find_all('i','c17YMy')#.8
        r3 = item.find_all('i','c1dtTC')#.0
        r4 = item.find_all('i','c1Zozd')#.1
        r5 = item.find_all('i','c3An30')#.5
        r6 = item.find_all('i','c1e2gb')#.4
        r7 = item.find_all('i','c1wCjy')#.7
        r8 = item.find_all('i','c3DcGB')#.6
        r9 = item.find_all('i','cbDGcO')#.2
        r10  = item.find_all('i','c3fsPU')#.3
        r11 = item.find_all('i','cF1vkb')#.9
        #print(f'{len(r1)} + {(len(r2)*0.8)} + {(len(r3)*0)} + {(len(r4)*0.1)} + {(len(r5)*0.5)} + {(len(r6)*0.4)} + {(len(r7)*0.7)} + {(len(r8)*0.6)} + {(len(r9)*0.2)} + {(len(r10)*0.3)} + {(len(r11)*0.9)}')
        rating = len(r1) + (len(r2)*0.8) + (len(r3)*0) + (len(r4)*0.1) + (len(r5)*0.5) + (len(r6)*0.4) + (len(r7)*0.7) + (len(r8)*0.6) + (len(r9)*0.2) + (len(r10)*0.3) + (len(r11)*0.9)
    except AttributeError:    
        rating = 'N/A'

    try:
        review_count = item.find('span','c3XbGJ').get_text()
    except AttributeError:
        review_count = 'N/A'
        
    result = (name,price,rating,review_count,link)
    return result

#main funct
def main(search_term):
    records = []
    
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    #for loop for pages
    for no in range(1,103):
        url = get_url(search_term,no)
        driver.get(url)
        sleep(5)

        soup = BeautifulSoup(driver.page_source,'html.parser')
    
        results = soup.find_all('div','c2prKC')
        #for loop for extracting all results records
        for item in results:
            record = extract_record(item)
            if record:
                records.append(record)
    
    driver.close()

    #all the record will be stored in a results.csv file
    with open(f'results/{search_term}_results.csv','w',newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Name','Price','Rating','Review Counts','link'])
        writer.writerows(records)
        
       
if __name__ == '__main__':    
    search_term = input("Search Product: ")
    main(search_term)
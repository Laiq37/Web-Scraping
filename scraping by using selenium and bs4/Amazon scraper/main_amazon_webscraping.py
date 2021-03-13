#importing all required modules/libraries
import csv
from bs4 import BeautifulSoup
from selenium import webdriver

#get_url will return url
def get_url(search_term,no):
    search_term = search_term.replace(' ','+')
    template = 'https://www.amazon.com/s?k='+f'{search_term}&ref=nb_sb_noss_2&page={no}'
    return template

#extract_record will return extracted data in form of tuple
def extract_record(item):
    tag = item.h2.a
    name = tag.text.strip() #name = tag.get_text() 

    link = 'https://www.amazon.com/'+tag.get('href')
    
    try:
        price = item.find('span',class_='a-offscreen').get_text() #item.find('span','a-offscreen')
    except AttributeError:
        price = 'N/A'
    

# if we only need tags then we dont need to use find function
    try:
        rating = item.i.text#item.find('i').text
    except AttributeError:
        rating = 'N/A'

    try:
        review_count = item.find('div','a-spacing-top-micro').find('span',{"class":'a-size-base',"dir":'auto'}).get_text()
    except AttributeError:
        review_count = 'N/A'
        
    result = (name,price,rating,review_count,link)
    return result

#main funct
def main(search_term,page = 21):
    records = []
    
    
    #options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")
    
    #for loop for pages
    for no in range(1,page):
        url = get_url(search_term,no)
        driver.get(url)
    
        soup = BeautifulSoup(driver.page_source,'html.parser')
    
        results = soup.find_all('div',{"data-component-type":'s-search-result'})
        
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
    while True:
        search_term = input("Search Product: ")
        if search_term == "":
            inp = input('Want to search other item? If yes press any character and then enter otherwise press enter only : ')
            if inp == "":
                break
        else:
            main(search_term)
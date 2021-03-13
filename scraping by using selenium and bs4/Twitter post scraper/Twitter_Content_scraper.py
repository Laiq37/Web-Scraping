#importing all required modules/libraries
import csv
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome

#loggig out function
def log_out():
    sleep(2)

    driver.find_element_by_xpath('.//div[@data-testid="SideNav_AccountSwitcher_Button"]').click()

    sleep(2)

    driver.find_element_by_xpath('.//a[@href="/logout"]').click()

    sleep(2)

    driver.find_element_by_xpath('.//div[@data-testid="confirmationSheetConfirm"]').click()
    driver.close()

#get_tweet_data will return content related data    
def get_tweet_data():
    
    Tweeter_name = post.find_element_by_xpath('.//span/span').text

    Tweeter_username = post.find_element_by_xpath('.//span[contains(text(),"@")]').text
    try:
        Tweet_post_time = post.find_element_by_xpath('//time').get_attribute('datetime')
    except NoSuchElementException:
        Tweet_post_time=''

    try:
        post.find_element_by_xpath('.//div[contains(text()),"Replying to"]').text
        Tweet_content = post.find_element_by_xpath('./div[2]/div[2]/div[2]//div').text
    except NoSuchElementException:
        Tweet_content = post.find_element_by_xpath('./div[2]/div[2]/div').text
        
    like = post.find_element_by_xpath('.//div[@data-testid="like"]').text
    reply_count = post.find_element_by_xpath('.//div[@data-testid="reply"]').text
    retweet =post.find_element_by_xpath('.//div[@data-testid="retweet"]').text

    return (Tweeter_name,Tweeter_username,Tweet_post_time,Tweet_content,like,reply_count,retweet)

#main function
def main():
    my_username = input('Enter your username: ')
    my_password = getpass('Enter your Twitter Password : ')
    search_term = input("Search here")

    driver = Chrome(executable_path="chromedriver.exe")

    driver.get('https://twitter.com/login')

    username = driver.find_element_by_xpath('.//input[@name="session[username_or_email]"]')
    username.send_keys(my_username')

    sleep(2)

    password = driver.find_element_by_xpath('.//input[@name="session[password]"]')
    password.send_keys(my_password)

    sleep(2)

    password.send_keys(Keys.RETURN)

    sleep(2)

    search = driver.find_element_by_xpath('.//input[@aria-label="Search query"]')
    search.send_keys(search_term)
    sleep(1)
    search.send_keys(Keys.RETURN)

    sleep(2)

    #latest
    driver.find_element_by_link_text('Latest').click()

    sleep(2)

    #latest
    driver.find_element_by_link_text('Latest').click()

    sleep(2)

    tweet_data = [] #it will store tuple of extracted tweet data
    tweet_ids = set()
    last_postion = driver.execute_script("return window.pageoffset;")
    scrolling = True

    while scrolling :
        #getting_post
        posts = driver.find_elements_by_xpath('.//div[@data-testid="tweet"]')
        for post in posts[-15:]:
            data = get_tweet_data()
            
            tweet_id = ''.join(data)
            if tweet_id not in tweet_ids:
                tweet_ids.add(tweet_id)
                tweet_data.append(data)
                
        scroll_attempt = 0
        while True:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            sleep(2)
            current_postion = driver.execute_script("return window.pageoffset;")
            
            if last_postion == current_postion:
                
                scroll_attempt += 1
                
                if scroll_attempt == 2:
                    scrolling = False
                    break
                else:
                    sleep(2) #attemp to scroll again
            else:
                last_postion = current_postion
                break
    log_out()
    
    #all the record will be stored in a results.csv file
    with open(f'{search_term}_related_tweet.csv','w',newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Accout Name','User Name','Timestamp','Contents','Likes','Comments','Retweets'])
        writer.writerows(tweet_data)
#loggig out function

if __name__ == '__main__':
    main()
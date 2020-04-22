from time import sleep
from selenium import webdriver

# Open up chrome webdriver and direct to the quiz
driver = webdriver.Chrome(executable_path=r'/mnt/c/tools/chromedriver.exe')
driver.get("https://remeeting:quiz@remeeting.com/quiz/")

## Iterate over all the possible numbers
for i in range (0, 1000):
    # Find the Element called numbers
    num = driver.find_element_by_name("number")

    # Enter in the number where are trying
    num.send_keys(str(i))

    #Click Submit
    driver.find_element_by_xpath("//input[@value='Submit']").click()

    #Copy and print out the html result
    x = driver.find_element_by_tag_name('body')
    print(x.text)

    #return back to the page and try again
    driver.find_element_by_link_text("OK, go back...").click()







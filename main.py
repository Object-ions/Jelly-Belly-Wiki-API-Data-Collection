from selenium import webdriver
chrome_path = "/usr/local/bin/chromedriver"

driver = webdriver.Chrome(chrome_path)

driver.get("https://www.jellybelly.com/jelly-belly-single-flavors")
driver.find_element_by_xpath("""//*[@id="7up"]""").click()

posts = driver.find_elements_by_xpath("""//*[@id="flavor-content"]/div""")
for post in posts:
  print(post.text)
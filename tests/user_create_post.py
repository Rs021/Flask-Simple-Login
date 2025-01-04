from selenium import webdriver
from selenium.webdriver.common.by import By
import random

def gen_content():

    raw_content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque libero diam, sagittis ut fermentum vitae, placerat ac lacus. Proin eu felis risus. Phasellus tincidunt ligula dolor, at placerat justo egestas ac. Nullam at dignissim lorem, vitae hendrerit felis. Sed rutrum nisi vitae elit semper lacinia. Phasellus ut libero id velit luctus posuere. Integer sollicitudin orci sit amet leo rutrum, in molestie quam tristique. Donec vitae dictum ex, ac euismod tellus. Aliquam vel diam viverra, maximus mi rutrum, commodo mi. Phasellus vestibulum ornare tortor. Nunc euismod, est lacinia euismod viverra, urna lorem egestas sem, at scelerisque eros ipsum in elit. Aliquam sodales ultricies lacus, in porttitor ex tristique sed. Vestibulum hendrerit elit nec massa pellentesque, et aliquam dolor ornare. Nam luctus ac erat a posuere.
Aliquam rutrum felis ac velit ornare auctor. Suspendisse felis ex, rhoncus id mollis aliquet, ultrices ut erat. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec sodales interdum nunc. Nullam laoreet hendrerit porttitor. Aliquam ultrices arcu nec quam venenatis, sit amet ornare ipsum porta. Curabitur quis ultrices orci, rhoncus pharetra risus. Nullam interdum non dui eget interdum. Cras in mi iaculis, scelerisque massa non, viverra eros.
Vestibulum sodales, neque vitae maximus porta, nibh massa fermentum nulla, et egestas arcu velit sit amet nisi. Vestibulum euismod lobortis justo non pharetra. Morbi vestibulum in arcu id ullamcorper. Sed elementum lorem arcu, vitae commodo odio fermentum a. Aliquam pretium ultrices neque vitae auctor. Ut vitae tellus feugiat, vehicula mi nec, convallis eros. Morbi hendrerit sem neque, in laoreet elit interdum in. Aliquam ut turpis eget orci consectetur dictum. Nam sed sapien quam. Pellentesque ex velit, pharetra in odio hendrerit, molestie sollicitudin ante. Ut neque nisi, viverra a finibus vitae, accumsan vitae libero.
Proin mauris nunc, scelerisque non augue eget, interdum egestas purus. Fusce rutrum, ligula tempus bibendum interdum, ante urna condimentum sem, eu auctor neque diam et ante. Cras ullamcorper massa at suscipit hendrerit. Curabitur tincidunt, augue vel scelerisque egestas, nisi nibh congue enim, quis condimentum dolor est et urna. Cras erat dui, tincidunt ac vehicula in, blandit ac justo. Aliquam erat volutpat. Nulla et massa efficitur, porttitor urna eu, hendrerit nunc. Integer sollicitudin ipsum nec velit venenatis ornare. Sed elementum consectetur enim, eu sagittis tellus tristique non. Vivamus quis libero enim. Donec pharetra lectus sollicitudin quam varius dignissim. Sed gravida consequat est, non porttitor lorem cursus at."""

    content = []

    for i in raw_content.splitlines():
        content.append(i)

    return content

def create_new_user(driver: webdriver):
    click_to_login = driver.find_element(by=By.ID, value='login-btn')

    driver.implicitly_wait(2)

    click_to_login.click()

    driver.implicitly_wait(2)

    click_register = driver.find_element(by=By.ID, value="register")

    driver.implicitly_wait(2)

    click_register.click()

    form_user = driver.find_element(by=By.ID, value='user')
    form_pass = driver.find_element(by=By.ID, value='pass')
    form_sub = driver.find_element(by=By.ID, value='sub')

    form_user.send_keys("bot")
    form_pass.send_keys('123')

    form_sub.click()

def do_login(driver):

    click_login = driver.find_element(by=By.ID, value='login-btn')

    click_login.click()

    form_user = driver.find_element(by=By.ID, value='form3Example3')
    form_pass = driver.find_element(by=By.ID, value='form3Example4')

    form_sub = driver.find_element(by=By.ID, value='sub-btn')

    form_user.send_keys('bot')
    form_pass.send_keys('123')

    form_sub.click()


content = gen_content()

driver = webdriver.Firefox()

driver.get('http://127.0.0.1:5000/')


do_login(driver)

for i in range(100):
    click_new_post = driver.find_element(by=By.ID, value='create-post')
    click_new_post.click()

    form_title = driver.find_element(by=By.NAME, value='title')
    form_content = driver.find_element(by=By.NAME, value='content')
    form_sub = driver.find_element(by=By.ID, value='sub-btn')

    form_title.send_keys('Bot Title')

    ct = content[random.randint(0, 3)]
    form_content.send_keys(f'{ct}')

    form_sub.click()

driver.quit()












from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint
import openpyxl

wb = openpyxl.load_workbook("users_list.xlsx")   # find excel spreadsheet
followed_all_time_ws = wb['followed_all_time']

geckodriver_path = 'C:\\Users\\antho\\Documents\\Code Projects\\Resources\\geckodriver-v0.24.0-win64(1)\\geckodriver.exe'
webdriver = webdriver.Firefox(executable_path=geckodriver_path)



webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('###Password###')
password = webdriver.find_element_by_name('password')
password.send_keys('###Username###')
sleep(2)

try:    # find login button
    login_button = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > button')
except:
    login_button = webdriver.find_element_by_css_selector('.L3NKy')
login_button.click()
sleep(3)


try:   # find "not now" button
    notnow = webdriver.find_element_by_class_name('HoLwm')
    sleep(randint(2, 3))
except:
    webdriver.refresh()
    sleep(randint(2, 3))
    notnow = webdriver.find_element_by_class_name('aOOlW')
    sleep(randint(2, 3))
notnow.click()



choice, amount = input("Type 'follow' or 'unfollow' and the number of accounts you'd like to interact with (ex. 'follow 50', 'unfollow 200'. Note that "
      "interacting with more than 250 accounts in 24 hours will have your account flagged by instagram.").split()

amount = int(amount)


if choice == 'unfollow':

    for i in range(0, amount):
        x = 1
        while followed_all_time_ws["A" + str(x)].value is not None:  # begin at first empty row
            x = x + 1

    my_username = webdriver.find_element_by_class_name("gmFkV")
    my_username.click()
    sleep(randint(2, 3))

    my_followers_button = webdriver.find_element_by_partial_link_text("following")
    my_followers_button.click()
    sleep(randint(2, 3))

    my_follower_count_str = webdriver.find_element_by_xpath("/html/body/span/section/main/div/header/section/ul/li[3]/a/span").text.replace(',', '')
    my_follower_count = int(my_follower_count_str)

    followed_names = webdriver.find_elements_by_class_name("_0imsa")
    following_buttons = webdriver.find_elements_by_class_name("sqdOP")

    for i in range(1, amount):
        print("archived and unfollowed ", followed_names[i].text)
        followed_all_time_ws[i + int(x)] = followed_names[i].text
        following_buttons[i-1].click()

        followed_all_time_ws["A" + str(i + x)] = "bingo " + str(i + x)

wb.save("users_list.xlsx")


if choice == "follow":

    hashtag_list = ['poppunk', 'guitar', 'garageband']

    new_followed = []
    tag = -1
    followed = 0
    likes = 0
    comments = 0

    for hashtag in hashtag_list:

        tag = tag + 1
        print('current hashtag:', hashtag_list[tag])
        webdriver.get('https://www.instagram.com/explore/tags/' + hashtag_list[tag] + '/')
        sleep(randint(5, 10))
        first_thumbnail = webdriver.find_element_by_class_name('eLAPa')

        first_thumbnail.click()
        sleep(randint(1, 2))


        # Comments and tracker
        new_followed = []
        followed = 0
        likes = 0
        comments = 0

        for x in range(amount):

            try:

                if webdriver.find_element_by_css_selector('.oW_lN').text == 'Follow':

                    webdriver.find_element_by_css_selector('.oW_lN').click()
                    followed += 1

                    # Liking the picture
                    try:
                        webdriver.find_element_by_css_selector('.coreSpriteHeartOpen').click()
                        likes += 1
                        sleep(randint(3, 5))
                    except:
                        webdriver.find_element_by_css_selector('.fr66n > button:nth-child(1) > span:nth-child(1)').click()
                        likes += 1
                        sleep(randint(3, 5))

                    # Comments and tracker
                    comm_prob = randint(1, 10)
                    print('post {} of #{}: comment value:{}'.format(x, hashtag, comm_prob))
                    if comm_prob > 7:
                        comments += 1
                        webdriver.find_element_by_css_selector('._15y0l > button:nth-child(1)').click()
                        comment_box = webdriver.find_element_by_css_selector('.Ypffh')

                        if comm_prob < 7:
                            sleep(1)
                        elif (comm_prob > 6) and (comm_prob < 9):
                            comment_box.send_keys('Nice work :)')
                            sleep(1)
                        elif comm_prob == 9:
                            comment_box.send_keys('Nice gallery!!')
                            sleep(1)
                        elif comm_prob == 10:
                            comment_box.send_keys('So cool! :)')
                            sleep(1)
                        # Enter to post comment
                        comment_box.send_keys(Keys.ENTER)
                        sleep(randint(10, 20))

                # Next picture
                webdriver.find_element_by_link_text('Next').click()
                sleep(randint(2, 6))

            except:
                sleep(randint(10, 15))
                webdriver.find_element_by_link_text('Next').click()
                print('Picture Load Fail, Skipping to Next Image.')
                sleep(randint(2, 6))

        print('----------------------------------------------------------------------')
        print('Liked {} photos.'.format(likes))
        print('Commented on {} photos.'.format(comments))
        print('Followed {} new people.'.format(followed))
        print('----------------------------------------------------------------------')

# InstagramAutomation
Uses Selenium Webdriver for Firefox for browser automation and Openpyxl for data storage and maniupulation. Drops likes,follows and unfollows, and leaves comments!


There needs to be an excel file named "users_list.xlsx" file as well as the geckodriver application in the same directory as the program for it to run.

If too many accounts are followed in a short time period, Instagram will stop you from following and the "follow" button will still say "follow" when clicked (instead of "following"), but the bot continues to try and click the button. In the future it will check for this and stop after the first time it happens, because instagram will lengthen the shadow-ban and even perma-ban accounts if they try to follow too much during a shadow-ban.

Unfollow feature doesn't work, there is an element blocking the unfollow buttons. Will be patched in the future.

Original implementation of this bot is here; https://towardsdatascience.com/increase-your-instagram-followers-with-a-simple-python-bot-fde048dce20d

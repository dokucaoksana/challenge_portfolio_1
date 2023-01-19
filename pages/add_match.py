from pages.base_page import BasePage


class Add_match(BasePage):
    email_xpath = "//*[@name = 'email']"
    phone_xpath = "//*[@name = 'phone']"
    name_xpath = "//*[@name = 'name']"
    surname_xpath = "//*[@name = 'surname']"
    weight_xpath = "//*[@name = 'weight']"
    height_xpath = "//*[@name = 'height']"
    club_xpath = "//*[@name = 'club']"
    level_xpath = "//*[@name = 'level']"
    mainpos_xpath = "//*[@name = 'mainPosition']"
    secondpos_xpath = "//*[@name = 'secondPosition']"
    achievements_xpath = "//*[@name = 'achievements']"
    age_xpath = "//child::div[2]/form/div[2]/div/div[7]/div/div/input"
    leg_xpath = "//*[@id='mui-component-select-leg']"
    district_xpath = "//*[@id='mui-component-select-district']"


    pass

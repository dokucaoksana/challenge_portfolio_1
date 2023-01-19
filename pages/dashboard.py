from pages.base_page import BasePage


class Dashboard(BasePage):
    dev_contact_xpath = "//*[text()='Dev team contact' and @class = 'MuiButton-label']"
    add_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a"
    last_created_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[1]/button"
    mainpage_xpath = "//*[text() = 'Main page']"
    players_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]"
    language_xpath = "//child::ul[2]/div[2]/div[2]/span"
    signout_xpath = "//child::ul[2]/div[2]/div[2]"
    last_updated_player_xpath = "//child::div[3]/div[3]/div/div/a[2]/button"
    last_created_match_xpath = "//child::div[3]/div[3]/div/div/a[3]/button"
    last_updated_match_xpath = "//child::div[3]/div[3]/div/div/a[4]/button"
    last_updated_report_xpath = "//child::div[3]/div[3]/div/div/a[5]/button"


pass

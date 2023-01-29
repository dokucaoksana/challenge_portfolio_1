import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en'
    main_page_button_xpath = "//span[normalize-space()='Main page']"
    players_button_xpath = "//span[normalize-space()='Players']"
    select_lang_xpath = "//span[normalize-space()='Polski']"
    sign_out_button_xpath = "//span[normalize-space()='Sign out']"
    dev_team_button_xpath = "//span[normalize-space()='Dev team contact']"
    add_player_button_xpath = "//span[normalize-space()='Add player']"
    last_created_player_xpath = "//span[normalize-space()='Robbie Lewandowski']"
    last_updated_player_xpath = "//span[normalize-space()='-2mm Ronaldo']"
    last_created_match_xpath = "//span[contains(text(),'lech')]"
    last_updated_report_xpath = "//span[normalize-space()='Julx err']"
    dashboard_expected_title = "Scouts panel"


    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_add_a_player(self):
        self.click_on_the_element(self.add_player_button_xpath)




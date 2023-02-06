import time

from pages.base_page import BasePage


class AddAMatch(BasePage):
    expected_title = "Add player"
    add_a_match_form_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    main_page_button_xpath = " //*[text()='Main page']"
    add_player_text_xpath = "//*[contains(@class, 'MuiTypography-h5')]"
    date_input_xpath = "//input[@type='date']"
    email_input_xpath = "//*[@name='email']"
    name_input_xpath = "//input[@name='name']"
    age_input_xpath = "//input[@name='age']"
    main_position_input_xpath = "//input[@name='mainPosition']"
    surname_input_xpath = "//input[@name='surname']"
    youtube_button_xpath = "//div[19]/button/span[1]"
    youtube_fill_line_xpath = "//input[@name='webYT[0]']"
    youtube_delete_text_xpath = "//div[19]/div/button/span[1]"
    sign_out_button_xpath = "//ul[2]/div[2]/div[2]/span"
    players_button_xpath = "//ul[1]/div[2]/div[2]/span"
    submit_button_xpath = "//div[3]/button[1]/span[1]"
    leg_scroll_list_xpath = "//*[@id='mui-component-select-leg']"
    right_leg_xpath = "//*[@data-value='right']"
    language_scroll_xpath = "//ul[2]/div[1]/div[2]/span"
    pass

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.add_a_match_form_url) == self.expected_title

    def filling_a_form(self, email, name, surname, age, mainPosition):
        self.field_send_keys(self.email_input_xpath, email)
        self.field_send_keys(self.name_input_xpath, name)
        self.field_send_keys(self.surname_input_xpath, surname)
        self.field_send_keys(self.age_input_xpath, age)
        self.field_send_keys(self.main_position_input_xpath, mainPosition)
        self.click_on_the_element(self.submit_button_xpath)

    def main_button_is_visible(self):
        self.wait_for_visibility_of_element_located(self.main_page_button_xpath)

    def choosing_the_leg(self):
        self.click_on_the_element(self.leg_scroll_list_xpath)
        self.click_on_the_element(self.right_leg_xpath)

    def language_change(self):
        self.click_on_the_element(self.language_scroll_xpath)

    def youtube_fill_and_delete_text(self, text):
        self.click_on_the_element(self.youtube_button_xpath)
        self.field_send_keys(self.youtube_fill_line_xpath, text)
        self.click_on_the_element(self.youtube_delete_text_xpath)

    def signing_out(self):
        self.click_on_the_element(self.sign_out_button_xpath)

    def go_on_players_page(self):
        self.click_on_the_element(self.players_button_xpath)

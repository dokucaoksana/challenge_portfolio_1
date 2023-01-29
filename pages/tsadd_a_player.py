from pages.base_page import BasePage

class AddPlayer(BasePage):
    email_field_xpath = "//input[@name='email']"
    name_field_xpath = "//input[@name='name']"
    surname_field_xpath = "//input[@name='surname']"
    phone_field_xpath = "//input[@name='phone']"
    weight_field_xpath = "//input[@name='weight']"
    height_field_xpath = "//input[@name='height']"
    leg_dropdown_xpath = "//div[@id='mui-component-select-leg']"
    club_field_xpath = "//input[@name='club']"
    level_field_xpath = "//input[@name='level']"
    main_position_field_xpath = "//input[@name='mainPosition']"
    second_position_field_xpath = "//input[@name='secondPosition']"
    district_dropdown_xpath = "//input[@name='secondPosition']"
    achievements_xpath = "//input[@name='achievements']"
    age_picker_xpath = "//input[@name='age']"
    add_language_button_xpath = "//span[normalize-space()='Add language']"
    ball_connect_field_xpath = "//input[@name='webLaczy']"
    nine_zero_minutes_xpath = "//input[@name='web90']"
    fb_field_xpath = "//input[@name='webFB']"
    youtube_link_button_xpath = "//button[@aria-label='Add link to Youtube']"
    submit_button = "//span[normalize-space()='Submit']"
    clear_button = "//span[normalize-space()='Clear']"
    add_player_page_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    add_player_expected_title = "Add player"

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.age_picker_xpath, age)

    def type_in_main_position(self, position):
        self.field_send_keys(self.main_position_field_xpath, position)

    def click_submit(self):
        self.click_on_the_element(self.submit_button)

    def title_of_add_player_page(self):
        assert self.get_page_title(self.add_player_page_url) == self.add_player_expected_title

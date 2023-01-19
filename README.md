# Task 1: Software configuration. #
### Subtask 1: Why did I choose to participate in the Dare IT Challenge?
1. I had an experience in manual testing at my previous job and I really enjoy that process, but repeating all of these steps can cost a lot of time and effort. 
2. I want to have the ability to reduce the time to run tests and get new knowledge, of course. 
3. I believe that project can help me with my goal. 

----

###### _Thank you for your attention!_ 




# Task 2: Selectors. #
### Subtask 1: Searching for selectors on the login page. ### 
1. login_field_xpath:
> //*[@id="__next"]/form/div/div/div/label[@for = "password"]
> 
>/*[@for = "login" and @id = "login-label"]
 

2. password_field_xpath:
>/label[@class='MuiFormLabel-root MuiInputLabel-root MuiInputLabel-formControl MuiInputLabel-animated' and @id='password-label']
> 
>//*[@id="__next"]/form/div/div/div/label[@for = "password"]
> 
>//label[text() = "Password"]

3. remind_password_hyperlink_xpath:
>//a[text()="Remind password"]
> 
>//*[@id="__next"]/form/div/div[1]/a
> 
>/child::div/a

4. button_xpath:
>//button
> 
>//child::button
> 
>//*[@type = 'submit']

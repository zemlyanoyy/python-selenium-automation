# Amazon Logo
driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')


# Create account
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')


# Your name
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')


# Email
driver.find_element(By.CSS_SELECTOR, '#ap_email')


# Password
driver.find_element(By.CSS_SELECTOR, '#ap_password')


# Password must be at least 6 characters
driver.find_element(By.XPATH, "//div[contains(text(),'at least 6 characters.')and@class='a-alert-content']")


# Re-enter password
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')


# Create your Amazon account
driver.find_element(By.CSS_SELECTOR, '#continue')


# Conditions of Use
driver.find_element(By.CSS_SELECTOR, "#legalTextRow [href*='condition']")


# Privacy Notice
driver.find_element(By.CSS_SELECTOR, "#legalTextRow [href*='privacy']")


# Sign in
driver.find_element(By.XPATH, "//a[contains(text(),'Sign in')and@class='a-link-emphasis']")


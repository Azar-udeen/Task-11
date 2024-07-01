from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def perform_drag_and_drop():
    # Initialize the WebDriver
    driver = webdriver.Chrome()  # Use the appropriate driver for your browser
    driver.get("https://jqueryui.com/droppable/")

    try:
        # Switch to the frame that contains the drag and drop elements
        driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))

        # Locate the elements
        draggable = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "draggable"))
        )
        droppable = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "droppable"))
        )

        # Perform the drag and drop action
        actions = ActionChains(driver)
        actions.drag_and_drop(draggable, droppable).perform()

        # Validate the success of the drag and drop action
        if "Dropped!" in droppable.text:
            print("Drag and Drop operation successful!")
        else:
            print("Drag and Drop operation failed!")

    finally:
        # Close the WebDriver
        driver.quit()

if _name_ == "_main_":
    perform_drag_and_drop()

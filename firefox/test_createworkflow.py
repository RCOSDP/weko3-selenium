# Generated by Selenium IDE
import pytest
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestCreateworkflow():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_createworkflow(self):
    # Test name: create workflow
    # Step # | name | target | value | comment
    # 1 | open | / |  | 
    self.driver.get(os.environ['WEKO3_HOST'])
    # 2 | setWindowSize | 1646x976 |  | 
    self.driver.set_window_size(1646, 976)
    # 3 | click | linkText=Log in |  | 
    self.driver.find_element(By.LINK_TEXT, "Log in").click()
    # 4 | type | id=email | info@inveniosoftware.org | 
    self.driver.find_element(By.ID, "email").send_keys("info@inveniosoftware.org")
    # 5 | type | id=password | uspass123 | 
    self.driver.find_element(By.ID, "password").send_keys("uspass123")
    # 6 | click | css=.btn-primary |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    # 7 | click | linkText=info@inveniosoftware.org |  | 
    self.driver.find_element(By.LINK_TEXT, "info@inveniosoftware.org").click()
    # 8 | click | linkText=Administration |  | 
    self.driver.find_element(By.LINK_TEXT, "Administration").click()
    # 9 | click | linkText=WorkFlow |  | 
    self.driver.find_element(By.LINK_TEXT, "WorkFlow").click()
    # 10 | click | linkText=Flow List |  | 
    self.driver.find_element(By.LINK_TEXT, "Flow List").click()
    # 11 | click | id=btn_submit |  | 
    self.driver.find_element(By.ID, "btn_submit").click()
    # 12 | click | id=txt_flow_name |  | 
    self.driver.find_element(By.ID, "txt_flow_name").click()
    # 13 | type | id=txt_flow_name | flow00 | 
    self.driver.find_element(By.ID, "txt_flow_name").send_keys("flow00")
    # 14 | click | id=btn-new-flow |  | 
    self.driver.find_element(By.ID, "btn-new-flow").click()
    # 15 | click | id=btn_pop_action |  | 
    self.driver.find_element(By.ID, "btn_pop_action").click()
    # 16 | click | id=btn_apply_3 |  | 
    self.driver.find_element(By.ID, "btn_apply_3").click()
    # 17 | click | id=btn_pop_action |  | 
    self.driver.find_element(By.ID, "btn_pop_action").click()
    # 18 | mouseOver | id=btn_pop_action |  | 
    element = self.driver.find_element(By.ID, "btn_pop_action")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 19 | mouseOut | id=btn_pop_action |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element, 0, 0).perform()
    # 20 | click | id=btn_apply_4 |  | 
    self.driver.find_element(By.ID, "btn_apply_4").click()
    # 21 | click | css=#row_3 .sortable_up |  | 
    self.driver.find_element(By.CSS_SELECTOR, "#row_3 .sortable_up").click()
    # 22 | click | css=#row_4 .sortable_up > .fa |  | 
    self.driver.find_element(By.CSS_SELECTOR, "#row_4 .sortable_up > .fa").click()
    # 23 | click | id=btn_submit |  | 
    self.driver.find_element(By.ID, "btn_submit").click()
    # 24 | click | linkText=WorkFlow List |  | 
    self.driver.find_element(By.LINK_TEXT, "WorkFlow List").click()
    # 25 | click | id=btn_submit |  | 
    self.driver.find_element(By.ID, "btn_submit").click()
    # 26 | click | id=txt_workflow_name |  | 
    self.driver.find_element(By.ID, "txt_workflow_name").click()
    # 27 | type | id=txt_workflow_name | wf00 | 
    self.driver.find_element(By.ID, "txt_workflow_name").send_keys("wf00")
    # 28 | click | id=txt_itemtype |  | 
    self.driver.find_element(By.ID, "txt_itemtype").click()
    # 29 | select | id=txt_itemtype | label=data2 | 
    dropdown = self.driver.find_element(By.ID, "txt_itemtype")
    dropdown.find_element(By.XPATH, "//option[. = 'data2']").click()
    # 30 | click | id=btn_create |  | 
    self.driver.find_element(By.ID, "btn_create").click()
    # 31 | click | linkText=info@inveniosoftware.org |  | 
    self.driver.find_element(By.LINK_TEXT, "info@inveniosoftware.org").click()
    # 32 | click | linkText=Logout |  | 
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
  

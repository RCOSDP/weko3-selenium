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

class TestCreateindextree():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_createindextree(self):
    # Test name: create indextree
    # Step # | name | target | value | comment
    # 1 | open | / |  | 
    self.driver.get(os.environ['WEKO3_HOST'])
    # 2 | setWindowSize | 1646x976 |  | 
    self.driver.set_window_size(1646, 976)
    # 3 | click | css=.fa-sign-in |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".fa-sign-in").click()
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
    # 9 | click | linkText=Setting |  | 
    self.driver.find_element(By.LINK_TEXT, "Setting").click()
    # 10 | click | linkText=Edit Tree |  | 
    self.driver.find_element(By.LINK_TEXT, "Edit Tree").click()
    # 11 | click | css=tree-internal:nth-child(1) > .tree > li > .value-container .node-name |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tree-internal:nth-child(1) > .tree > li > .value-container .node-name").click()
    # 12 | click | id=add |  | 
    self.driver.find_element(By.ID, "add").click()
    # 13 | click | css=tree-internal:nth-child(2) .node-name |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tree-internal:nth-child(2) .node-name").click()
    # 14 | click | css=.input-group:nth-child(1) |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".input-group:nth-child(1)").click()
    # 15 | type | id=inputTitle_ja | IndexA | 
    self.driver.find_element(By.ID, "inputTitle_ja").send_keys("IndexA")
    # 16 | click | id=inputTitle_en |  | 
    self.driver.find_element(By.ID, "inputTitle_en").click()
    # 17 | click | css=.panel:nth-child(1) > .panel-body > .row .input-group:nth-child(3) |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".panel:nth-child(1) > .panel-body > .row .input-group:nth-child(3)").click()
    # 18 | type | id=inputTitle_en | IndexA | 
    self.driver.find_element(By.ID, "inputTitle_en").send_keys("IndexA")
    # 19 | click | id=rss_display |  | 
    self.driver.find_element(By.ID, "rss_display").click()
    # 20 | click | id=index-detail-submit |  | 
    self.driver.find_element(By.ID, "index-detail-submit").click()
    # 21 | assertAlert | Index updated successfully. |  | 
    assert self.driver.switch_to.alert.text == "Index updated successfully."
    # 22 | click | css=tree-internal:nth-child(1) > .tree > li |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tree-internal:nth-child(1) > .tree > li").click()
    # 23 | click | css=tree-internal:nth-child(1) > .tree > li > .value-container .node-name |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tree-internal:nth-child(1) > .tree > li > .value-container .node-name").click()
    # 24 | click | id=add |  | 
    self.driver.find_element(By.ID, "add").click()
    # 25 | mouseOver | id=add |  | 
    element = self.driver.find_element(By.ID, "add")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 26 | mouseOut | id=add |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element, 0, 0).perform()
    # 27 | click | css=tree-internal:nth-child(3) .node-name |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tree-internal:nth-child(3) .node-name").click()
    # 28 | click | css=.input-group:nth-child(1) |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".input-group:nth-child(1)").click()
    # 29 | type | id=inputTitle_ja | IndexB | 
    self.driver.find_element(By.ID, "inputTitle_ja").send_keys("IndexB")
    # 30 | type | id=inputTitle_en | IndexB | 
    self.driver.find_element(By.ID, "inputTitle_en").send_keys("IndexB")
    # 31 | click | id=rss_display |  | 
    self.driver.find_element(By.ID, "rss_display").click()
    # 32 | mouseOver | id=rss_display |  | 
    element = self.driver.find_element(By.ID, "rss_display")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 33 | mouseOut | id=rss_display |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element, 0, 0).perform()
    # 34 | click | id=index-detail-submit |  | 
    self.driver.find_element(By.ID, "index-detail-submit").click()
    # 35 | assertAlert | Index updated successfully. |  | 
    assert self.driver.switch_to.alert.text == "Index updated successfully."
    # 36 | click | css=tree-internal:nth-child(1) > .tree > li > .value-container .node-name |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tree-internal:nth-child(1) > .tree > li > .value-container .node-name").click()
    # 37 | click | id=add |  | 
    self.driver.find_element(By.ID, "add").click()
    # 38 | mouseOver | id=add |  | 
    element = self.driver.find_element(By.ID, "add")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 39 | mouseOut | id=add |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element, 0, 0).perform()
    # 40 | click | css=tree-internal:nth-child(4) .node-name |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tree-internal:nth-child(4) .node-name").click()
    # 41 | click | css=.input-group:nth-child(1) |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".input-group:nth-child(1)").click()
    # 42 | type | id=inputTitle_ja | IndexC | 
    self.driver.find_element(By.ID, "inputTitle_ja").send_keys("IndexC")
    # 43 | type | id=inputTitle_en | IndexC | 
    self.driver.find_element(By.ID, "inputTitle_en").send_keys("IndexC")
    # 44 | click | id=rss_display |  | 
    self.driver.find_element(By.ID, "rss_display").click()
    # 45 | mouseOver | id=rss_display |  | 
    element = self.driver.find_element(By.ID, "rss_display")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 46 | mouseOut | id=rss_display |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element, 0, 0).perform()
    # 47 | click | id=index-detail-submit |  | 
    self.driver.find_element(By.ID, "index-detail-submit").click()
    # 48 | assertAlert | Index updated successfully. |  | 
    assert self.driver.switch_to.alert.text == "Index updated successfully."
    # 49 | click | css=tree-internal:nth-child(2) .node-name |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tree-internal:nth-child(2) .node-name").click()
    # 50 | click | id=add |  | 
    self.driver.find_element(By.ID, "add").click()
    # 51 | click | css=.node-collapsed |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".node-collapsed").click()
    # 52 | click | css=tree-internal:nth-child(2) tree-internal .node-name |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tree-internal:nth-child(2) tree-internal .node-name").click()
    # 53 | click | css=.input-group:nth-child(1) |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".input-group:nth-child(1)").click()
    # 54 | type | id=inputTitle_ja | IndexA2 | 
    self.driver.find_element(By.ID, "inputTitle_ja").send_keys("IndexA2")
    # 55 | type | id=inputTitle_en | IndexA1 | 
    self.driver.find_element(By.ID, "inputTitle_en").send_keys("IndexA1")
    # 56 | click | id=inputTitle_ja |  | 
    self.driver.find_element(By.ID, "inputTitle_ja").click()
    # 57 | type | id=inputTitle_ja | IndexA1 | 
    self.driver.find_element(By.ID, "inputTitle_ja").send_keys("IndexA1")
    # 58 | click | id=rss_display |  | 
    self.driver.find_element(By.ID, "rss_display").click()
    # 59 | mouseOver | id=rss_display |  | 
    element = self.driver.find_element(By.ID, "rss_display")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 60 | mouseOut | id=rss_display |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element, 0, 0).perform()
    # 61 | click | id=index-detail-submit |  | 
    self.driver.find_element(By.ID, "index-detail-submit").click()
    # 62 | assertAlert | Index updated successfully. |  | 
    assert self.driver.switch_to.alert.text == "Index updated successfully."
    # 63 | click | css=.node-collapsed |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".node-collapsed").click()
    # 64 | click | css=tree-internal:nth-child(1) > .tree > li > tree-internal:nth-child(2) > .tree > li > .value-container .node-name |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tree-internal:nth-child(1) > .tree > li > tree-internal:nth-child(2) > .tree > li > .value-container .node-name").click()
    # 65 | click | id=add |  | 
    self.driver.find_element(By.ID, "add").click()
    # 66 | mouseOver | id=add |  | 
    element = self.driver.find_element(By.ID, "add")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 67 | mouseOut | id=add |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element, 0, 0).perform()
    # 68 | click | css=.node-collapsed |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".node-collapsed").click()
    # 69 | click | css=tree-internal:nth-child(2) tree-internal:nth-child(3) .node-name |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tree-internal:nth-child(2) tree-internal:nth-child(3) .node-name").click()
    # 70 | click | css=.input-group:nth-child(1) |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".input-group:nth-child(1)").click()
    # 71 | type | id=inputTitle_ja | IndexA2 | 
    self.driver.find_element(By.ID, "inputTitle_ja").send_keys("IndexA2")
    # 72 | click | css=.panel:nth-child(1) > .panel-body > .row .input-group:nth-child(3) |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".panel:nth-child(1) > .panel-body > .row .input-group:nth-child(3)").click()
    # 73 | type | id=inputTitle_en | IndexA2 | 
    self.driver.find_element(By.ID, "inputTitle_en").send_keys("IndexA2")
    # 74 | click | id=rss_display |  | 
    self.driver.find_element(By.ID, "rss_display").click()
    # 75 | mouseOver | id=rss_display |  | 
    element = self.driver.find_element(By.ID, "rss_display")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 76 | mouseOut | id=rss_display |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element, 0, 0).perform()
    # 77 | click | id=index-detail-submit |  | 
    self.driver.find_element(By.ID, "index-detail-submit").click()
    # 78 | assertAlert | Index updated successfully. |  | 
    assert self.driver.switch_to.alert.text == "Index updated successfully."
    # 79 | click | css=tree-internal:nth-child(3) .node-name |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tree-internal:nth-child(3) .node-name").click()
    # 80 | click | id=add |  | 
    self.driver.find_element(By.ID, "add").click()
    # 81 | mouseOver | id=add |  | 
    element = self.driver.find_element(By.ID, "add")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 82 | mouseOut | id=add |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element, 0, 0).perform()
    # 83 | click | css=tree-internal:nth-child(3) .folding |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tree-internal:nth-child(3) .folding").click()
    # 84 | click | css=tree-internal:nth-child(3) tree-internal .node-name |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tree-internal:nth-child(3) tree-internal .node-name").click()
    # 85 | click | css=.input-group:nth-child(1) |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".input-group:nth-child(1)").click()
    # 86 | click | css=.input-group:nth-child(1) |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".input-group:nth-child(1)").click()
    # 87 | type | id=inputTitle_ja | IndexB1 | 
    self.driver.find_element(By.ID, "inputTitle_ja").send_keys("IndexB1")
    # 88 | click | css=.panel:nth-child(1) > .panel-body > .row .input-group:nth-child(3) |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".panel:nth-child(1) > .panel-body > .row .input-group:nth-child(3)").click()
    # 89 | type | id=inputTitle_en | IndexB1 | 
    self.driver.find_element(By.ID, "inputTitle_en").send_keys("IndexB1")
    # 90 | click | css=.panel:nth-child(3) .col-sm-10 |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".panel:nth-child(3) .col-sm-10").click()
    # 91 | click | id=rss_display |  | 
    self.driver.find_element(By.ID, "rss_display").click()
    # 92 | mouseOver | id=rss_display |  | 
    element = self.driver.find_element(By.ID, "rss_display")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 93 | mouseOut | id=rss_display |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element, 0, 0).perform()
    # 94 | click | css=.panel-footer |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".panel-footer").click()
    # 95 | click | id=index-detail-submit |  | 
    self.driver.find_element(By.ID, "index-detail-submit").click()
    # 96 | assertAlert | Index updated successfully. |  | 
    assert self.driver.switch_to.alert.text == "Index updated successfully."
    # 97 | click | css=tree-internal:nth-child(3) .value-container |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tree-internal:nth-child(3) .value-container").click()
    # 98 | click | css=tree-internal:nth-child(3) .node-name |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tree-internal:nth-child(3) .node-name").click()
    # 99 | click | id=add |  | 
    self.driver.find_element(By.ID, "add").click()
    # 100 | mouseOver | id=add |  | 
    element = self.driver.find_element(By.ID, "add")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 101 | mouseOut | id=add |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element, 0, 0).perform()
    # 102 | click | css=tree-internal:nth-child(3) .folding |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tree-internal:nth-child(3) .folding").click()
    # 103 | click | css=tree-internal:nth-child(3) tree-internal:nth-child(2) > .tree |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tree-internal:nth-child(3) tree-internal:nth-child(2) > .tree").click()
    # 104 | click | css=tree-internal:nth-child(3) tree-internal:nth-child(3) .node-name |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tree-internal:nth-child(3) tree-internal:nth-child(3) .node-name").click()
    # 105 | click | css=.panel:nth-child(1) > .panel-body:nth-child(1) |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".panel:nth-child(1) > .panel-body:nth-child(1)").click()
    # 106 | type | id=inputTitle_ja | IndexB2 | 
    self.driver.find_element(By.ID, "inputTitle_ja").send_keys("IndexB2")
    # 107 | type | id=inputTitle_en | IndexB2 | 
    self.driver.find_element(By.ID, "inputTitle_en").send_keys("IndexB2")
    # 108 | click | css=.panel:nth-child(3) .col-sm-10 |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".panel:nth-child(3) .col-sm-10").click()
    # 109 | click | id=rss_display |  | 
    self.driver.find_element(By.ID, "rss_display").click()
    # 110 | mouseOver | id=rss_display |  | 
    element = self.driver.find_element(By.ID, "rss_display")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 111 | mouseOut | id=rss_display |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element, 0, 0).perform()
    # 112 | click | css=.glyphicon-send |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".glyphicon-send").click()
    # 113 | assertAlert | Index updated successfully. |  | 
    assert self.driver.switch_to.alert.text == "Index updated successfully."
    # 114 | click | css=tree-internal:nth-child(4) .node-value |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tree-internal:nth-child(4) .node-value").click()
    # 115 | click | css=.node-selected > .node-name |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".node-selected > .node-name").click()
    # 116 | click | css=.glyphicon-plus |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".glyphicon-plus").click()
    # 117 | mouseOver | css=.glyphicon-plus |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".glyphicon-plus")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 118 | mouseOut | css=.glyphicon-plus |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element, 0, 0).perform()
    # 119 | click | css=tree-internal:nth-child(4) .folding |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tree-internal:nth-child(4) .folding").click()
    # 120 | click | css=tree-internal:nth-child(4) tree-internal .node-name |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tree-internal:nth-child(4) tree-internal .node-name").click()
    # 121 | click | id=inputTitle_ja |  | 
    self.driver.find_element(By.ID, "inputTitle_ja").click()
    # 122 | click | css=.input-group:nth-child(1) |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".input-group:nth-child(1)").click()
    # 123 | doubleClick | css=.input-group:nth-child(1) |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".input-group:nth-child(1)")
    actions = ActionChains(driver)
    actions.double_click(element).perform()
    # 124 | type | id=inputTitle_ja | IndexC1 | 
    self.driver.find_element(By.ID, "inputTitle_ja").send_keys("IndexC1")
    # 125 | click | css=.panel:nth-child(1) > .panel-body > .row .input-group:nth-child(3) |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".panel:nth-child(1) > .panel-body > .row .input-group:nth-child(3)").click()
    # 126 | type | id=inputTitle_en | IndexC1 | 
    self.driver.find_element(By.ID, "inputTitle_en").send_keys("IndexC1")
    # 127 | click | id=rss_display |  | 
    self.driver.find_element(By.ID, "rss_display").click()
    # 128 | mouseOver | id=rss_display |  | 
    element = self.driver.find_element(By.ID, "rss_display")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 129 | mouseOut | id=rss_display |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element, 0, 0).perform()
    # 130 | click | id=index-detail-submit |  | 
    self.driver.find_element(By.ID, "index-detail-submit").click()
    # 131 | assertAlert | Index updated successfully. |  | 
    assert self.driver.switch_to.alert.text == "Index updated successfully."
    # 132 | click | css=tree-internal:nth-child(4) .node-name |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tree-internal:nth-child(4) .node-name").click()
    # 133 | click | id=add |  | 
    self.driver.find_element(By.ID, "add").click()
    # 134 | mouseOver | id=add |  | 
    element = self.driver.find_element(By.ID, "add")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 135 | mouseOut | id=add |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element, 0, 0).perform()
    # 136 | click | css=tree-internal:nth-child(4) .folding |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tree-internal:nth-child(4) .folding").click()
    # 137 | click | css=tree-internal:nth-child(4) tree-internal:nth-child(3) .node-name |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tree-internal:nth-child(4) tree-internal:nth-child(3) .node-name").click()
    # 138 | click | css=.input-group:nth-child(1) |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".input-group:nth-child(1)").click()
    # 139 | type | id=inputTitle_ja | IndexC2 | 
    self.driver.find_element(By.ID, "inputTitle_ja").send_keys("IndexC2")
    # 140 | type | id=inputTitle_en | IndexC2 | 
    self.driver.find_element(By.ID, "inputTitle_en").send_keys("IndexC2")
    # 141 | click | id=rss_display |  | 
    self.driver.find_element(By.ID, "rss_display").click()
    # 142 | mouseOver | id=rss_display |  | 
    element = self.driver.find_element(By.ID, "rss_display")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 143 | mouseOut | id=rss_display |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element, 0, 0).perform()
    # 144 | click | id=index-detail-submit |  | 
    self.driver.find_element(By.ID, "index-detail-submit").click()
    # 145 | assertAlert | Index updated successfully. |  | 
    assert self.driver.switch_to.alert.text == "Index updated successfully."
    # 146 | click | linkText=info@inveniosoftware.org |  | 
    self.driver.find_element(By.LINK_TEXT, "info@inveniosoftware.org").click()
    # 147 | click | linkText=Logout |  | 
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
    # 148 | click | css=tree-internal:nth-child(2) .folding |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tree-internal:nth-child(2) .folding").click()
    # 149 | click | css=tree-internal:nth-child(3) .node-collapsed |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tree-internal:nth-child(3) .node-collapsed").click()
    # 150 | click | css=.node-collapsed |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".node-collapsed").click()
  

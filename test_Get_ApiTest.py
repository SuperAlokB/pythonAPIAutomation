import requests
import json
import jsonpath

from assertpy.assertpy import assert_that


def test_get_employee_details_withstatus_200():
    #response = requests.get("https://petstore.swagger.io/#/pet/findPetsByStatus");
    
    response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=available")
    assert response.status_code == 200
    #The data is returned as a Python dictionary 
    json_response = response.json()    
        
    firstAnimalName = [category['id'] for category in json_response]
    print(type(firstAnimalName))
    print(firstAnimalName[0])
    
    assert_that(firstAnimalName[0]).is_equal_to(23444)
  
   
    
       #Response json contents
    
   # nameList =  jsonpath.jsonpath(json_response,"nameList[0].name")
   # print("*********** :" + nameList[0].name)
    #validate response json content - type header
    
    #assert response.headers["Content-Type"] == "application/json"
    
    #resp_body = response.json()
    #validate json with expected value 
    
    
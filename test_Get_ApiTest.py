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
       
    #print(json_response[0]) 
    #print(len(json_response))
    
    #Getting all objects from pet store - 
    for objects in json_response:
        print(objects)
        #can write verification login for each objects
        
    firstAnimalName = [category['id'] for category in json_response]
    print(firstAnimalName[0])
   
   # print all json data in response 
      
    """
    for key in json_response[0]:{
        print(key, ":" , json_response[key])
       
    }"""

 # print(type(json_response))
    assert_that(firstAnimalName[0]).is_equal_to(23444)
    
       #Response json contents
    
   # nameList =  jsonpath.jsonpath(json_response,"nameList[0].name")
   # print("*********** :" + nameList[0].name)
    #validate response json content - type header
    
    #assert response.headers["Content-Type"] == "application/json"
    
    #resp_body = response.json()
    #validate json with expected value 
    
    
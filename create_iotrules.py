#This python script runs AWS CLI commands and relies on the permissions on your AWS CLoud9 instance
#Create IoT rules from Iot Core to Sitewise. json object reference for rules have been pre defined in /iot_rules

import time
import json
from collections import namedtuple
import os
import subprocess as sp
import argparse

#Define path 
path = os.path.abspath( os.path.dirname( __file__ ) )
print(path)

#Gets arguments 
parser = argparse.ArgumentParser()
parser.add_argument("-r", "--roleArn", action="store", required=True, dest="roleArn")

args = parser.parse_args()
roleArn = f"{args.roleArn}"



#Function for iot_core rule creation
def CreateIoTRuleJSON(path, station_number, role_arn): #Inputs path and how many rules you like to create 
    # #load role_arn
    # with open(f"{path}/iot_rules/role_arn.json",) as file:
    #     print(f"working from {path}")
    #     role_arn = json.load(file)
     
    n = station_number
    rule_out = {
          "sql": f"SELECT * FROM '/pumpingstation/{n}'",
          "description": f"Sends data to sitewise pumpingstation{n}",
          "ruleDisabled": False,
          "awsIotSqlVersion": "2016-03-23",
          "actions": [
            {
              "iotSiteWise": {
                "putAssetPropertyValueEntries":[
                                {
                                    "propertyValues": [
                                        {
                                            "timestamp": {
                                                "timeInSeconds": "${floor(timestamp() / 1E3)}", 
                                                "offsetInNanos": "0"
                                            }, 
                                            "value": {
                                                "integerValue": "${get(*, \"Pressure\")}"
                                            }
                                        }
                                    ], 
                                    "propertyAlias": f"/pumpingstation/{n}/Pressure"
                                }, 
                                {
                                    "propertyValues": [
                                        {
                                            "timestamp": {
                                                "timeInSeconds": "${floor(timestamp() / 1E3)}", 
                                                "offsetInNanos": "0"
                                            }, 
                                            "value": {
                                                "integerValue": "${get(*, \"Vibration\")}"
                                            }
                                        }
                                    ], 
                                    "propertyAlias": f"/pumpingstation/{n}/Vibration"
                                }, 
                                {
                                    "propertyValues": [
                                        {
                                            "timestamp": {
                                                "timeInSeconds": "${floor(timestamp() / 1E3)}", 
                                                "offsetInNanos": "0"
                                            }, 
                                            "value": {
                                                "integerValue": "${get(*, \"Flow\")}"
                                            }
                                        }
                                    ], 
                                    "propertyAlias": f"/pumpingstation/{n}/Flow"
                                }, 
                                {
                                    "propertyValues": [
                                        {
                                            "timestamp": {
                                                "timeInSeconds": "${floor(timestamp() / 1E3)}", 
                                                "offsetInNanos": "0"
                                            }, 
                                            "value": {
                                                "integerValue": "${get(*, \"Amperage\")}"
                                            }
                                        }
                                    ], 
                                    "propertyAlias": f"/pumpingstation/{n}/Amperage"
                                }, 
                                {
                                    "propertyValues": [
                                        {
                                            "timestamp": {
                                                "timeInSeconds": "${floor(timestamp() / 1E3)}", 
                                                "offsetInNanos": "0"
                                            }, 
                                            "value": {
                                                "integerValue": "${get(*, \"Voltage\")}"
                                            }
                                        }
                                    ], 
                                    "propertyAlias": f"/pumpingstation/{n}/Voltage"
                                }, 
                                {
                                    "propertyValues": [
                                        {
                                            "timestamp": {
                                                "timeInSeconds": "${floor(timestamp() / 1E3)}", 
                                                "offsetInNanos": "0"
                                            }, 
                                            "value": {
                                                "integerValue": "${get(*, \"Temperature\")}"
                                            }
                                        }
                                    ], 
                                    "propertyAlias": f"/pumpingstation/{n}/Temperature"
                                }, 
                                {
                                    "propertyValues": [
                                        {
                                            "timestamp": {
                                                "timeInSeconds": "${floor(timestamp() / 1E3)}", 
                                                "offsetInNanos": "0"
                                            }, 
                                            "value": {
                                                "booleanValue": "${get(*, \"Fan\")}"
                                            }
                                        }
                                    ], 
                                    "propertyAlias": f"/pumpingstation/{n}/Fan"
                                }, 
                                {
                                    "propertyValues": [
                                        {
                                            "timestamp": {
                                                "timeInSeconds": "${floor(timestamp() / 1E3)}", 
                                                "offsetInNanos": "0"
                                            }, 
                                            "value": {
                                                "integerValue": "${get(*, \"rpm\")}"
                                            }
                                        }
                                    ], 
                                    "propertyAlias": f"/pumpingstation/{n}/rpm"
                                }, 
                                {
                                    "propertyValues": [
                                        {
                                            "timestamp": {
                                                "timeInSeconds": "${floor(timestamp() / 1E3)}", 
                                                "offsetInNanos": "0"
                                            }, 
                                            "value": {
                                                "integerValue": "${get(*, \"Humidity\")}"
                                            }
                                        }
                                    ], 
                                    "propertyAlias": f"/pumpingstation/{n}/Humidity"
                                }, 
                                {
                                    "propertyValues": [
                                        {
                                            "timestamp": {
                                                "timeInSeconds": "${floor(timestamp() / 1E3)}", 
                                                "offsetInNanos": "0"
                                            }, 
                                            "value": {
                                                "stringValue": "${get(*, \"Location\")}"
                                            }
                                        }
                                    ], 
                                    "propertyAlias": f"/pumpingstation/{n}/Location"
                                }
                            ],
                "roleArn": f"{role_arn}" 
              }
            }
          ]
        }   
            
        
      
    #Checks if a JSON rule profile already exists
    profile_exists = os.path.exists(f"{path}/iot_rules/iotcore_to_sitewise_rule_pumpingstation{n}.json")
    
    if profile_exists:
        sp.getoutput(f"aws iot create-topic-rule --rule-name pumpingstation{n} --topic-rule-payload file://{path}/iot_rules/iotcore_to_sitewise_rule_pumpingstation{n}.json")
        print(f"aws iot creat-topic-rule for pumpingstation{n}")
        
        #If the profile is not present start configuration and file creation
    else:
        #Write to a file 
        with open(f"{path}/iot_rules/iotcore_to_sitewise_rule_pumpingstation{n}.json", 'a') as outfile:
              json.dump(rule_out, outfile)
              print(f"IoT rule JSON profile created for pumping station {n}")
        sp.getoutput(f"aws iot create-topic-rule --rule-name pumpingstation{n} --topic-rule-payload file://{path}/iot_rules/iotcore_to_sitewise_rule_pumpingstation{n}.json")
        print(f"aws iot creat-topic-rule for pumpingstation{n}")
        

        
     
for n in range(1, 11):
    CreateIoTRuleJSON(path, n, roleArn)
    
print ("Script finished gracefully !!!")
      

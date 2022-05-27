
#This scrip runs AWS CLI commands and relies on the permissions on your AWS CLoud9 instance
import time
import json
from collections import namedtuple
import os
import subprocess as sp

#DELETE THIS LATER 

def DeleteAsset(asset_id): 
    delete_asset = sp.getoutput(f"aws iotsitewise delete-asset \
    --asset-id {asset_id}")
    print (f"Asset {asset_id} has been scheduled for deletion")
    
    
    
    #DeleteAsset(asset_id)

    
#print (get_asset_model_id_json["assetModelSummaries"][0]["id"], get_asset_model_id_json["assetModelSummaries"][0]["name"])

# output = sp.getoutput("aws iotsitewise create-asset \
#   --asset-name pumpingstation003 \
#   --asset-model-id 6c785413-553d-4911-901d-695de7459a47")

  
# print ("asset created")  
  
# print (output)

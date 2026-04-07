import os
import httpx
from dotenv import load_dotenv
from ms_graph import get_access_token, MS_GRAPH_BASE_URL

base = f"{MS_GRAPH_BASE_URL}"

def get_folder_id(headers, folder_name, parent_folder_id=None):
    if parent_folder_id is None:
        url = f"{base}/me/mailFolders"
    else:
        url = f"{base}/{parent_folder_id}/childFolders"
        
    response = httpx.get(url, headers=headers)
    response.raise_for_status()
    
    data = response.json()
    folders = data.get("value", [])
    
    for folder in folders:
        print(folder.get("displayName"), folder.get("id")) # * temp for debugging
        if folder.get("displayName") == folder_name:
            return folder.get("id")
        
        child_id = get_folder_id(
            headers,
            folder_name,
            parent_folder_id=folder.get("id")
        )
        
        if child_id:
            return child_id
        
def fetch_mails(headers, folder_id):
    url = f"{base}/me/mailFolders/{folder_id}/messages"
    response = httpx.get(url, headers=headers)
    response.raise_for_status()
    
    data = response.json()
    messages = data.get("value", [])

    for message in messages:
        print(message.get("subject"), message.get("bodyPreview"))
        print("____________________________")
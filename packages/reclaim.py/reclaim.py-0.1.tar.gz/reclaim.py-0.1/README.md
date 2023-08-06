# reclaim.py


**Unofficial [https://reclaim.ai](reclaim.ai) Python Client for creating tasks**

- Works via Google Tasks (for now)
- Only Task Creation supported (for now)


## Setup Guide

1. Install via pip:
    ```
    pip3 install reclaim.py
    ```

2. Setup Google Tasks API

    *If you use this for yourself, you are likely going to stay in Google API's free quota, so no worries there!*

    1) Visit the [Google Cloud Console](https://console.cloud.google.com/) and accept the terms
    2) Search for "Google Tasks API" or go [here](https://console.cloud.google.com/marketplace/product/google/tasks.googleapis.com?q=search&referrer=search) and click the blue "Activate" button
    3) Once activated, click "Manage" (also blue button)
    4) Naviagte to "OAuth consent screen"
    5) Create an "external" Consent Screen and fill out the <u>required</u> fields (Email fields: Put your Gmail there, Name fields: put in anything)
    6) "Save and Continue", then click "Add or Remove **Scopes**
    7) Seach for "Tasks" and coninue like this:<br>
   <img src="https://user-images.githubusercontent.com/45080708/161107506-e759d721-b160-4e36-9111-a0aae4ecef2b.png" width="500">
<br>
    8) Click "Save and Continue" and add your email to "Test users". There will be no need to ever leave the "Testing" phase.
    9) Once you added your email as Test User, it should look like this:<br>
    <img src="https://user-images.githubusercontent.com/45080708/161108575-c146a62b-ecc8-47b0-a6e9-368c0a55c790.png" width="600"><br>
    10) Naviage to "Credentials" and click "Create Credentials", "OAuth Client ID". Then select "Desktop app" as type.
    11) Once created, click "Download Json" on the popup shown. Save this file as `credentials.json` in your project folder.
   <br><br>
1. With the `credentials.json` in the same folder as your application, you can start creating some tasks:

```py
import reclaim
from datetime import datetime, timedelta

client = reclaim.Client(credentials = "credentails.json", token_store = "token.json")
                        # you can optionally set reclaim_task_list_id if you don't want it to be detected automatically


if not client.authorized: # authorize your google account once
    client.do_authorization() # You will be asked to Login with Google. Just follow the instructions printed.

assert client.authorized # ensure you are authorized with Google

succeeded:bool = client.create_task(is_work = True,
                    title = "My fancy Reclaim task",
                    duration = timedelta(hours = 2, minutes = 30), # 2 hours, 30 minutes
                    due_at = datetime.now() + timedelta(weeks = 3),
                    not_before = datetime.now() + timedelta(days = 4), # only start in 4 days            
                )
print(succeeded) # should output True
```


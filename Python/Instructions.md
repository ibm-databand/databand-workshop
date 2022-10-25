Section 1: Local environment
a. Get pyCharm
Goto https://www.jetbrains.com/pycharm/ and download PyCharm (if you do not have it yet). This workshop is based upon PyCharm but you can use any editor of your liking. Be aware of setting up a Python environment with version 3.8. That is the version we are using now.

b. Define a new project
Create a new project in PyCharm, any name will do.

c. Add Databand packages to project env
So to make your Pytyhon code work with Databand, you need to add some Databand libraries. Please review https://docs.databand.ai/docs/python for extra information. Please do (or add the packages otherwise) this:
pip install databand dbnd

Might your environment complain about other libraries, please add those too!

d. Review Python scripts
This folder holds 3 python scripts and a set of data files. Basically the order of flow is:
1. Prepare_GreatOutdoors_Demo.py
2. Pipeline_GreatOutdoors_Demo.py
3. Lineage__GreatOutdoors_Demo.py

Download the content of this folder into your project. You can review the data files but the main theme is outdoors equipment sales. In step 1. the base file will be prepared, in step 2. abstracts will be created. In step 3. again abstracts will be created but mainly to get a form of lineage in Databand.

Section 2: databand.ai
a. Access databand.ai
First let's access the Databand environment. You will be provided with the required URL and account credentials. Browse through the different parts of the Databand environment. Do not break the environment!

b. Create token
When you want your Python pipelines to be monitored by Databand, they need to be adjusted to push their logging metadata to the relevant Databand environment related to your account. For that you need a Databand access token. You will be shown where this done. 

Adjust all (3) Python scripts:
"databand_url": "<databand_url>" -> replace <databand_url> with the provided URL 
"databand_access_token": "<databand_access_token>" -> replace <databand_access_token> with your created or privided token

Be aware: Depending on the workshop group size you will not get equal amount account credentials. In that case you will share account credentials and access tokens.

Section 3: Happy flow
a. Adjust Python script (make it work with databand.ai)
You already did some changes but you are not done yet. In the Databand environment your pipelines need some identification. You will provide these in your code via:
job_name="Prepare_GreatOutdoors_demo_<tbd>"
run_name="GreatOutdoors_Weekly_<tbd>"
project_name="GreatOutdoors Retail Analytics_<tbd>"

These are the three attributes to identify your pipeline. Please change <tbd> to anything that makes your pipelines findable to you in the Databand environment: You are sharing that with your workshop colleagues (who are using the same workshop assets) and others (that might have used the same assets or just others). 

Please read more at https://docs.databand.ai/docs/python

b. Run Python scripts (a few times)
Databand is trying to interpret the provided logging metadata and correlate the data to existing data. This is how lineage is being composed. For that it needs a few pipeline runs to be executed. Run the scripts locally. Solve anny issues and make sure you at least have 5 run results per script in Databand.

c. Review databand.ai
Goto the Databand environment and review your pipelines.

Section 4: Broken flow
a. Break Python script
Here your Python experience is helpfull! You are going to break the scripts in a way so you know what is broken in the scripts and how this will be represented in Databand. Do not break all three of them, this is a Databand learning exercise. 

Hint: Take a peak at Databand alerts and try to create a "breaking point" that would match a alerting type.

b. Run Python scripts (a few times)
Databand is trying to interpret the provided logging metadata and correlate the data to existing data. This is how lineage is being composed. For that it needs a few pipeline runs to be executed. Run the scripts locally. Solve anny issues and make sure you at least have 5 run results per script in Databand.

c. Review databand.ai
Goto the Databand environment and review your pipelines.

Section 5: Alerting
a. Define alert
Goto the Databand environment and define an alert. YOu might even define a few alerts. You might be wondering why you, up to now, did not see any lineage yet? Lineage is related to alerts. If you did not define an alert, you get no lineage. For more on alerting, goto: https://docs.databand.ai/docs/alerting 

b. Run Python scripts (a few times)
Databand is trying to interpret the provided logging metadata and correlate the data to existing data. This is how lineage is being composed. For that it needs a few pipeline runs to be executed. Run the scripts locally. Solve anny issues and make sure you at least have 5 run results per script in Databand.

c. Review databand.ai (including lineage)
Goto the Databand environment and review your pipelines.
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
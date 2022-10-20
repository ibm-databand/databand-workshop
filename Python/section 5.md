Section 5: Alerting
a. Define alert
Goto the Databand environment and define an alert. YOu might even define a few alerts. You might be wondering why you, up to now, did not see any lineage yet? Lineage is related to alerts. If you did not define an alert, you get no lineage. 

b. Run Python scripts (a few times)
Databand is trying to interpret the provided logging metadata and correlate the data to existing data. This is how lineage is being composed. For that it needs a few pipeline runs to be executed. Run the scripts locally. Solve anny issues and make sure you at least have 5 run results per script in Databand.

c. Review databand.ai (including lineage)
Goto the Databand environment and review your pipelines.
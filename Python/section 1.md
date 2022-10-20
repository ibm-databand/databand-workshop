Section 1: Local environment
a. Get pyCharm

Goto https://www.jetbrains.com/pycharm/ and download PyCharm (if you do not have it yet). This workshop is based upon PyCharm but you can use any editor of your liking. Be aware of setting up a Python environment with version 3.8. That is the version we are using now.

b. Define a new project
Create a new project in PyCharm, any name will do.

c. Add Databand packages to project env
So to make your Pytyhon code work with Databand, you need to add some Databand libraries. Please review https://docs.databand.ai/docs/python for extra information. To be on the safeside (and also add Airflow support), please do (or add the packages otherwise) this:
pip install databand

For airflow:
pip install dbnd-spark dbnd-airflow
pip install dbnd-airflow-auto-tracking 
pip install dbnd-airflow-monitor

Might your environment complain about other libraries, please add those too!

d. Review Python scripts
This folder holds 3 python scripts and a set of data files. Basically the order of flow is:
1. Prepare_GreatOutdoors_Demo.py
2. Pipeline_GreatOutdoors_Demo.py
3. Lineage__GreatOutdoors_Demo.py

You can review the data files but the main theme is outdoors equipment sales. In step 1. the base file will be prepared, in step 2. abstracts will be created. In step 3. again abstracts will be created but mainly to get a form of lineage in Databand.
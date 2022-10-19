# Import pandas and databand libraries
import pandas as pd
from dbnd import dbnd_tracking, task, dataset_op_logger

@task
def read_raw_data():
    rawData = pd.read_csv('Retail_Products_and_Customers1.csv')

    with dataset_op_logger("local://Base/Retail_Products_and_Customers.csv", "read", with_schema=True,
                           with_preview=True) as logger:
        logger.set(data=rawData)

    return rawData

@task
def write_demo_data(rawData):

    demoData = rawData

    with dataset_op_logger("local://GreatOutdoors/GreatOutdoors_Retail_Products_and_Customers.csv", "write", with_schema=True,
                           with_preview=True) as logger:
        logger.set(data=demoData)

    demoData.to_csv("GreatOutdoors_Retail_Products_and_Customers.csv", index=False)

def prepare_demo_data():
    with dbnd_tracking(
            conf={
                "core": {
                    "databand_url": "<databand_url>",
                    "databand_access_token": "<databand_access_token>",

                }
            },
            job_name="Prepare_GreatOutdoors_demo_<tbd>",
            run_name="GreatOutdoors_Weekly_<tbd>",
            project_name="GreatOutdoors Retail Analytics_<tbd>",
    ):
    
        rawData = read_raw_data()

        write_demo_data(rawData)

        print("Finished running the Prepare_GreatOutdoors_demo pipeline")

prepare_demo_data()

# Import pandas and databand libraries
import pandas as pd
from dbnd import dbnd_tracking, task, dataset_op_logger


@task
def read_sales_data():
    retailData = pd.read_csv('GreatOutdoors_Camping_Equipment.csv')

    with dataset_op_logger("local://GreatOutdoors/GreatOutdoors_Camping_Equipment.csv", "read", with_schema=True,
                           with_preview=True) as logger:
        logger.set(data=retailData)

    return retailData


@task
def write_data_by_state(salesData):
    salesByState = salesData.loc[salesData['State'] == 'Arizona']

    with dataset_op_logger("local://GreatOutdoors/GreatOutdoors_Arizona_Camping_Equipment.csv", "write", with_schema=True,
                           with_preview=True) as logger:
        logger.set(data=salesByState)

    salesByState.to_csv("GreatOutdoors_Arizona_Camping_Equipment.csv", index=False)

def prepare_retail_data():
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
        salesData = read_sales_data()

        write_data_by_state(salesData)

        print("Finished running the Lineage_GreatOutdoors_demo pipeline")

prepare_retail_data()

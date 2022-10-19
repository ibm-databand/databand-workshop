# Import pandas and databand libraries
import pandas as pd
from dbnd import dbnd_tracking, task, dataset_op_logger
@task
def read_raw_data():
    retailData = pd.read_csv('GreatOutdoors_Retail_Products_and_Customers.csv')

    # Log the data read
    with dataset_op_logger("local://GreatOutdoors/GreatOutdoors_Retail_Products_and_Customers.csv", "read", with_schema=True,
                           with_preview=True) as logger:
        logger.set(data=retailData)

    return retailData


@task
def filter_data(rawData):
    filteredRetailData = rawData.drop(['Buy', 'PROFESSION', 'EDUCATION'], axis=1)

    with dataset_op_logger("script://GreatOutdoors/Filtered_df", "read", with_schema=True, with_preview=True) as logger:
        logger.set(data=filteredRetailData)

    return filteredRetailData


@task
def write_data_by_product_line(filteredData):
    campingEquipment = filteredData.loc[filteredData['Product line'] == 'Camping Equipment']

    with dataset_op_logger("local://GreatOutdoors/GreatOutdoors_Camping_Equipment.csv", "write", with_schema=True,
                           with_preview=True) as logger:
        logger.set(data=campingEquipment)

    campingEquipment.to_csv("GreatOutdoors_Camping_Equipment.csv", index=False)

    golfEquipment = filteredData.loc[filteredData['Product line'] == 'Golf Equipment']

    with dataset_op_logger("local://GreatOutdoors/GreatOutdoors_Golf_Equipment.csv", "write", with_schema=True,
                           with_preview=True) as logger:
        logger.set(data=golfEquipment)

    golfEquipment.to_csv("GreatOutdoors_Golf_Equipment.csv", index=False)

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
        rawData = read_raw_data()

        filteredData = filter_data(rawData)

        write_data_by_product_line(filteredData)

        print("Finished running the Pipeline_GreatOutdoors_demo pipeline")

prepare_retail_data()

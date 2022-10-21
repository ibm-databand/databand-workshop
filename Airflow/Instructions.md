# Airflow Integration Workshop Guide

1. Install Docker if not already on machine.
    * https://docs.docker.com/get-docker/
2. Build & run Docker image for Airflow
    1. `cd <path/to/databand-workhop/Airflow`
    1. `docker-compose up -d`
    1. Check status: `docker ps`, You should see Airflow containers running.
3. Check that Airflow is running without errors on localhost:8080
    * username: `airflow`
    * password: `airflow`
4. Run both DAGs via Airflow webserver
5. Login to Databand using credentials:
    * url: https://ibm-bp-demo.databand.ai
    * username: `artefact_user`
    * password: `DatabandIBM!2022`
6. Create a new Airflow Sync Config:
    1. Add any Airflow URL, this is required but doesn't need to a valid address
    1. Give your syncer a name
    1. Check the **Include source code** option
    1. Continue to the **Connect Airflow Syncer** section
    1. **Add json code to Airflow before clicking Test Connection**
7. Add connection back in Airflow webserver:
    1. Navigate to **Admin -> Connections** page
    1. Add a new connection
        * Connection Id: **dbnd_config**
        * Connection Type: **HTTP**
        * Extra: **JSON code from previous step**
    1. Save connection
8. Complete syncer setup:
    1. Check: **I've applied this configuration in Airflow**
    1. Select: **Test Connection** (This may prompt an error, you can ignore this)
9. Review Databand
    * In list of syncers, select three dots beside your newly created syncer and select **validate**
    * Your syncer should now be connected
    * Go back to dashboard, and select your syncer name in the source filter
10. Happy monitoring!
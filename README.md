# wrldc_mis_state_files_ingestion
python script that reads wrldc state files and stores the data in a database

## Useful info
* historical state files location - \\10.2.100.63\g$\ETL\03_SCADA\OperationalData
* state files status list web page in reporting software website - https://reporting.wrldc.in/POSOCOUI/FileUpload/OperationalDataFileList
* demand met = restricted demand = catered demand (incl aux consumption)
* unrestricted demand = restricted demand + load shedding (scheduled + unscheduled)

## Workflow
* Get the files info from 'file_mapping' sheet
* Iterate through each file
* Open file and store in openpyxl object
* Get the entity metrics info in 'meas_info' sheet
* Get address for each entity metric and store in database table in the format (timestamp, entity_tag, metric_name, value)

## Aggregations and equations while reading data from file
* The address column may have multiple cells
* The aggregation strategy can be any one of 'average', 'sum' or 'equation'
* If the aggregation strategy is 'equation', then the metric value will be the evaluated expression by substituting the values in equation placeholders ({{0}} will be substituted by first address value, {{1}} will be substituted by second address value etc)

## Links
* read excel sheet cell value by address from xlsx file using openpyxl python - https://stackoverflow.com/questions/22613272/how-to-access-the-real-value-of-a-cell-using-the-openpyxl-module-for-python
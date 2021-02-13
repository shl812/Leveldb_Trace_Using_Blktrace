# Leveldb_Trace_Using_Blktrace

## Tracing File Structure

```
.
├─ README.md
├─ config.sh
├─ Trace
|   ├─ data
|   |   ├─ blk_data.txt
|   |   └─ parsing_data.csv
|   └─ src
|       ├─ trace_leveldb.py
|       └─ parsing.py
├─ Kmeans
|   ├─ data
|   |   ├─ time_data.csv
|   |   └─ parsing_data.csv
|   └─ src
|       └─ k_blk.py
```

|Directory|Explanation|
|---------|-----------|
|InitData| TripFiles Download and unzip |
|RefineData| Classify the data using normalized values and create a refined refine_file.csv file |


|Source code|Explanation|Data|
|----|-----------|------|
|README.md|||
|config.sh| Enables configurations and install at once ||
|Estimator.sh| All programs can be executed ||
|vlogger.py| Download TripFiles from Firebase |TripFiles|
|unzip.sh| TripFiles: trip file unzip |unzip TripFiles|
|service_account.json| Google Storage account file ||
|refine_classified.sh| Classify TripFiles according to conditions |RefineFiles|

## Configuration and Install

Configuration and API Install code.

	# sudo source config.sh


## Estimator

### Usage Help
	
	# ./Estimator.sh -h

or

	# ./Estimator.sh -?

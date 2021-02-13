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
└─ Kmeans
    ├─ data
    |   ├─ time_data.csv
    |   └─ parsing_data.csv
    └─ src
        └─ k_blk.py
```

|Directory|Explanation|
|---------|-----------|
|Trace| TripFiles Download and unzip |
|Kmeans| Classify the data using normalized values and create a refined refine_file.csv file |


|Source code|Explanation|Data|
|----|-----------|------|
|README.md|||
|config.sh| Enables configurations and install at once ||
|blk_data.txt| All programs can be executed ||
|parsing_data.csv| Download TripFiles from Firebase |TripFiles|
|trace_leveldb.py| TripFiles: trip file unzip |unzip TripFiles|
|parsing.py| Google Storage account file ||
|time_data.csv| Classify TripFiles according to conditions |RefineFiles|
|k_blk.py| Google Storage account file ||


## Configuration and Install

Configuration and API Install code.

	# sudo source config.sh


## Estimator

### Usage Help
	
	# ./Estimator.sh -h

or

	# ./Estimator.sh -?

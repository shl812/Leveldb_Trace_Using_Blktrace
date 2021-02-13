# Leveldb_Trace_Using_Blktrace

## Tracing File Structure

```
.
├─ README.md
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
|Trace| Trace file parsing and make csv |
|Kmeans| Clustering using csv |


|Source code|Explanation|Data|
|----|-----------|------|
|README.md|||
|blk_data.txt| Leveldb tracing data ||
|parsing_data.csv| Parsing data |blk_data.txt|
|trace_leveldb.py| Leveldb trace through blktrace |unzip TripFiles|
|parsing.py| Parsing blk_data to generate csv ||
|time_data.csv|  ||
|k_blk.py| Google Storage account file ||


## Configuration and Install

Configuration and API Install code.

	# sudo source config.sh


## Estimator

### Usage Help
	
	# ./Estimator.sh -h

or

	# ./Estimator.sh -?

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
|parsing_data.csv| Parsing data ||
|trace_leveldb.py| Leveldb trace through blktrace ||
|parsing.py| Parsing blk_data to generate csv |blk_data.txt|
|time_data.csv|  ||
|k_blk.py| Google Storage account file |parsing_data.csv, time_data.csv|


## Tracing

Configuration and API Install code.

	# sudo source config.sh


## Estimator

### Usage Help
	
	# ./Estimator.sh -h

or

	# ./Estimator.sh -?

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
|Overspeed| Counts the number of overspeed by comparing the user's driving DB with the road information DB |
|Groundtruth| Using clustering algorithms, we create groundtruth to be used in the driving score |
|Regression| Groundtruth-based Driving Score Estimate is performed using regression algorithms |

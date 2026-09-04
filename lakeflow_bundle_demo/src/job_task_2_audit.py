rows_loaded = dbutils.jobs.taskValues.get(
    taskKey="ingest_task",
    key="rows_loaded"
)

print("Received rows_loaded =", rows_loaded)
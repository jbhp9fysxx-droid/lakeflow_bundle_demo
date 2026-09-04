rows_loaded = 12540

dbutils.jobs.taskValues.set(
    key="rows_loaded",
    value=rows_loaded
)

print("Published rows_loaded =", rows_loaded)
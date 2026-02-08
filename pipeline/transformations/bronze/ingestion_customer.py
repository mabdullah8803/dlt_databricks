import dlt

@dlt.table(
    name="customers_stg"
)

def customers_stg():
    df=spark.readStream.table("dlt_pipeline.dlt_schema.customers")
    return df
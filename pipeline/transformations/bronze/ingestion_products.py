import dlt

@dlt.table(
    name="products_stg"
)

def products_stg():
    df=spark.readStream.table("dlt_pipeline.dlt_schema.products")
    return df
import dlt
from pyspark.sql.functions import *

dlt.create_streaming_table(
    name="sales_stg"
)


#creating east sales flow
@dlt.append_flow(target="sales_stg")
def east_sales():
    df=spark.readStream.table("dlt_pipeline.dlt_schema.sales_east")
    return df


@dlt.append_flow(target="sales_stg")
def west_sales():
    df=spark.readStream.table("dlt_pipeline.dlt_schema.sales_west")
    return df
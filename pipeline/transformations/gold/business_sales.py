import dlt
from pyspark.sql.functions import *

# creating a MAT business view:
@dlt.table(
    name="business_sales"
)
def business_sales():
    df_fact=spark.read.table("fact_sales")
    df_dimProd=spark.read.table("dim_product")
    df_dimCus=spark.read.table("dim_customers")


    df_join=df_fact.join(df_dimCus,df_fact.customer_id==df_dimCus.customer_id,"inner").join(df_dimProd,df_fact.product_id==df_dimProd.product_id,"inner")

    df_prune=df_join.select("region","category","total_amount") 
    df_agg=df_prune.groupBy("region","category").agg(sum("total_amount").alias("total_sales"))
    return df_agg

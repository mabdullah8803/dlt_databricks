import dlt


#create empty stream table
dlt.create_streaming_table(
    name="dim_product",
)

dlt.create_auto_cdc_flow(
    target = "dim_product",
    source = "products_enr_view",
    keys = ["product_id"],
    sequence_by = "last_updated",
    ignore_null_updates = False,
    apply_as_deletes = None,
    apply_as_truncates = None,
    column_list = None,
    except_column_list = None,
    stored_as_scd_type = 2,
)
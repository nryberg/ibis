import ibis

con = ibis.connect("duckdb://penguins.ddb")
con.create_table(
    "penguins", ibis.examples.penguins.fetch().to_pyarrow(), overwrite=True
)

con = ibis.connect("duckdb://penguins.ddb")
con.list_tables()

penguins = con.table("penguins")
print(penguins.head())

print(penguins.head().to_pandas())

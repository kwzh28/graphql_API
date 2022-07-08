import snowflake.connector

ctx = snowflake.connector.connect(
user='<username>',
password='<password>',
account='<accountname>'
)
cs = ctx.cursor()
try:
    cs.execute("SELECT current_version()")
    one = cs.fetchone()
    print(one[0])
finally:
    cs.close()
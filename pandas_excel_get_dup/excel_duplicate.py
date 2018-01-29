# We will use data structures and data analysis tools provided in Pandas library
import pandas as pd

# Import retail sales data from an Excel Workbook into a data frame
#path = '/Documents/analysis/python/examples/2015sales.xlsx'
#path = 'F:/python/an.xlsx'
path = 'an.xlsx'
xlsx = pd.ExcelFile(path)
df = pd.read_excel(xlsx, 'Sheet1')

# Let's add a new boolean column to our dataframe that will identify a duplicated order line item (False=Not a duplicate; True=Duplicate)
df['is_duplicated'] = df.duplicated(['ip'])

# We can sum on a boolean column to get a count of duplicate order line items
#df['is_duplicated'].sum()

# Now let's quantify the impact of duplicate line items in terms of over counted units sold
#df[df['is_duplicated']].order_item_quantity.sum()

# With Python, we can use 'vectorizing' to multiple two columns and place the result in a new column
# This saves us from having to loop over every row in our sales data
#df['line_item_total'] = df.order_item_quantity * df.order_item_cost_price

# We can use our boolean sum shortcut again to get the sum of revenue from duplicated order line items
#df[df['is_duplicated']].line_item_total.sum()

# We are only interested in the non-duplicated order line items, so let's get those now
#df_nodup = df.loc[df['is_duplicated'] == False]
df_dup = df.loc[df['is_duplicated'] == True]

# Let's do a quick sanity check to make sure we now have a dataset with no identified duplicate order line items
#df_nodup[df_nodup['is_duplicated']].line_item_total.sum()

# Finally let's save our cleaned up data to a csv file
df_dup.to_csv('dup.csv', encoding='utf-8')
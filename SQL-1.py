# %%
import sqlite3
import pandas as pd


# %%
# make a connection to our database
con = sqlite3.connect('sakila.db')

# %%

# we'll use this function to query our database


def sql_to_df(sql_query):
    df = pd.read_sql(sql_query, con)
    return df


# %%

query = '''

SELECT *
FROM sqlite_master
WHERE type = 'table';

'''

tables = sql_to_df(query)
tables


# %%
query = ''' 
    SELECT first_name,last_name 
    FROM customer
'''

customer_names = sql_to_df(query)
customer_names

# %%
# head gives some info on the first five entries
print(customer_names.head())
# %%
# tail gives some info on the last five entries
print(customer_names.tail())

# %%
# describe and info give more detailed information on the dataset as a whole
print(customer_names.describe())

# %%
print(customer_names.info())


# %%

query = ''' SELECT * FROM film '''

film_list = sql_to_df(query)
print(film_list.head())
print(film_list.info())


# %%
# let's query for films with pastry in the description
query = ''' 
    SELECT *
    FROM film 
    WHERE description
    LIKE '%Pastry%'
    
'''

pastry_films = sql_to_df(query)
pastry_films
pastry_films.describe()


# %%
# now let's try grouping those pastry films by rating
query = ''' 
    SELECT 
        COUNT(title) as Count,
        rating AS Rating
    FROM film 
    WHERE description
    LIKE '%Pastry%'
    GROUP BY rating
    ORDER By Count DESC;
    
'''

pastry_films_by_rating = sql_to_df(query)
pastry_films_by_rating

# %%
pastry_films_by_rating.describe()

# %%
# we can get a basic plot using hist; sometimes it's useful for a quick peek
pastry_films_by_rating.hist(column='Count', grid=False)

# %%

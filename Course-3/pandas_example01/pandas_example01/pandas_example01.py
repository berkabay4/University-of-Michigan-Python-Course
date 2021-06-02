### Pandas
import pandas as pd

## Read csv file
df = pd.read_csv('Pokemon.csv')
print(df)
print('\n')

## Read excel file
# df_xlsx = pd.read_excel('pokemon_data.xlsx')

## Read text file
# df_txt = pd.read_csv('pokemon_data.txt', delimiter= '\t')

## Print first 3 row
print(df.head(3))
print('\n')

## Print last 3 row
# print(df.tail(3))


### Reading data in Pandas

## Read Headers
# print(df.columns)
# print('\n')

## Read each Column
print(df['Name'][0:5])           # List Name 0 to 5
print('\n')

# print(df.Name)                 # List all Name 

# print(df[['Name', 'Type 1', 'HP']])     # Read more than 1

## Read Each Row
# print(df.head(4))

print(df.iloc[0:4])
print('\n')

## Read a specific Location (R,C)
print("Specific Location (1,1) -> ", df.iloc[1,1])
print('\n')

## Iterr each row
# for index, row in df.iterrows():
#     print(index, row)
#      print(index,row['Name'])

## Find with specific data witht loc
fire_pokemons = df.loc[df['Type 1'] == "Fire"]  # Show only Type 1 = Fire
print(fire_pokemons[0:10])
print('\n')


### Sorting/Describing Data

## mean, std, min, %25, %50...
print(df.describe()) 
print('\n')

## Sorting
print('----Sorted List----\n')
# Type 1 -> ascending, HP -> descending
print( df.sort_values(['Type 1', 'HP'], ascending = [1,0])[0:5] )
print('\n')

### Making changes to the data 

## Add new column
# sum(axis = 1) horizontal sum(axis = 0) vertical
df['Total'] = df.iloc[:, 4:10].sum(axis = 1)
print(df.head(10))
print('\n')

## Delete column
# df = df.drop(columns = ['Total'])


## Reorder columns
cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

print(df.head(5))
print('\n')

### Saving our Data (Exporting into Desired Format)

## Export as CSV
df.to_csv('modified_pokemon.csv', index = True) 

## Export as Excel 
# df.to_excel('modified_pokemon.xlsx', index = False) 

## Export as Text
df.to_csv('modified_pokemeon.txt', index = False, sep ='\t')      # '\t'-> sep with tabs


### Filtering Data
print('Fire & Grass Pokemons List\n')
new_df = list_firegrass = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 10)]


print(new_df)       # Index numbers are not in order
print('\n')

## Reset Index 
print('---New Dataframe---\n')
new_df.reset_index(drop = True, inplace = True)

print(new_df)
print('\n')


print('----Mega Pokémons List-----\n')
df_mega = new_df.loc[df['Name'].str.contains('Mega')]           # Find which names are contains 'Mega' 

print(df_mega.head(5))                                      # print first 5 name in df_mega
print('\n')


# Delete Mega and %..Forms Pokémons names in new_df

print('----Mega, Size, Mode, %Form Pokémons are deleted in new_df----\n')
new_df = new_df.loc[~df['Name'].str.contains('Mega') & 
                ~new_df['Name'].str.contains('Mode') &
                ~new_df['Name'].str.contains('Size') &
                ~new_df['Name'].str.contains('Forme')]           # Find which names are not contains 'Mega', 'Forme', etc.

for index,rows in new_df.iterrows():
    print(index,rows['Name'])


### Conditional Changes

## Change Fire to Flamer
df.loc[df['Type 1'] == 'Fire', 'Type 1'] ='Flamer'
print('----Fire = Flamer----\n')
print(df.head(25))
print('\n')


## Change all Fire Pokémons to Legendary
df.loc[df['Type 1'] == 'Flamer', 'Legendary'] = True

print('----All Flamer Pokémons are Legendary!----\n')
print(df.head(25))
print('\n')

print('----Change 2 Value----\n')

df.loc[df['Total'] > 250, ['Generation', 'Legendary']] = ['TG', 'TL']
print(df)
print('\n')


print('----Change Normal----\n')
df = pd.read_csv('modified_pokemeon.txt', delimiter = '\t' )
print(df)
print('\n')

### Aggregate Statistics (Groupby)

## Mean
df_type1mean = df.groupby(['Type 1']).mean().sort_values('Defense', ascending = False)
print('----Type 1 Defense Mean List [Descending]----\n')
print(df_type1mean.head(3))
print('\n')

print('In Type 1 Steel Pokémon type have highest Defense Value')
print('\n')

df_type1mean = df.groupby(['Type 1']).mean().sort_values('Attack', ascending = False)
print('----Type 1 Attack Mean List [Descending]----\n')
print(df_type1mean.head(3))
print('\n')

print('In Type 1 Dragon Pokémon type have highest Attack Value')
print('\n')

## Sum
df_type1sum = df.groupby(['Type 1']).sum()
print('----Sum----\n')
print(df_type1sum.head(5))
print('\n')

## Count
df_type1count = df.groupby(['Type 1']).count()
print('----Count----\n')
print(df_type1count.head(5))
print('\n')

# For delete useless columns 
df['count'] = 1
df_type1count = df.groupby(['Type 1']).count()['count']
print('----Count Again----\n')
print(df_type1count)
print('\n')

df_type1count = df.groupby(['Type 1', 'Type 2']).count()['count']
print('----Count Type 2 and Type 1----\n')
print(df_type1count)
print('\n')


### Working with large amounts of data
print('----Working with large amounts of data----\n\n')

# df = pd.read_csv('modified.csv')   #load everything 
for df in pd.read_csv('Pokemon.csv',chunksize = 5):
    print(df)

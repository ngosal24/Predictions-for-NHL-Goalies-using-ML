import pandas as pd

# import datasets
data1213 = pd.read_csv("12_13.csv", header = 0)
data1314 = pd.read_csv("13_14.csv", header = 0)
data1415 = pd.read_csv("14_15.csv", header = 0)
data1516 = pd.read_csv("15_16.csv", header = 0)
data1617 = pd.read_csv("16_17.csv", header = 0)
data1718 = pd.read_csv("17_18.csv", header = 0)
data1819 = pd.read_csv("18_19.csv", header = 0)
data1920 = pd.read_csv("19_20.csv", header = 0)
data2021 = pd.read_csv("20_21.csv", header = 0)
data2122 = pd.read_csv("21_22.csv", header = 0)
data2223 = pd.read_csv("22_23.csv", header = 0)

# combine all data sets
goalieData = pd.concat([data1213, data1314, data1415, data1516, data1617, data1718, data1819, data1920, data2021, data2122, data2223])
goalieData = goalieData.sort_values(by=['season', 'name'])

# filter out unneeded situations (only need 'all' to summarize each goalie-season)
goalieData = goalieData[goalieData['situation'] == 'all']

# filter out goalie-seasons with less than 20 games played
goalieData = goalieData[goalieData['games_played'] >= 20]

# drop penalty columns
goalieData = goalieData.drop(['penalityMinutes', 'penalties', 'position', 'situation'], axis = 1)

# add save percentage column for the current season (not included for some reason?)
goalieData['sv_pct'] = 1 - (goalieData['goals'] / goalieData['ongoal'])

# add 'y' column - the following season's save percentage
# helper function to find next sv%, if it exists
def find_next_sv_pct(goalieName, year):
    if goalieData.loc[(goalieData['name'] == goalieName) & (goalieData['season'] == year + 1)].any().all():
        result = (goalieData.loc[(goalieData['name'] == goalieName) & (goalieData['season'] == year + 1)])['sv_pct']
        result = result.iloc[0]
    else:
        result = None
    return result

goalieData['next_sv_pct'] = goalieData.apply(lambda row: find_next_sv_pct(row['name'], row['season']), axis = 1)

# remove seasons where there is no prediction to be made (player didn't play 20+ games the following season)
goalieData = goalieData[goalieData['next_sv_pct'].notna()]

# write to file
goalieData.to_csv("data.csv")

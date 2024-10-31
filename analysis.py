import pandas as pd
import statsmodels.api as sm

users_df = pd.read_csv('users.csv')
repos_df = pd.read_csv('repositories.csv')

#Q1- Sort by 'followers' in descending order
top_users = users_df.sort_values(by='followers', ascending=False).head(5)

# Get the 'login' of the top 5 users as a comma-separated string
top_5_logins = ", ".join(top_users['login'].tolist())
print("Top 5 users by followers:", top_5_logins)

#Q2- Convert 'created_at' to datetime format for accurate sorting
users_df['created_at'] = pd.to_datetime(users_df['created_at'])

# Sort by 'created_at' in ascending order to get the earliest users
earliest_users = users_df.sort_values(by='created_at').head(5)

# Get the 'login' of the 5 earliest users as a comma-separated string
earliest_5_logins = ", ".join(earliest_users['login'].tolist())
print("5 Earliest Registered Users by login:", earliest_5_logins)

 #Q3-Filter out rows with missing licenses
repos_with_licenses = repos_df[repos_df['license_name'].notna()]

# Count each unique license and get the top 3 most popular
top_licenses = repos_with_licenses['license_name'].value_counts().head(3)

# Get the top 3 license names as a comma-separated string
top_3_licenses = ", ".join(top_licenses.index.tolist())
print("3 Most Popular Licenses:", top_3_licenses)

# Q4-Drop rows with empty company names
companies = users_df[users_df['company'].notna()]

# Find the most common company
top_company = companies['company'].value_counts().idxmax()
print("Most common company:", top_company)

#Q5- Drop rows with missing language information
repos_with_language = repos_df[repos_df['language'].notna()]

# Find the most common language
most_popular_language = repos_with_language['language'].value_counts().idxmax()
print("Most popular programming language:", most_popular_language)

users_df['created_at'] = pd.to_datetime(users_df['created_at'])

#Q6- Filter users who joined after 2020
recent_users = users_df[users_df['created_at'] > "2020-01-01"]

# Get their logins to filter the repositories
recent_user_logins = recent_users['login'].tolist()

# Filter repositories to include only those by recent users
recent_repos = repos_df[repos_df['login'].isin(recent_user_logins) & repos_df['language'].notna()]

# Find the second most common language
second_most_popular_language = recent_repos['language'].value_counts().index[1]
print("Second most popular language for users who joined after 2020:", second_most_popular_language)

# Q7-Calculate average stars per language
avg_stars_per_language = repos_df.groupby('language')['stargazers_count'].mean().sort_values(ascending=False)

# Get the language with the highest average stars
language_with_highest_avg_stars = avg_stars_per_language.idxmax()
print("Language with highest average stars per repository:", language_with_highest_avg_stars)

#Q8-Calculate leader strength
users_df['leader_strength'] = users_df['followers'] / (1 + users_df['following'])
top_leader_strength_users = users_df.sort_values(by='leader_strength', ascending=False).head(5)
# Get the 'login' of the top 5 users as a comma-separated string
top_5_leader_strength_logins = ", ".join(top_leader_strength_users['login'].tolist())
print("Top 5 users by leader strength:", top_5_leader_strength_logins)
#Q9
correlation_followers_repos = users_df['followers'].corr(users_df['public_repos'])
# Format to 3 decimal places
correlation_followers_repos_rounded = round(correlation_followers_repos, 3)
print("Correlation between followers and public repositories:", correlation_followers_repos_rounded)

#Q10-Define the independent variable (public_repos) and dependent variable (followers)
X = users_df['public_repos']
y = users_df['followers']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
slope = model.params['public_repos']
slope_rounded = round(slope, 3)
print("Regression slope of followers on public repositories:", slope_rounded)

#Q11 Calculate correlation between 'has_projects' and 'has_wiki'
repos_df['has_projects'] = repos_df['has_projects'].astype(int)  # Convert boolean to int (True=1, False=0)
repos_df['has_wiki'] = repos_df['has_wiki'].astype(int)
correlation_projects_wiki = repos_df['has_projects'].corr(repos_df['has_wiki'])
correlation_projects_wiki_rounded = round(correlation_projects_wiki, 3)
print("Correlation between projects enabled and wiki enabled:", correlation_projects_wiki_rounded)

#Q12 Calculate averages
avg_following_hireable = users_df[users_df['hireable'] == True]['following'].mean()
avg_following_non_hireable = users_df[users_df['hireable'] == False]['following'].mean()
average_following_difference = round(avg_following_hireable - avg_following_non_hireable, 3)
print("Average following difference (hireable - non-hireable):", average_following_difference)

#Q13- Remove users without bios and calculate bio word count
users_df['bio_word_count'] = users_df['bio'].apply(lambda x: len(str(x).split()) if pd.notna(x) else 0)
users_with_bios = users_df[users_df['bio_word_count'] > 0]
# Define independent variable (bio word count) and dependent variable (followers)
X_bio = users_with_bios['bio_word_count']
y_followers = users_with_bios['followers']
X_bio = sm.add_constant(X_bio)
model_bio = sm.OLS(y_followers, X_bio).fit()
bio_slope = model_bio.params['bio_word_count']
bio_slope_rounded = round(bio_slope, 3)
print("Regression slope of followers on bio word count:", bio_slope_rounded)

#Q14-Convert 'created_at' to datetime format
repos_df['created_at'] = pd.to_datetime(repos_df['created_at'])
# Extract the day of the week (0=Monday, 6=Sunday)
repos_df['day_of_week'] = repos_df['created_at'].dt.dayofweek
# Filter for weekends (Saturday=5, Sunday=6)
weekend_repos = repos_df[repos_df['day_of_week'].isin([5, 6])]
# Count repositories created by each user
top_weekend_users = weekend_repos['login'].value_counts().head(5)
# Get the top 5 user logins as a comma-separated string
top_5_weekend_users_logins = ", ".join(top_weekend_users.index.tolist())
print("Top 5 users who created the most repositories on weekends:", top_5_weekend_users_logins)

#Q15 Calculate fractions of users with email addresses
fraction_hireable = users_df[users_df['hireable'] == True]['email'].notna().mean()
fraction_non_hireable = users_df[users_df['hireable'] == False]['email'].notna().mean()
email_fraction_difference = round(fraction_hireable - fraction_non_hireable, 3)
print("Difference in email sharing fraction:", email_fraction_difference)


# 16. Most common surname
users_df['surname'] = users_df['name'].str.split().str[-1]
common_surnames = users_df['surname'].value_counts()
most_common_surname = common_surnames.idxmax()
most_common_surname_count = common_surnames.max()
print(f"Ans 16 : Most common surname: {most_common_surname} with {most_common_surname_count} users")
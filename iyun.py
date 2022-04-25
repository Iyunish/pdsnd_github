 #https://stackoverflow.com/questions/36010999/convert-pandas-datetime-month-to-string-representation
#Python-for-Data-Analysis-2nd-Edition.pdf
#https://realpython.com/pandas-groupby/#:~:text=The%20%E2%80%9CHello%2C%20World!%E2%80%9D%20of%20Pandas%20GroupBy,-Now%20that%20you&text=You%20call%20.,a%20single%20column%20name%20to%20.
#https://www.geeksforgeeks.org/how-to-combine-groupby-and-multiple-aggregate-functions-in-pandas/?ref=lbp
#https://stackoverflow.com/questions/2847386/python-strings-and-integer-concatenation
#https://stackoverflow.com/questions/19377969/combine-two-columns-of-text-in-pandas-dataframe
#https://stackoverflow.com/questions/19384532/get-statistics-for-each-group-such-as-count-mean-etc-using-pandas-groupby
#https://stackoverflow.com/questions/47950227/what-is-the-meaning-of-modex-mode0
#https://www.datainsightonline.com/post/exploring-us-bikeshare-data-project


import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

DAY_DATA = ['monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    username = input('To get started, kindly enter your name\n').title()
    print('Hello', username,'!' 'Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    
    city_name = ''
    while city_name.lower() not in CITY_DATA:
        city_name = input("\nWhat city would you like to analyze data for?\nInput either new york city, chicago or washington\n")
        if city_name.lower() in CITY_DATA:
            city = CITY_DATA[city_name.lower()]
        else:
            print("oops! Please input either New York City, Washington or Chicago.\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    month_name = ''
    while month_name.lower() not in MONTH_DATA:
        month_name = input("\nWould you like to filter data by month? (Input either january, february, ... , june) or 'all' to apply no month filter \n")
        if month_name.lower() in MONTH_DATA:
            month = month_name.lower()
        else:
            print("oops! try again with january, february, ..., june or all as input \n")
    day_name = ''
    while day_name.lower() not in DAY_DATA:
        day_name = input("\nWould you like to filter data by day? (Input either monday, tuesday, ...,sunday or 'all' to apply no day filter\n")
        if day_name.lower() in DAY_DATA:
            day = day_name.lower()
        else:
            print("oops! try again with a day of the week\n")       
    print('='*60)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(city)# load data file into a dataframe
    df['Start Time'] = pd.to_datetime(df['Start Time'])# convert start time column to datetime
    
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all': 
        month = MONTH_DATA.index(month) + 1       
        df = df.loc[df['month'] == month] 

    if day != 'all': 
        df = df.loc[df['day'] == day.title()]
    
       
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    most_freq_month = df['month'].mode()[0] # TO DO: display the most common month
    print('The Most Common Month is:  ' + MONTH_DATA[most_freq_month].title())

    most_freq_day = (df['day'].mode()[0]) # TO DO: display the most common day of week
    print('The Most Common Day of the Week is:  ', most_freq_day)

    most_freq_hour = (df['hour'].mode()[0]) # TO DO: display the most common start hour
    print('The Most Common Start Hour is:  ', most_freq_hour,':00')
    
    print("\nThis took %s seconds." % round((time.time() - start_time)))
    print('='*60)
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    start_station_m = df['Start Station'].mode()[0] # TO DO: display most commonly used start station
    print("The Most Commonly Used Start Station is:  ", start_station_m)
    
    end_station_m = df['End Station'].mode()[0]  # TO DO: display most commonly used end station
    print("The Most Commonly End Station is:  ", end_station_m)
    
    combined_trip_m = (df['Start Station'] + "||" + df['End Station']).mode()[0]  # TO DO: display most frequent combination of start station and end station trip
    print ("The Most Frequent Combos for Both Start and End Stations are:  "+ str(combined_trip_m.split("||")))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*60)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_trip_duration = df['Trip Duration'].sum()   # TO DO: display total travel time
    print("The Total Trip Duration in the filtered data is:    "+ str(total_trip_duration))
    
    mean_trip_duration = df['Trip Duration'].mean()    # TO DO: display mean travel time
    print("The Mean Trip Duration in the filtered data is:    "+str(mean_trip_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*60)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_type_count = df.groupby('User Type')['User Type'].count()  # TO DO: Display counts of user types
    print('User Type and total number of Users is \n',  user_type_count)

    if city != 'washington.csv': # includes a condition because the washington table is missing the Gender and Birth Year columns
        gender_count = df.groupby('Gender')['Gender'].count()  # TO DO: Display counts of gender
        print('The Total number of gender is \n', gender_count)
    
        earliest_year = int(df['Birth Year'].min())  # TO DO: Display earliest, most recent, and most common year of birth
        print('The Earliest Birth Year is: ', earliest_year)
    
        most_recent_year = df['Birth Year'].max().astype(int)
        print('The Most Recent Birth Year is: {}'.format(most_recent_year))
    
        most_common_year = int(df['Birth Year'].mode()[0])
        print('The Most Common Birth Year is: ', (most_common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*60)
    
def raw_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower() 
    start_loc = 0
    while True:
        if view_data.lower() == 'yes':
            print(df.iloc[start_loc: start_loc + 5])
            start_loc += 5
            view_data = input("Do you wish to continue?: Enter yes or no\n").lower()
        else:
            break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df) 
        user_stats(df, city)
        raw_data(df)
        

        restart = input('\nWould you like to restart? Enter yes 'Y' or no 'N'.\n')
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
    main()

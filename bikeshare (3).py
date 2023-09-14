import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # Get user input for city (chicago, new york city, washington)
    while True:
        city = input("Choose a city name (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Please enter a correct city name.")
    
    # Get user input for month (all, january, february, ..., june)
    while True:
        month = input("Choose a month (all, january, february, ..., june): ").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print('Wrong month.')
    
    # Get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Choose a day of the week (all, monday, tuesday, ... sunday): ").lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print('Wrong day .')
    
    print('-' * 40)
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])

    # Convert 'Start Time' to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract month, day, and hour from 'Start Time'
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # Filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # Filter by day of week
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is: {common_month}')

    # Display the most common day of the week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day of the week is: {common_day}')

    # Display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The most common start hour is: {common_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common start station is: {common_start_station}')

    # Display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common end station is: {common_end_station}')

    # Display most frequent combination of start station and end station trip
    df['Route'] = df['Start Station'] + " to " + df['End Station']
    common_route = df['Route'].mode()[0]
    print('The most common route is: {common_route}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: {total_travel_time} seconds')

    # Display average travel time
    average_travel_time = df['Trip Duration'].mean()
    print('Average travel time: {average_travel_time} seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print('Counts of user types:\n', user_type_counts)

    if 'Gender' in df:
        # Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print('Counts of gender:\n', gender_counts)
        
        # Display earliest, most recent, and most common year of birth
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        common_birth_year = int(df['Birth Year'].mode()[0])
        print('Earliest birth year: {earliest_birth_year}')
        print('Most recent birth year: {most_recent_birth_year}')
        print('Most common birth year: {common_birth_year}')
    else:
        print('Gender and birth year data not available for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def display_data(df):
    b = 0
    user_input = input('Would you like to display 5 rows of raw data? (yes/no): ').lower()
    
    if user_input == 'yes':
        while b < df.shape[0]:
            print(df.iloc[b:b+5])
            b += 5
            more_data = input('Would you like to see more data? (yes/no): ').lower()
            if more_data != 'yes':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
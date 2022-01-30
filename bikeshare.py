import time
import pandas as pd
import numpy as np


city_data = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_data = {'all','january','february','march','april','may','june'}

day_data = {'all','monday','tuesday','wednesday','thursday','friday','saturday','sunday'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Would you like to see the data for chicago, new york, or washington? ").lower()
    while city not in city_data.keys():
        city = input("Oops, please try again and choose from Chicago, New York, or Washington: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please type in the month/s you like to analyze: all, january, february, ... , june: ").lower()
    while month not in month_data:
        month = input("Oops, please try again and type in the month/s you like to analyze: all, january, february, ... , june: ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please type in a day to analyze: all, monday, tuesday, ... , sunday: ").lower()
    while day not in day_data:
        day = input("Oops, please try again and type in the day/s you like to analyze: all, monday, tuesday, ... , sunday: ").lower()


    print('-'*40)
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
    #received help in the upcoming part from the useful comments in the mentor forum and partially oriented my code on the input from there
    df = pd.read_csv(city_data[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #print(df['Start Time'])
    df['month']=df['Start Time'].dt.month_name()
    print(df['month'])
    df['day_of_week']=df['Start Time'].dt.day_name()
    df['hour_of_day']=df['Start Time'].dt.hour


    if month != 'all':
       df =df[df['month'].str.lower() == month]

    if day != 'all':
       df =df[df['day_of_week'].str.lower() == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()
    print("The most common month is ", most_common_month)


    # TO DO: display the most common day of week
    most_common_day_week = df['day_of_week'].mode()
    print("The most common day is ", most_common_day_week)


    # TO DO: display the most common start hour
    most_common_hour = df['hour_of_day'].mode()
    print("The most common hour is ", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_station = df['Start Station'].mode()
    print("The most common start station we calculated is: ", most_common_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()
    print("The most common end station we identified is: ", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination_of_stations = df['Start Station'] + df['End Station']
    most_common_combination = combination_of_stations.mode()
    print("The most common combination of start and end station is: ", most_common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    # Show the start and end points upon user request
    data_question = input("Do you like to see the first 5 rows of start and end stations? Enter yes or no: ").lower()
    comb_stat = 0
    if data_question not in ('yes','no'):
        data_question = input("Please try again and note: only yes or no are allowed inputs. Show data? Yes or no: ").lower()
    if data_question == 'no':
        return
    if data_question == 'yes':
        combination_start_end = df['Start Station'] + df['End Station']
        comb_stat += 5
        print(combination_start_end.head(comb_stat))
        view_request = input("Do you like to see 5 more? Yes or no: ").lower()
        while view_request == 'yes':
            combination_start_end = df['Start Station'] + df['End Station']
            comb_stat += 5
            print(combination_start_end.head(comb_stat))
            view_request = input("Do you like to see 5 more? Yes or no: ").lower()


  #  if data_question not in ('yes','no'):
      #  data_question = input("Do you like to see the first 5 rows of start and end stations? Enter yes or no").lower()
  #   if data_question == 'yes':
   #         combination_start_end = df['Start Station'] + df['End Station']
    #        print(combination_start_end.head(com_stat))
     #       comb_stat += 5
      #      view_request = input("Do you like to see 5 more orews of start and end stations? Enter yes or no").lower()

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    print("The total duration is: ", total_duration)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean duration is: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user_types = df['User Type'].value_counts(dropna=False)
    print("The counts of user types are: ", counts_user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        counts_gender = df['Gender'].value_counts(dropna=False)
        print("The counts of gender are: ", df['Gender'].value_counts(dropna=False))
    else:
        print("Gender data is not available here")


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_yob = df['Birth Year'].min()
        print("The earliest year of birth is: ", earliest_yob)
    else:
        print("This dataset does not include a birth year. Therefore, no earliest year of birth can be calculated.")

    if 'Birth Year' in df:
        recent_yob = df['Birth Year'].max()
        print("The most recent year of birth is: ", recent_yob)
    else:
        print("This dataset does not include a birth year. Therefore, no most recent year of birth can be calculated.")

    if 'Birth Year' in df:
        common_yob = df['Birth Year'].mode()
        print("The most common year of birth is: ", common_yob)
    else:
        print("This dataset does not include a birth year. Therefore, no most common year of birth can be calculated.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        display_data(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

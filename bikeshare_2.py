import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ""

    while city not in CITY_DATA.keys():
        print("\nPlease chose of this cities \n1) chicago \n2) new york city \n3) washington")
        city = input().lower()
        if city not in CITY_DATA.keys():
            print("\n please check your input ")
    print("\nYou have chosen {}".format(city.title()))


    # get user input for month (all, january, february, ... , june)
    months = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ""
    while month not in months.keys():
        print("\nEnter Month between january to june or Enter all for all of them")
        month = input().lower()
        if month not in months.keys():
            print("\nYou input an invalid data of month")
            print("Try another one")
            print("\nEnter Month between january to june or Enter all for all of them")

    print("\nYou have chosen {}".format(month.title()))

    # get user input for day of week (all, monday, tuesday, ... sunday)
    Days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ""
    while day not in Days:
        print("\nEnter one of day from monday to sunday or enter all for all of them")
        day = input().lower()
        if day not in Days:
            print("\nYou input an invalid data of day")
            print("Try another one")
            print("\nEnter one of day from monday to sunday or enter all for all of them")
    print("\nYou have chosen {}".format(day.title()))
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
    print("\nloading....")

    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df['hour'] = df['Start Time'].dt.hour
    df["day"] = df["Start Time"].dt.day_name()

    if month != "all":
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != "all":
        df = df[df['day'] == day.title()]

    print("\nDone!")
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_month = df["month"].mode()[0]
    print("\nThe most common month is {}".format(most_month))


    # display the most common day of week
    most_day = df["day"].mode()[0]
    print("\nThe most common day is {}".format(most_day))



    # display the most common start hour
    most_hour = df["hour"].mode()[0]
    print("\nThe most common hour is {}".format(most_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_start = df["Start Station"].mode()[0]
    print("\nmost commonly used start station is {}".format(most_start))

    # display most commonly used end station
    most_end = df["End Station"].mode()[0]
    print("\nmost commonly used end station is {}".format(most_end))


    # display most frequent combination of start station and end station trip
    df["Station"] = df[["Start Station", "End Station"]].agg(' to '.join, axis=1)
    most_freq = df["Station"].mode()[0]
    print("\nmost frequent combination of start station and end station trip {}".format(most_freq))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("\nThe total travel times is {} minute".format(total_travel_time / 60))

    # display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("\nThe mean travel times is {} minute".format(mean_travel_time / 60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df["User Type"].value_counts()
    print("\nThe count of user types is :- {}".format(user_type))

    # Display counts of gender
    try:
        Gender = df["Gender"].value_counts()
        print("\nThe counts of gender is {}".format(Gender))
    except:
        print("no Gender column in this dataset")



    # Display earliest, most recent, and most common year of birth
    try:
        earlist = df["Birth Year"].min()
        print("\nThe earlist birth year is {}".format(str(int(earlist))))

        most_recent = df["Birth Year"].max()
        print("\nThe most recent birth year is {}".format(str(int(most_recent))))

        most_common = df["Birth Year"].mode()[0]
        print("\nThe most common birth year is {}".format(str(int(most_common))))
    except:
        print("no Birth Year column in this dataset")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        row = 0

        while True:
            viewData = input("Would you like to see the raw data? Type 'Yes' or 'No'.").title()
            print(viewData)
            if viewData == 'Yes':
                data = df[row:row+5]
                print("Dataframe \n ")
                print(data)
                row += 5
            else:
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

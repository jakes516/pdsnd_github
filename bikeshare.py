#change made for refactoring
#change 2 made for refactoring
import time
import pandas as pd


CITY_DATA = { 'chicago': './chicago.csv',
              'new york city': './new_york_city.csv',
              'washington': './washington.csv' }

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
    
    while True:
        city = str(input('Enter a city: ').lower())
        if city in ('chicago', 'new york city', 'washington'):
            print('One moment')
            print('-'*40)
            break
        else:
            print('invalid city please enter chicago, new york, or washington')
    while True:
        month = str(input('Enter a month: ').lower())
        if month in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print('One moment')
            print('-'*40)
            break
        else:
            print('invalid month please enter "all" or a month from January to/including June')
    while True:
        day = str(input('Enter a day: ').lower())
        if day in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print('One moment')
            print('-'*40)
            break
        else:
            print('invalid day please enter "all" or any day of the week')
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
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
 
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df







def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].value_counts().idxmax()

    # TO DO: display the most common day of week

    popular_day = df['day_of_week'].value_counts().idxmax()

    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].value_counts().idxmax()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return popular_month, popular_day, popular_hour





def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().idxmax()

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].value_counts().idxmax()
    
    # TO DO: display most frequent combination of start station and end station trip
    df['Start and End Stations'] = df['Start Station'] + ' --> ' + df['End Station']
    
    popular_start_end_station_combo = df['Start and End Stations'].value_counts().idxmax()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return popular_start_station, popular_end_station, popular_start_end_station_combo


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Start and End Stations'] = df['Start Station'] + ' --> ' + df['End Station']
    
    total_travel_time = df[['Start and End Stations', 'Trip Duration']].groupby('Start and End Stations').sum()
    
    # TO DO: display mean travel time\
    mean_travel_time = df[['Start and End Stations', 'Trip Duration']].groupby('Start and End Stations').mean()
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return total_travel_time, mean_travel_time


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    if 'User Type' in df.columns:
        user_type_count = df['User Type'].value_counts() 
    else:
        user_type_count = print('\nNo user type data\n')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
    
        gender_count = df['Gender'].value_counts()
    else:
        gender_count = print('\nNo gender data\n')

    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:
        earliest_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].value_counts().idxmax()
    else:
        earliest_birth = print('\nNo birth year data\n')
        recent_birth = None
        common_birth = None

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return user_type_count, gender_count, earliest_birth, recent_birth, common_birth


def main():
    while True:
        user_input = get_filters()
        print(user_input)

        df = load_data(user_input[0], user_input[1], user_input[2])

        time_statistics = time_stats(df)
        print(time_statistics)
        print('Month, Day, Hour')
        
        station_statistics = station_stats(df)
        print(station_statistics)
        print('Popular Start Station, Popular End Station, Popular trip')
        
        trip_time_stats_sum, trip_time_stats_mean  = trip_duration_stats(df)
        print('Total Travel Time:')
        print(trip_time_stats_sum)
        print('Mean Travel Time:')
        print(trip_time_stats_mean)


        user_statistics = user_stats(df)
        print(str(user_statistics[0])+"\n")
        print(str(user_statistics[1])+"\n")
        print(str(user_statistics[2]) + ": Earliest Birth Year")
        print(str(user_statistics[3]) + ": Most Recent Birth Year")
        print(str(user_statistics[4]) + ": Most Common Birth Year")
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

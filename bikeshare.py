import time
import pandas as pd




CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# CITIES = ['chicago', 'new york', 'washington']

MONTHS_OF_YEAR = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS_OF_WEEK = ['sunday', 'monday', 'tuesday', 'wednesday',
        'Thursday', 'Friday', 'Saturday' ]

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
    while True:
        city = input('\nWhich city do you want to look at? Enter chicago, new york city  or washington?\n~ ')
        city = city.lower()
        if city == 'chicago' or city == 'new york city' or city == 'washington':
            break
        else:
            print('Please enter a valid city.')

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWhich month do you want to see?''enter month from January to June\n~').lower()
        if month in MONTHS_OF_YEAR:
            break;
        else:
            print('Please enter a valid month')
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\n Which day do you want to see?''enter day from Monday to Sunday\n~').lower()
        if day in DAYS_OF_WEEK:
            break;
        else:
            print('Please enter a valid day')
    print('-' * 40)
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        month = MONTHS_OF_YEAR.index(month) + 1
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is :", most_common_month)


    # display the most common day of week

    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of week is :", most_common_day_of_week)


    # display the most common start hour

    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is :", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    commonnest_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :", commonnest_start_station)


    # display most commonly used end station

    commonnest_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", commonnest_end_station)


    # display most frequent combination of start station and end station trip

    df['Combined Station'] = df['Start Station'] + ' to ' + df['End Station']
    common_combined_station = df['Combined Station'].mode()[0]
    print('Most common combination of start and end station is', common_combined_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)

    # display mean travel time

    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of user types:\n")
    user_counts = df['User Type'].value_counts()
    # iteratively print out the total numbers of user types
    for index, user_count in enumerate(user_counts):
        print("  {}: {}".format(user_counts.index[index], user_count))

    print()

    if 'Gender' in df.columns:
        user_stats_gender(df)

    if 'Birth Year' in df.columns:
        user_stats_birth(df)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats_gender(df):
    """Displays statistics of analysis based on the gender of bikeshare users."""

    # Display counts of gender
    print("Counts of gender:\n")
    gender_counts = df['Gender'].value_counts()
    # iteratively print out the total numbers of genders
    for index, gender_count in enumerate(gender_counts):
        print("  {}: {}".format(gender_counts.index[index], gender_count))

    print()


def user_stats_birth(df):
    """Displays statistics of analysis based on the birth years of bikeshare users."""

    # Display earliest, most recent, and most common year of birth
    birth_year = df['Birth Year']
    # the most common birth year
    most_common_year = birth_year.value_counts().idxmax()
    print("The most common birth year:", most_common_year)
    # the most recent birth year
    most_recent = birth_year.max()
    print("The most recent birth year:", most_recent)
    # the most earliest birth year
    earliest_year = birth_year.min()
    print("The most earliest birth year:", earliest_year)

def display_five_line_data(df):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.
    Args:
        data frame
    Returns:
        none
    '''
    def valid_data (show):
        if show.lower() in ['yes', 'no']:
            return True
        else:
            return False
    h = 0
    t = 5
    valid_input = False
    while valid_input == False:
        show = input('\nWould you like to see individual trip data? '
                        'Enter \'yes\' or \'no\'.\n')
        valid_input = valid_data(show)
        if valid_input == True:
            break
        else:
            print("Sorry, I do not have access to your input. Please enter 'yes' or"
                  " 'no'.")
    if show.lower() == 'yes':
        # print all columns except the 'journey' column created in statistics()
        print(df[df.columns[0:5]].iloc[h:t])
        show_more = ''
        while show_more.lower() != 'no':
            valid_data_input = False
            while valid_data_input == False:
                show_more = input('\nWould you like to explore more individual'
                                     ' trip data? Enter \'yes\' or \'no\'.\n')
                valid_data_input = valid_data(show_more)
                if valid_data_input== True:
                    break
                else:
                    print("Sorry, I do not have access to your input. Please enter "
                          "'yes' or 'no'.")
            if show_more.lower() == 'yes':
                h += 5
                t += 5
                print(df[df.columns[0:5]].iloc[h:t])
            elif show_more.lower() == 'no':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_five_line_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n~')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

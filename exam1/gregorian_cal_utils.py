def is_leap_year(year: int) -> bool:
    """
    Given a year, this function returns a boolean indicating whether or not it is a leap year.

    :param year: an integer indicating a year.
    :return: A boolean indicating whether or not the year parameter is a leap year.
    """
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return False
    else:
        return True


    #if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        #return True

    #The year must be evenly divisible by 4;
    # * If the year can also be evenly divided by 100, it is not a leap year; unless
    #     * The year is also evenly divisible by 400. Then it is a leap year.
    #pass  # implement me

from datetime import datetime

import QuantLib as ql


def create_brazilian_business_days_schedule(start_date, end_date):
    """
    Find business days using B3 holidays calendar
    """

    # Create the schedule
    schedule = ql.MakeSchedule(
        effectiveDate=start_date,
        terminationDate=end_date,
        tenor=ql.Period(ql.Daily),
        calendar=ql.Brazil(ql.Brazil.Exchange),
        convention=ql.Following,
        rule=ql.DateGeneration.Forward,
    )

    # Return the schedule
    return [datetime(date.year(), date.month(), date.dayOfMonth()) for date in schedule]

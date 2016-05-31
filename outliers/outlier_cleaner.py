#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    for x in range(len(predictions)):
        for y in range(len(cleaned_data) + 1):
            if (y == len(cleaned_data)) or (cleaned_data[y][2] < abs(predictions[x][0] - net_worths[x][0])):
                cleaned_data.insert(y, (ages[x][0], net_worths[x][0], abs(predictions[x][0] - net_worths[x][0])))
                break

    cleaned_data = cleaned_data[(len(predictions) / 10) + 1:]

    return cleaned_data

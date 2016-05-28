#!/usr/bin/python

import operator


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).

        error = actual - predicted
    """

    cleaned_data = []

    for p, age, netw in zip(predictions, ages, net_worths):
        error = p[0] - netw[0]
        cleaned_data.append((age[0], netw[0], error))

    # print cleaned_data
    cleaned_data.sort(key=operator.itemgetter(2))

    return cleaned_data[:81]

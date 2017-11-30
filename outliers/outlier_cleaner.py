#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """
    print "\nages size: ", len(ages)
    print "net_worths size: ", len(net_worths)
    print "predictions size: ", len(predictions)

    size = len(ages)
    cleaned_data = []
    a = []
    b = []
    c = []
    ### your code goes here
    for i in range(size):
        a.append(ages[i]) # age
        b.append(net_worths[i]) # net worth
        c.append(net_worths[i] - predictions[i]) # error
        t = [a[i], b[i], c[i]]
        cleaned_data.append(t)
    cleaned_data = sorted(cleaned_data)
    get_ten_percent = len(cleaned_data) - (len(cleaned_data) * .10)
    print "length - ten percent: ", int(get_ten_percent)
    return cleaned_data[:int(get_ten_percent)]

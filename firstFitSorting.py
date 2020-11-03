"""
    Sorting the numbers in the given array M into N different bins where each bin is of the type integer array.
    Constraint: The sum of elements in each bin should be less than or equal to given maximum element
    Solution: First fit sorting
"""


def first_fit_sorting(array, maximum):
    """
    function sorts the elements into N different bins
    :param array: array to be sorted
    :param maximum: maximum element
    :return: array of N bins
    """
    sum_ = 0    # to calculate the sum of numbers in the bin
    total_bins = list()     # array containing the bins
    temp = list()
    for item in array:
        """
        check if the sum of the numbers in the bin is less than or equal to the maximum element,
        if yes: add the element to the bin, update the sum
        if no: reinitialize sum to 0, append the number(s) in the bin (temp) to the array of bins (total_bins)
        """
        if sum_ + item <= maximum:  # check if the sum is less than or equal to the maximum element
            sum_ += item
            temp.append(item)
        else:
            sum_ = 0
            total_bins.append(temp)
            temp = []   # reinitialize the temp to empty list
            if sum_ + item <= maximum:
                sum_ += item
                temp.append(item)
            else:
                """
                if the element in the given array itself is larger than the maximum element,
                say the maximum element is 20 but the current element in the array is 26,
                just append the element to the bin (temp) and later append this bin to the array of bins (total_bins)
                """
                temp.append(item)
                total_bins.append(temp)
                temp = []   # reinitialize to empty list
    # for the elements which are still in the temp list, append them to the bin list after exiting the loop
    total_bins.append(temp)
    return total_bins


if __name__ == '__main__':
    M = [2, 7, 11, 15, 4, 7, 1, 20, 6]
    M_max = 20
    print(f"output = {first_fit_sorting(M, M_max)}")

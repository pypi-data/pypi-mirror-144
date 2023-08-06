"""
Component functions.

Usage:
 ./utils/base.py

Author:
 Peter Rigali - 2022-03-10
"""
from typing import Union
from pyjr.utils.tools import _unique_values, _search_dic_values, _round_to, _to_metatype


# Internal Math Functions
def _max(data: Union[list, tuple]) -> float:
    """
    Find the max value of a list.

    :param data: Input data.
    :type data: list or tuple.
    :return: Maximum value.
    rtype: float.
    :note: *None*
    """
    if data.__len__() > 1:
        return max(data)
    return data[0]


def _min(data: Union[list, tuple]):
    """
    Find the min value of a list.

    :param data: Input data.
    :type data: list or tuple.
    :return: Minimum value.
    :rtype: float.
    :note: *None*
    """
    if data.__len__() > 1:
        return min(data)
    return data[0]


def _range(data: Union[list, tuple]) -> float:
    """
    Find the max to min range value of a list.

    :param data: Input data.
    :type data: list or tuple.
    :return: Range value.
    :rtype: float.
    :note: *None*
    """
    if data.__len__() > 1:
        return _max(data=data) - _min(data=data)
    return 0.0


def _mean(data: Union[list, tuple]) -> float:
    """
    Find the mean value of a list.

    :param data: Input data.
    :type data: list or tuple.
    :return: Mean value.
    :rtype: float.
    :note: *None*
    """
    return sum(data) / data.__len__()


def _variance(data: Union[list, tuple], ddof: int = 1) -> float:
    """
    Find the variance value of a list.

    :param data: Input data.
    :type data: list or tuple.
    :param ddof: Desired Degrees of Freedom.
    :type ddof: int
    :return: Variance value.
    :rtype: float.
    :note: *None*
    """
    mu = _mean(data=data)
    return sum(((x - mu) ** 2 for x in data)) / (data.__len__() - ddof)


def _std(data: Union[list, tuple], ddof: int = 1) -> float:
    """
    Find the Standard Deviation value of a list.

    :param data: Input data.
    :type data: list or tuple.
    :param ddof: Desired Degrees of Freedom.
    :type ddof: int
    :return: Standard Deviation value.
    :rtype: float.
    :note: *None*
    """
    return _variance(data=data, ddof=ddof) ** .5


def _sum(data: Union[list, tuple]) -> float:
    """
    Find the sum value of a list.

    :param data: Input data.
    :type data: list or tuple.
    :return: Sum value.
    rtype: float.
    :note: *None*
    """
    if data.__len__() > 1:
        return sum(data)
    return data[0]


def _median(data: Union[list, tuple]) -> float:
    """
    Find the median value of a list.

    :param data: Input data.
    :type data: list or tuple.
    :return: Mean value.
    :rtype: float.
    :note: *None*
    """
    sorted_lst, lst_len = sorted(data), data.__len__()
    index = (lst_len - 1) // 2
    if lst_len % 2:
        return sorted_lst[index]
    else:
        return _mean(data=[sorted_lst[index]] + [sorted_lst[index + 1]])


def _mode(data: Union[list, tuple]) -> float:
    """
    Find the mode value of a list.

    :param data: Input data.
    :type data: list or tuple.
    :return: Mode value.
    :rtype: float.
    :note: *None*
    """
    count_dic = _unique_values(data=data, count=True)
    count_dic_values = _to_metatype(data=count_dic.values())
    dic_max = _max(count_dic_values)
    lst = []
    for i in count_dic_values:
        val = _search_dic_values(dic=count_dic, item=dic_max)
        lst.append((val, i))
        # del count_dic[val]
        count_dic_values = _to_metatype(data=count_dic.values())

    first_val, second_val = lst[0][0], lst[0][1]
    equal_lst = [i[0] for i in lst if second_val == i[1]]
    if equal_lst.__len__() == 1:
        return first_val
    elif equal_lst.__len__() % 2 == 0:
        return _mean(data=equal_lst)
    else:
        return _median(data=equal_lst)


def _skew(data: Union[list, tuple]) -> float:
    """
    Find the skew value of a list.

    :param data: Input data.
    :type data: list or tuple.
    :return: Skew value.
    :rtype: float.
    :note: *None*
    """
    mu, stdn, length = _mean(data=data), _std(data=data, ddof=1) ** 3, data.__len__()
    if stdn == 0:
        stdn = mu / 2.0
    return (((_sum(data=[i - mu for i in data]) ** 3) / length) / stdn) * ((length * (length - 1)) ** .5) / (length - 2)


def _kurtosis(data: Union[list, tuple]) -> float:
    """
    Find the kurtosis value of a list.

    :param data: Input data.
    :type data: list or tuple.
    :return: Kurtosis value.
    :rtype: float.
    :note: *None*
    """
    mu, stdn = _mean(data=data), _std(data=data, ddof=1) ** 4
    if stdn == 0:
        stdn = mu / 2
    return (((_sum(data=[i - mu for i in data])**4) / data.__len__()) / stdn) - 3


def _percentile(data: Union[list, tuple], q: float) -> float:
    """
    Find the percentile value of a list.

    :param data: Input data.
    :type data: list or tuple.
    :param q: Percentile percent.
    :type q: float.
    :return: Percentile value.
    rtype: float.
    :note: *None*
    """
    data = _round_to(data=[item * 1000.0 for item in data], val=1)
    ind = _round_to(data=data.__len__() * q, val=1)
    data.sort()
    for item in data:
        if item >= data[ind]:
            return item / 1000.0


def _percentiles(data: Union[list, tuple], q_lst: Union[list, tuple] = (0.159, 0.841)):
    """
    Calculate various percentiles for a list.

    :param data: Input data.
    :type data: list or tuple.
    :param q_lst: Desired percentile percents.
    :type q_lst: List of floats.
    :return: A group of stats.
    :note: *None*
    """
    return (_percentile(data=data, q=q) for q in q_lst)

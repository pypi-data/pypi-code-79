from mobster.likelihood_calculation import *
import numpy as np


def ICL(data, params, tail):
    bic = BIC(data, params, tail)
    entropy = compute_entropy(params, tail)
    return bic + entropy

def BIC(data, params, tail):
    lk = likelihood(data, params, tail)
    n_params = calculate_number_of_params(params)
    n = number_of_samples(data)
    return np.log(n) * n_params - 2 * lk


def AIC(data, params, tail):
    lk = likelihood(data, params, tail)
    n_params = calculate_number_of_params(params)
    return 2 * n_params - 2 * lk


def likelihood(data, params, tail):
    lk = compute_likelihood_from_params(data, params, tail)
    return lk


def calculate_number_of_params(params):

    res = 0
    for i in params:
        if type(params[i]) is dict:
            next
        else:
            res += np.prod(params[i].shape)
    return res


def number_of_samples(data):

    res = 0
    for k in data:
        res += np.prod(data[k].shape)
    return res
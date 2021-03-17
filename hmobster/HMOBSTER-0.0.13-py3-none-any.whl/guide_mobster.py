import pyro as pyro
import numpy as np
from pyro.infer import MCMC, NUTS, Predictive, HMC, config_enumerate
from pyro.infer.autoguide import AutoDelta, init_to_sample
import pyro.distributions as dist
import pyro.poutine as poutine
import torch
from torch.distributions import constraints
import mobster.utils_mobster as mut


@config_enumerate
def guide(data, K=1, tail=1, purity=0.96, clonal_beta_var=1., alpha_prior_concentration = 5, alpha_prior_rate = 10, number_of_trials_clonal_mean=100.,
          number_of_trials_clonal=900., number_of_trials_k=300., prior_lims_clonal=[1., 10000.],
          prior_lims_k=[1., 10000.]):
    """
    Parameters
    ----------
    param1 :
    The first parameter.
    param2 :
    The second parameter.

    """
    karyos = list(data.keys())

    # Here we calculate the theoretical number of clonal clusters
    theoretical_num_clones = [mut.theo_clonal_list[kr] for kr in karyos]

    # Calculate the theoretical clonal means, wihch can be analytically defined for simple karyotypes, and then multiply them by the ploidy
    theoretical_clonal_means = [mut.theo_clonal_means_list[kr] * purity for kr in karyos]

    counts_clones = dict()
    for i in theoretical_num_clones:
        counts_clones[i] = counts_clones.get(i, 0) + 1

    index_2 = [i for i, j in enumerate(theoretical_num_clones) if j == 2]
    index_1 = [i for i, j in enumerate(theoretical_num_clones) if j == 1]

    a_prior = pyro.param("tail_mean", torch.tensor(1.5), constraint=constraints.interval(0.5, 5))
    sd_prior = pyro.param("tail_sd",dist.Gamma(concentration=alpha_prior_concentration, rate=alpha_prior_rate).mean, constraint=constraints.positive)

    alpha_prior_sd = pyro.sample('sd_tail', dist.Delta(sd_prior))


    alpha_prior = pyro.sample('u', dist.Delta(a_prior))

    idx1 = 0
    idx2 = 0

    if tail == 1:
        weights_tail = pyro.param("param_tail_weights", 1 / torch.ones([len(karyos), 2]), constraint=constraints.simplex)

    if 2 in theoretical_num_clones:
        weights_param_2 = pyro.param("param_weights_2", (1 / (K + 2)) * torch.ones([len(index_2), K + 2]),
                                     constraint=constraints.simplex)
    if 1 in theoretical_num_clones:
        weights_param_1 = pyro.param("param_weights_1", (1 / (K + 1)) * torch.ones([len(index_1), K + 1]),
                                     constraint=constraints.simplex)

    for kr in pyro.plate("kr", len(karyos)):

        pyro.sample('alpha_{}'.format(kr), dist.LogNormal(torch.log(alpha_prior), alpha_prior_sd))

        if theoretical_num_clones[kr] == 2:

            pyro.sample('weights_{}'.format(kr), dist.Delta(weights_param_2[idx2]).to_event(1))

            # Mean parameter when the number of clonal picks is 2
            a_2_theo = torch.cat([theoretical_clonal_means[i] for i in index_2]).reshape([2, counts_clones[2]])
            max_lim_2 = torch.tensor([torch.min(theoretical_clonal_means[i]) for i in index_2])
            a_2_k = dist.Uniform(0.1, max_lim_2 - (0.3 * max_lim_2)).sample([K])

            # Number of trials parameter when the number of clonal picks is 2
            b_2_theo = torch.ones([2, len(index_2)]) * number_of_trials_clonal_mean
            b_2_k = torch.ones([K, len(index_2)]) * number_of_trials_k

            a21 = pyro.param('a_2',
                             torch.cat((a_2_theo, a_2_k)).reshape([2 + K, len(index_2)]),
                             constraint=constraints.unit_interval)
            a22 = pyro.param('b_2',
                             torch.cat((b_2_theo, b_2_k)).reshape([2 + K, len(index_2)]),
                             constraint=constraints.positive)

            with pyro.plate("clones_{}".format(kr), 2 + K):
                pyro.sample('beta_clone_mean_{}'.format(kr), dist.Delta(a21[:, idx2]))
                pyro.sample('beta_clone_n_samples_{}'.format(kr), dist.Delta(a22[:, idx2]))
            idx2 += 1

        else:
            pyro.sample('weights_{}'.format(kr), dist.Delta(weights_param_1[idx1]).to_event(1))

            # Mean parameter when the number of clonal picks is 1
            a_1_theo = torch.tensor([theoretical_clonal_means[i] for i in index_1]).reshape([1, counts_clones[1]])
            max_lim_1 = torch.tensor([np.min(theoretical_clonal_means[i]) for i in index_1])
            a_1_k = dist.Uniform(0.1, max_lim_1 - (0.3 * max_lim_1)).sample([K])

            # Number of trials parameter when the number of clonal picks is 1
            b_1_theo = torch.ones([1, len(index_1)]) * number_of_trials_clonal_mean
            b_1_k = torch.ones([K, len(index_1)]) * number_of_trials_k

            a11 = pyro.param('a_1',
                             torch.cat((a_1_theo, a_1_k)).reshape([1 + K, len(index_1)]),
                             constraint=constraints.unit_interval)
            a12 = pyro.param('b_1',
                             torch.cat((b_1_theo, b_1_k)).reshape([1 + K, len(index_1)]),
                             constraint=constraints.positive)

            with pyro.plate("clones_{}".format(kr), 1 + K):
                pyro.sample('beta_clone_mean_{}'.format(kr), dist.Delta(a11[:, idx1]))
                pyro.sample('beta_clone_n_samples_{}'.format(kr), dist.Delta(a12[:, idx1]))
            idx1 += 1

        if tail == 1:
            # K = K + tail
            pyro.sample('weights_tail_{}'.format(kr), dist.Delta(weights_tail[kr]).to_event(1))


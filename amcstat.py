# Some statistical functions used by amcpy package
import numpy as np

def likelihood(signal,alphabet,sigma):
    "Likelihood Function Calculate the log likelihood of signal belonging to a\
            set of bivariate normal distributions with specified\
            alphabet(means). and sigma(standard deviation)."
    for iSignal in signal.size:
        for iAlphabet in alphabet.size:
            iLikelihood(iAlphabet) = np.exp(-ny.power(np.abs(signal[iSignal]\
                    -alphabet[iAlphabet]),2)/2/np.power(sigma,2))/(2*pi*\
                    np.power(sigma,2))
        likelihood(iSignal) = np.mean(iLikelihood)
    
    likelihood = np.sum(np.log(likelihood))

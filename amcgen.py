import numpy as np

def genmodsig(modulationType,sampleNo):
    "GENMODSIG   Generate i.i.d modulated signal samples with unit power"
    
    # Create basic mapping of signal symbols
    if modulationType == '2pam':
        symbolMap = np.array([1, -1])
    elif modulationType == '4pam':
        symbolMap = np.array([-3, -1, 1, 3])
    elif modulationType == '8pam':
        symbolMap = np.array([-7, -5, -3, -1, 1, 3, 5, 7])
    elif modulationType == '2psk':
        symbolMap = np.array([1j, -1j])
    elif modulationType == '4psk':
        symbolMap = np.array([1, 1j, -1, -1j])
    elif modulationType == '8psk':
        symbolMap = np.array([np.sqrt(2), 1+1j, np.sqrt(2)*1j, -1+1j,\
            -np.sqrt(2), -1-1j, -np.sqrt(2)*1j, 1-1j])
    elif modulationType == '4qam':
        symbolMap = np.array([1+j, -1+j, -1-j, 1-j])
    elif modulationType == '16qam':
        symbolMap = np.array([3+3j, 3+j, 3-j, 3-3j, 1+3j, 1+j, 1-j, 1-3j,\
                -1+3j, -1+j, -1-j, -1-3j, -3+3j, -3+j, -3-j, -3-3j])
    elif modulationType == '64pam':
        symbolMap = np.array([1+1j, 3+1j, 1+3j, 3+3j, 7+1j, 5+1j, 7+3j,\
                5+3j, 1+7j, 3+7j, 1+5j, 3+5j, 7+7j, 5+7j, 7+5j, 5+5j, 1-1j,\
                1-3j, 3-1j, 3-3j, 1-7j, 1-5j, 3-7j, 3-5j, 7-1j, 7-3j, 5-1j,\
                5-3j, 7-7j, 7-5j, 5-7j, 5-5j, -1+1j, -1+3j, -3+1j, -3+3j,\
                -1+7j, -1+5j, -3+7j, -3+5j, -7+1j, -7+3j, -5+1j, -5+3j,\
                -7+7j, -7+5j, -5+7j, -5+5j, -1-1j, -3-1j, -1-3j, -3-3j,\
                -7-1j, -5-1j, -7-3j, -5-3j, -1-7j, -3-7j, -1-5j, -3-5j,\
                -7-7j, -5-7j, -7-5j, -5-5j])

    # Calculate signal power
    symbolPower = np.mean(np.square(np.absolute(symbolMap)))
    
    # Normalise symbol
    symbolMap = np.divide(symbolMap,np.sqrt(symbolPower))
    
    # Create uniform random index of signal samples
    symbol = np.floor(np.random.rand(sampleNo)*symbolMap.size)
    symbol = symbol.astype(int)

    #fix(rand(sampleNo,1)*size(symbolMap,1)) + 1, 
    # Map the signal samples to symbols
    sigOut = symbolMap[symbol]

    return sigOut

def awgn(sigIn,snr):
    "AMCAWGN   Adds AWGN noise to signals according to Signal-to-noise ratio."

    # Determine the dimension of input signal data
    N = sigIn.size

    # Generate unscaled AWGN noise components
    noise = np.random.randn(N) + np.random.randn(N)*1j

    # Calculate signal power
    sigPower = np.mean(np.square(np.absolute(sigIn)))
    
    # Calculate noise power
    noisePower = np.mean(np.square(np.absolute(noise)))
    
    # Calculate scaling factor for noise components according to SNR
    sigNoise = np.sqrt(sigPower/noisePower)*(np.power(10,-snr/20))

    # Map the noise power scaling factor
    sigOut = sigIn + noise*sigNoise

    return sigOut

def sig16qam(length):

	# Import numpy and other libraries
	import numpy
	
	# Set modulation constellation symbol mapping
	map16 = numpy.array([1+1j, 1-1j, -1+1j, -1-1j, 3+1j, 3-1j, -3+1j,\
			-3-1j, 3+3j, 3-3j, -3+3j, -3-3j, 1+3j, 1-3j, -1+3j, -1-3j])
	
	# Geneate uniform random index for symbol mapping
	mapIndex = numpy.random.randint(16,size=(length,1))
	
	# Mapping the signal samples to the symbols with mapping index
	signal = map16[mapIndex]

	# Return generated signal samples
	return signal

def awgn(sigIn,snr):
	
	# Import numpy and other libraries
	import numpy

	# Measure signal length
	N = len(sigIn)

	# Generate unscaled white Gaussian noise
	noise = numpy.zeros((N,1),dtype=complex)
	noise.real = numpy.random.randn(N,1)
	noise.imag = numpy.random.randn(N,1)

	# Measure power of the unscaled white Gaussian noise
	noisePower = sum(numpy.abs(noise)**2)
	
	# Measure power of input signal
	sigPower = sum(numpy.abs(sigIn)**2)

	# Scale white Gaussian noise and add to the input signal
	sigOut = sigIn + noise*numpy.sqrt(sigPower/noisePower)*(10**(-snr/20))

	return sigOut

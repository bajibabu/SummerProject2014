from scipy.io.wavfile import read
import matplotlib.pyplot as plt

def run():
# read audio samples
	print 'hello'
	rate,input_data = read("demo1.wav")
	audio = input_data[:,1]
# plot the first 1024 samples
	plt.plot(audio[0:1024])
# label the axes
	plt.ylabel("Amplitude")
	plt.xlabel("Time")
# set the title  
	plt.title("Sample Wav")
# display the plot
	plt.show()

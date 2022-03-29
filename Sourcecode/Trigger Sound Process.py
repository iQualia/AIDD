

#Initiate Microphone
#Wait for trigger
#Record for 1 second after each trigger
#Post process recorded audio
    #-1st milestone (convert into time domain picture)
    #-2nd milestone convert into frequency domain using fourier transform
    #-3rd milestone
#final product - MEL spectogram of the recorded frame
#test
import pyaudio
import time
import librosa
import librosa.display
import matplotlib.pyplot as plt
import skimage.io

def scale_minmax(X, min=0.0, max=1.0):
    X_std = (X - X.min()) / (X.max() - X.min())
    X_scaled = X_std * (max - min) + min
    return X_scaled
#Initiating pyaudio
#-Assign variables for the details needed
PATH =  r'D:\Personal\PROJECT\Qualia\DEFECT DETECTION\DATASET\TRAINING DATASET'
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100 #mostly used for high quality Audio- 441khz = 16bits * 44100 = 1 411 200 bits / seconds
RECORD_SECONDS = 6

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK)

# Listen to MIC for 5 seconds
import numpy as np
def rec(seconds,samplerate): # record and convert data to array for (x) seconds

    npsound = []#Initiate empty list to collect 16-bit samples
    samplerate = RATE

    time_end = time.time()+seconds
    while time.time()<time_end:
        sound_data = stream.read(samplerate) #Data collected in int16
        cvtd_data = np.frombuffer(sound_data, dtype=np.int16) #Convert data collected and stored as numpy
        npsound.append(cvtd_data) #append all the data in the time into the list

    npsound_concat = np.concatenate(npsound) # once the audio is fully recorded, concatenate all data into one numpy
    # files

    return npsound_concat

def melspectrogram(X,samplerate):#input sample points
    S = librosa.feature.melspectrogram(X.astype(np.float),samplerate)
    S_dB = librosa.power_to_db(S, ref=np.max)

    return S_dB



#Run loop, to only record after the tapping is triggered

i = 0

while True:


    if i%2 == 0:
        # print('saving{}'.format(i))
        samplepoints = rec(1,RATE)
       # print(samplepoints)
        #print(len(samplepoints))
        S_dB = melspectrogram(samplepoints,RATE)
        #print(S_dB)
        img = scale_minmax(S_dB, 0, 255).astype(np.uint8)
        #img = librosa.display.specshow(S_dB, x_axis='time', y_axis='mel', sr=sr, fmax=8000, ax=ax)

        img = np.flip(S_dB, axis=0)  # put low frequencies at the bottom in image
        skimage.io.imsave(r'D:\Personal\PROJECT\Qualia\DEFECT DETECTION\DATASET\TRAINING DATASET\graph{}.png'.format(i),img)

        i = i + 1
        print(i)
        time.sleep(5)


    elif i > 20:
        break

    else:
        i = i + 1


# def troubleshoot():#function to check value of all graphs /TODO Plot multiple graph at each domain
#     rec(1,44100)
#     fig, ax = plt.subplots(1, figsize=(15, 7))
#     ax.set_title('Trouble shoot to see audio wave')
#     ax.set_xlabel('samples')
#     ax.set_ylabel('Signal value')
#     ax.set_ylim(-5000, 5000)  # set the vertical graph max and min value
#     ax.set_xlim(0, len(npsound_concat))  # set the horizontal graph starting and end point - in this case the number of
#     # seconds the audio was recorded
#     x = np.arange(0, 2 * secs * RATE, 2)  # arrange the value at X axis in the steps of two (starting from zero
#     # ending at
#     print(x)
#     print(x.shape)
#     # 5 seconds
#     line, = ax.plot(x, npsound_concat, '-', lw=2)
#     # line.set_ydata(npsound_concat)
#     plt.show(block=False)
#
#     librosa.display.specshow(S_dB, x_axis='time', y_axis='mel', sr=sr, fmax=8000, ax=ax)\



























    #Trouble shoot - plot graph to see
#####ARCHIVE########
# S = librosa.feature.melspectrogram(npsound_concat.astype(np.float),RATE)#convert concat sound to float // using astype
# print(S)
# fig, ax = plt.subplots()
# S_dB = librosa.power_to_db(S, ref=np.max)
# img = librosa.display.specshow(S_dB, x_axis='time',
#                          y_axis='mel', sr=RATE,
#                          fmax=8000, ax=ax)
# fig.colorbar(img, ax=ax, format='%+2.0f dB')
# ax.set(title='Mel-frequency spectrogram')

# import matplotlib.pyplot as plt
#
# fig, ax = plt.subplots(1, figsize=(15, 7))
# ax.set_title('Trouble shoot to see audio wave')
# ax.set_xlabel('samples')
# ax.set_ylabel('Signal value')
# ax.set_ylim(-5000, 5000)  # set the vertical graph max and min value
# ax.set_xlim(0, len(npsound_concat))  # set the horizontal graph starting and end point - in this case the number of
# # seconds the audio was recorded
# x = np.arange(0, 2 * secs * RATE, 2)  # arrange the value at X axis in the steps of two (starting from zero
# # ending at
# print(x)
# print(x.shape)
# # 5 seconds
# line, = ax.plot(x, npsound_concat, '-', lw=2)
# # line.set_ydata(npsound_concat)
# plt.show(block=False)
#
# # Apply Fast fourier transform (FFT) to change to frequency domain
#
# from numpy.fft import fft, ifft
#
# X = fft(npsound_concat)  # FFT return complex ndarray (padded if the input is shorter than duration set in the
# # arguments, cropped if the input is longer, default return original length)
# print(X.shape)
# samplecount = len(X)
# print(samplecount)
# print(X[1])
# values = np.arange(samplecount)
# print(values)
# T = samplecount / RATE
# freq = values / T
# print(freq)
# print(len(freq))
# plt.stem(freq, np.abs(X), 'b', \
#          markerfmt=" ", basefmt="-b")
# plt.xlabel('Freq (Hz)')
# plt.ylabel('FFT Amplitude |X(freq)|')
# plt.xlim(0, samplecount)
#
# # while True:
# # data = stream.read(CHUNKSIZE)
# # numpydata = np.frombuffer(data, dtype=np.int16)  # Array just represent
# #  line.set_ydata(numpydata)  # if we were to use real time data - will need to use set data y - to keep on
# # updating and changing y without changing the frame of the graph
#
# test = np.arange(3)
# TIME = 3 / 2
# f = test / TIME
# print(test)
# print(TIME)
# print(f)
# print(len(f))
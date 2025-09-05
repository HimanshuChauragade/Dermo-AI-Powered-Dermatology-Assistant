from tkinter import filedialog
#import tensorflow.keras
import tensorflow
from tensorflow import keras
from tkinter import *
import numpy as np
import webbrowser
import cv2

root = Tk()

# Width X Height
root.geometry("400x500")
root.minsize(644, 333)
root.maxsize(1000, 800)

# Window Title
root.title("Dermo")


def openacne():
    webbrowser.open("https://en.wikipedia.org/wiki/Acne")

def openDermatophytosis():
    webbrowser.open("https://en.wikipedia.org/wiki/Dermatophytosis")

normalskin = Label(root, text="Skin Status: Normal", font="lucida 19 bold")
acneskin = Label(root, text="Skin Status: Acne", font="lucida 19 bold")
acnebutton = Button(root, fg="black", text="Load More about Acne", font="lucida 19 bold", command=openacne)
Dermatophytosisskin = Label(root, text="Skin Status: Dermatophytosis", font="lucida 19 bold")
Dermatophytosisbutton = Button(root, fg="black", text="Load More about Dermatophytosis", font="lucida 19 bold", command=openDermatophytosis)

class Classifier:

    def __init__(self, modelPath, labelsPath=None):
        self.model_path = modelPath
        # Disable scientific notation for clarity
        np.set_printoptions(suppress=True)
        # Load the model
        self.model = tensorflow.keras.models.load_model(self.model_path)

        # Create the array of the right shape to feed into the keras model
        # The 'length' or number of images you can put into the array is
        # determined by the first position in the shape tuple, in this case 1.
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.labels_path = labelsPath
        if self.labels_path:
            label_file = open(self.labels_path, "r")
            self.list_labels = []
            for line in label_file:
                stripped_line = line.strip()
                self.list_labels.append(stripped_line)
            label_file.close()
        else:
            print("No Labels Found")

    def getPrediction(self, img, draw= True, pos=(50, 50), scale=2, color = (0,255,0)):
        # resize the image to a 224x224 with the same strategy as in TM2:
        imgS = cv2.resize(img, (224, 224))
        # turn the image into a numpy array
        image_array = np.asarray(imgS)
        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

        # Load the image into the array
        self.data[0] = normalized_image_array

        # run the inference
        prediction = self.model.predict(self.data)
        indexVal = np.argmax(prediction)
        print(indexVal) #if indexVal == 0: acne detected elif indexVal == 1: Normal_Skin
        
        if indexVal == 0:  #Normal_skin
            acnebutton.pack_forget()
            acneskin.pack_forget()
            Dermatophytosisskin.pack_forget()
            Dermatophytosisbutton.pack_forget()
            normalskin.pack(side=TOP, padx=20, pady=20)

        
        if indexVal == 1: #acne
            Dermatophytosisskin.pack_forget()
            Dermatophytosisbutton.pack_forget()
            normalskin.pack_forget()
            acneskin.pack(side=TOP, padx=20, pady=20)
            acnebutton.pack(side=TOP, padx=10)

        if indexVal == 2:#Dermatophytosis
            acnebutton.pack_forget()
            acneskin.pack_forget()
            normalskin.pack_forget()
            Dermatophytosisskin.pack(side=TOP, padx=20, pady=20)
            Dermatophytosisbutton.pack(side=TOP, padx=10)

        if draw and self.labels_path:
            cv2.putText(img, str(self.list_labels[indexVal]),
                        pos, cv2.FONT_HERSHEY_COMPLEX, scale, color, 2)

        return list(prediction[0]), indexVal


    #ImageName = int(input("Enter Image Name: "))
    #baseLocation = "Dataset/"
    #ImageFormat = ".jpg"
    # CompleteImageName = r"C:\Users\Himanshu\PycharmProjects\Acne Detector\Dataset\0.jpg"
    #CompleteImageName = (
    #    f"{baseLocation}"
    #    f"{ImageName}"
    #    f"{ImageFormat}"
    #    )



while True:
    def openFile():
        root.file = filedialog.askopenfilename(title="Select A File",
                                               filetypes=[("Images", "*.svg"),
                                                          ("Images", "*.jpg"),
                                                          ("Images", "*.jpeg"),
                                                          ("Images", "*.png")])
        print("Selected File:", root.file)
        fl = root.file
        # cap = cv2.VideoCapture(1)
        img = cv2.imread(fl)
        myClassifier = Classifier('MyModel/keras_model.h5', 'MyModel/labels.txt')
        # _, img = cap.read()
        predictions = myClassifier.getPrediction(img)
        cv2.imshow("Results", img)
        key = cv2.waitKey(1) & 0xFF


    # do a bit of cleanup
    cv2.destroyAllWindows()

    Label(root, text="Note: For External Detection Only", font="lucida 19 bold").pack(side=TOP, padx=20, pady=10)
    Label(root, text="Enter File Location: ", font="lucida 19 bold").pack(side=TOP, padx=20, pady=20)
    Button(root, fg="black", text="Browse...", font="lucida 19 bold", command=openFile).pack(side=TOP, padx=10)

    root.mainloop()
from Prediction import predict
import numpy as np
import cv2
import sys

Theta1 = np.loadtxt('Theta1.txt')
Theta2 = np.loadtxt('Theta2.txt')

num_set = {0: "Zero", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}

def run(threshold = 100, loss_rate = 22, path = fr"uploads\({sys.argv[1]}).jpg" if len(sys.argv) > 1 else print("Cannot find uploads"), num = 0):
    try:
        image = cv2.resize(cv2.bitwise_not(cv2.imread(path, cv2.IMREAD_GRAYSCALE)), (28,28))
    except :
        return

    image = np.where(image > threshold, 255, 0)

    x = np.asarray(image)
    image_vector = np.zeros((1, 784))

    k = 0
    for i in range(28):
        for j in range(28):

            pixel = 255 if x[i][j] > loss_rate else 0

            image_vector[0][k] = pixel
            k += 1

        #     print("{0: <3}".format(f"{pixel}"), end=" ")
        # print("\n")

    # Calling function for prediction
    pred = predict(Theta1, Theta2, image_vector / 255)

    
    # if __name__ == "__main__":
    # return pred[0] == num
    # else:
    print(str(pred[0]))

run()
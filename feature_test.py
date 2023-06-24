# read a npy file and print the array
import numpy as np
import torch
import os

PATH = "./data/clip/ViT-B_32/"
TEST_LOG = "test.log"
WRITE_LOG = True

def isVaildFeature(feature):
    try:
        data = np.load(os.path.join(PATH, feature))
        if isinstance(data, np.ndarray) and data.size > 0:
            return True
    except Exception:
        return False
    return False

def checkAll():
    # check all the feature in the folder is valid
    Total, Valid, Invalid = 0, 0, 0
    invalids = []
    for feature in os.listdir(PATH):
        print(feature, end=" ")
        if WRITE_LOG:
            with open(TEST_LOG, "a") as f:
                f.write(feature + " ")
        if isVaildFeature(feature):
            Valid += 1
            print(",Valid")
            with open(TEST_LOG, "a") as f:
                f.write(",Valid\n")
        else:
            Invalid += 1
            print(",Invalid")
            if WRITE_LOG:
                with open(TEST_LOG, "a") as f:
                    f.write(",Invalid\n")
            invalids.append(feature)
        Total += 1

    print("Total: {}, Valid: {}, Invalid: {}".format(Total, Valid, Invalid))
    print("Invalids: ", invalids)
    if WRITE_LOG:
        with open(TEST_LOG, "a") as f:
            f.write("Total: {}, Valid: {}, Invalid: {}".format(Total, Valid, Invalid))
            f.write("Invalids: {}".format(invalids))


if __name__ == "__main__":
    checkAll()
    
    # feature = "v__NpsOCOnQS6c_clip.npy"
    # print(isVaildFeature(feature))
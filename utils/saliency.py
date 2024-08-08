## Copyright for this code belongs to University of Southern California.
import tensorflow as tf
import numpy as np

def Normalize(x):
    return (x - np.min(x)) / (np.max(x) - np.min(x))

def saliencyMap(model, X, normalize=False):
    saliencyMaps = []
    
    for idx, i in enumerate(X):
        img = i.reshape((1, *X[0].shape))
        img = img.reshape((*img.shape, 1))
        #print(np.shape(i), *X[0].shape, np.shape(img))
        img = tf.Variable(img, dtype=float)
        
        with tf.GradientTape() as tape:
            pred  = model(img, training=False)
            #print('prediction: ', pred)
            classSorted = np.argsort(pred.numpy().flatten())[::-1]
            #print('classSorted: ', classSorted)
            loss = pred[0][classSorted[0]]
            #print('loss: ', loss)
        grad = tape.gradient(loss, img)
        gradAbs = tf.math.abs(grad)
        gradMax = np.max(gradAbs, axis=4)[0]
        #print('grad shape: ', np.shape(grad))
        if normalize:
            saliencyMaps.append(Normalize(gradMax))
        else:
            saliencyMaps.append(gradMax)
    
    return np.asarray(saliencyMaps)

def postProcess(smap, brains):
    smap2 = []
    for idx, brain in enumerate(brains):
        # remove saliency outside the brain
        brainMask  = np.where(brain>1, 1, 0)
        tempSal = smap[idx]*brainMask
        
        # convert to saliency probability
        tempSal=tempSal/np.sum(tempSal)
        
        smap2.append(tempSal)
    
    return np.asarray(smap2)

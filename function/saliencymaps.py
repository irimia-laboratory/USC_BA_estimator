
import numpy as np
import tensorflow as tf

def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))
    
def smap(model, X_test): 
    saliency_map_list = []
    for index in range(len(X_test)):
        images = X_test[index].reshape((1, *X_test[0].shape)) 
        images = tf.Variable(images, dtype=float)
    
        with tf.GradientTape() as tape:
            pred = model(images, training=False)
            class_idxs_sorted = np.argsort(pred.numpy().flatten())[::-1]
            loss = pred[0][class_idxs_sorted[0]]
        grads = tape.gradient(loss, images)
        dgrad_abs = tf.math.abs(grads)
        dgrad_max_ = np.max(dgrad_abs, axis=4)[0]
    
      # cut regions
        buf = dgrad_max_
        buf_test = X_test[index].reshape((82,86,100))
        buf = np.where(np.all(np.stack([buf>0, buf_test<=0]), axis=0), 0, buf)
        buf = NormalizeData(buf)
        saliency_map_list.append(buf)
    saliency_map_list = np.asarray(saliency_map_list)
 
    return saliency_map_list
 
# if __name__ == '__main__':
#     tmp = time.ctime().split(" ")
#     data = filename(tmp)
    #return 0
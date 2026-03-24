import numpy as np
def f1_micro(y_true, y_pred) -> float:
    npyt= np.array(y_true)
    npyp= np.array(y_pred)
    total = len(y_true)
    TP = np.sum(npyt==npyp)
    FP = total - TP
    F1 = TP/(FP+TP)
    return F1
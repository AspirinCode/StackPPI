import numpy as np
import pickle as p

def aac_pssm(input_matrix):
    seq_cn=float(np.shape(input_matrix)[0])
    aac_pssm_matrix=input_matrix.sum(axis=0)
    aac_pssm_vector=aac_pssm_matrix/seq_cn
    return aac_pssm_vector
def bi_pssm(input_matrix):
    PSSM=input_matrix
    PSSM=np.array(PSSM)
    bipssm=[[0.0]*400]*(PSSM.shape[0]-1)
    p=0
    for i in range(20):
        for j in range(20):
            for h in range(PSSM.shape[0]-1):
                bipssm[h][p]=PSSM[h][i]*PSSM[h+1][j]
            p=p+1
    vector=np.sum(bipssm,axis=0)
    return vector
f1=open('example\Hsapi_pssm_PB.data','rb')
pssm1=p.load(f1)
bi=[]
for i in range(len(pssm1)):
    bi_pssm_obtain=bi_pssm(pssm1[i])
    bi.append(bi_pssm_obtain)
bi_data=np.array(bi)



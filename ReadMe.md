##StackPPI

Improving protein-protein interactions prediction accuracy using XGBoost feature selection and stacked ensemble classifier.

###GcForest-PPI uses the following dependencies:
* python 3.6 
* numpy
* scipy
* scikit-learn

###Guiding principles:

**The dataset file contains the S. cerevisiae, H. pylori, the independent dataset and network dataset.

**Feature extraction
1) Evolutionary information: 
   Evolutionary_information.py is the implementation of AAC-PSSM and Bi-PSSM. 
2) PseAAC.m is the implementation of PseAAC.
3) CTDC.py, CTDT.py, CTDD.py are the implementation of CTD.
4) Auto_yeast.m is the implementation of AD.
  
** Dimensional reduction:
   XGBoost.py represents XGBoost feature selection
   stacking_KPCA.py represents KPCA.
   stacking_LLE.py represents LLE.
   stacking_TSVD.py represents SVD.
   stacking_MDS.py represents MDS.

** Classifier:
   stacking_test.py is the implementation of the stacked ensemble classifier.
   yeast_Ad.py is the implementation of AdaBoost.
   yeast_KNN.py is the implementation of KNN.
   yeast_LR.py is the implementation of LR.
   yeast_RF.py is the implementation of RF.
   yeast_SVM.py is the implementation of SVM.



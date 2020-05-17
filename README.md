# 14-ML-challenge
## **Assumptions**
1. The seller is looking for the highest Price.
2. Price is determined by Weight.
3. Weight is directly proportional to Mass.
**Then, the seller is looking for a high fish mass.**

## **Raw Data Linearity**
![](images/raw_linearity.png)

## **Raw Data Distribution**
![](images/raw_distribution.png)

## **Preprocess**
### Removing Outliers
1. Removing outliers by feature and species using ***IsolationForest***
2. Replace outliers with mean by feature and specie

### Calculated Fields
1. Lmax = Max(Length1, Length2, Length3)
2. Volume = Lmax * Height * Width
3. Mass =  Density * Volume
4. Lavg = Avg(Length1, Length2, Length3)

### Normalize
1. Using ***QuantileTransformer*** to fit a normal distribution
2. Using ***MaxMinScaler*** to adjust the data back to its original min and max range

## **Final Data Linearity**
![](images/linearity.png)

## **Final Data Distribution  (Raw v. Final)**
![](images/distribution.png)

### Feature Selection
1. Calculate feature correlation v. Weight
2. Selected features with correlation greater then 74%

## **Model Training**
1. Train Size: ***76%***
2. Test Size: ***33%***
3. Model Accuracy: ***99.85%***
4. Model Strategy: ***ExtraTreeRegressor***

## **Prediction**
1. mse: ***39.83***

![](images/predictions.png)

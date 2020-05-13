# 14-ML-challenge
### **Assumptions:**
1. The seller is looking for the highest Price.
2. Price is determined by Weight.
3. Weight is directly proportional to Mass.

**Then, the seller is looking for a high fish mass.**

### **Research:**
1. Mass =  Density * Volume
2. Air density ( p ) is constant = 1.225 Kg/m3
3. Lmax = Max(Length1, Length2, Length3)
3. Volume = Lmax * Height * Width
4. The higher the Volume, the higher the Mass, the higher the Price.

### **Data Preparation:**
1. Limit dataframe float values to 3 decimals
2. Calculate columns Mass, Volume
...

### **Target Variable:**
1. y = "Weight

### **Feature Selection:**
1. Select relevant features based on correlation
-> pic
3. X = "Height", "Width", "Lmax", "Mass" ???

### **Model Selection:**
1. Looking for lowest neg_mean_squared_error
2. Looking for highest accuracy
**Models Tested:**
...
**Models Selected:**
...


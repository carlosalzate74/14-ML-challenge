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

**Our formula to predict will be:**

Mass = p * Volume

**Our Matrix (X) and Target (y) will be:**

X = "Height", "Width", "Lmax", "Mass"

y = "Weight"




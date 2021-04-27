# Inisisalisasi
"""
wi = 0 ; i = 1 ,2, 3, ....
bias = 0


"""

Bias = 0
DNet = 0

Xn = int(input("input jumlah X = "))
Data = int(input("input jumlah data = "))

# W lama
W_List = []
# W baru
W_hasil = []

for batas in range(Xn):
    W_List.append(0)
    W_hasil.append(0)

X_List= []
T_List = []


Net = []

# input data 
for data in range(Data):
    print("data", data)
    X_List.append([])
    for x in range(Xn):
        X_List[data].append(int(input("Nilai X{} (Note : 0 atau -1 dan 1) = " .format(x))))
    T_List.append(int(input("Nilai Target data{} (Note : 0 atau -1 dan 1)= " .format(x))))
    print()


# menampilkan input X
for tpl_colom2 in range (Xn):
    print("X"+str(tpl_colom2),end='\t')
print()

for tpl_data1 in range(Data):
    for tpl_data2 in range (Xn):
        print(X_List[tpl_data1][tpl_data2],end='\t')
    print()


# menampilkan target
print("\nTarget")
for tpl_target2 in range (Data):
    print(T_List[tpl_target2])
print()


        
# perhitungan W
# W baru = W lama + (Xi * Yi)
# Bias = bias(lama) + Y
for x_dimensi_1 in range(Data): 
    for x_dimensi_2 in range(Xn):
        W_List[x_dimensi_2] = X_List[x_dimensi_1][x_dimensi_2] * T_List[x_dimensi_1]
    for x_dimensi_2 in range(Xn):
        W_hasil[x_dimensi_2] = W_hasil[x_dimensi_2] + W_List[x_dimensi_2]    
    Bias = Bias + T_List[x_dimensi_1]
    print()



# perhitungan Net
# Net = Sum(Xi * Wi) + b
for i in range(Data):
    DNet = 0
    for j in range(Xn):
        DNet += X_List[i][j] * W_hasil[j]
    
    Net.append(DNet + Bias)
    # print("Net = ",Net[i])
print()

print("Net = ",Net)


# inisialisasi FNet
for k in range(Data):
    if Net[k] >= 0:
        Net[k] = 1
    else:
        Net[k] = 0

# print("FNet = ",Net)


# menampilkan Nilai Fnet
print("Fnet")
for Net_hasil in range (Data):
    print(Net[Net_hasil])
print()



# Testing

# inisisalisasi
print("Testing " )
print("Bias : ", Bias)
Hasil = 0
for tes in range (Xn):
    print("W"+str(tes)+" = ",W_hasil[tes])

Data_uji = []

# input data yg diuji
for data_uji in range(Xn):
    Data_uji.append(int(input("masukan uji data {} = ".format(data_uji))))


# Mencari nilai Net
for hasil in range (Xn):
    Hasil += Data_uji[hasil] * W_hasil[hasil]

net_uji = Hasil + Bias


# mencari nilai Fnet
Fnet_uji = net_uji

print("net = ",Fnet_uji)
if Fnet_uji >= 0:
    Fnet_uji = 1
else:
    Fnet_uji = 0

# hasil
print("Fnet = ",Fnet_uji)


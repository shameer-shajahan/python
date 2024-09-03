#      *
#     * *
#    * * *
#   * * * * 
#  * * * * * 

# for row in range(1,4):
#     for col in range(1,row+1):
#         print("@",end=" ")
#     print("\n")

for row in range(1,7):
    for col in range(row,7):
        print("",end=" ")
    for col in range(row):
        print("*",end=" ")
    print("\n")
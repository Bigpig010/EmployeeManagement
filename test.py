# while True:
#     Phai = input("Enter gender (Male/Female): ")
#     if Phai in ["Male", "Female"]:
#         break
#     else:
#         print("Error: Gender must be 'Male' or 'Female'. Please Try Again!!!.")
#         continue


while True:
    MaNV = input("Enter employee id: ")
    if not MaNV.isdigit():
        print("Error: Employee id must be a number, Please Try Again!!!")

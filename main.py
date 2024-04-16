from EmployeeManager import EmployeeManager
from Employees import Employees

manager = EmployeeManager()

while True:
    print("1: Add new employee")
    print("2: Edit employee info")
    print("3: Detele employee")
    print("4: view employee list by departments type")
    print("5: view raw in the file")
    print("0: Exit the program")

    choice = input("Enter number (0 to quit): ")

    if choice == "0":
        break
    elif choice == "1":
        while True:
            while True:
                MaNV = input("Enter employee id: ")
                if not MaNV.isdigit():
                    print("Error: Employee id must be a number, Please Try Again!!!")
                else: break
                    

            if manager.check_employee_exists(MaNV):
                print(f"Error: Employee with id {MaNV} already exists!")
                continue

            while True:
                HoTen = input("Enter full name: ")
                if HoTen.strip() == "":
                    print("'Full name' cannot be blank. Please Try Again!!!.")
                else: break

            NgaySinh = manager.get_formatted_date()

            while True:
                Phai = input("Enter gender (Male/Female): ")
                if Phai in ["Male", "Female"]: break
                else: print("Error: Gender must be 'Male' or 'Female'. Please Try Again!!!.")

            while True:
                Diachi = input("Enter address: ")
                if Diachi.strip() == '':
                    print("'Address' cannot be blank. Please Try Again!!!.")
                else: break
                    
            while True:
                Phong = input("Enter departments: ")
                if Phong.strip() == '':
                    print("Departments cannot be blank. Please Try Again!!!.")
                else: break

            employee = Employees(MaNV, HoTen, NgaySinh, Phai, Diachi, Phong)
            manager.add_employee(employee)
            manager.view_raw_data()

            add = input("Do you want add employees? (Y/N) : ").lower()
            if add != 'y': break

    elif choice == "2":
        manager.view_raw_data()
        while True:
            while True:
                MaNV = input("Enter employee id you want edit: ")
                if not MaNV.isdigit():
                    print("Error: Employee id must be a number, Please Try Again!!!")
                else: break
                    
            edit = input("Are you sure want to edit employee's information (Y/N) : ").lower()
            if edit == "y":
                # Kiểm tra xem MaNV có tồn tại trong danh sách nhân viên không
                found = False
                for employee in manager.employees:
                    if employee["MaNV"] == MaNV:
                        found = True
                if not found:
                    print("Error: Employee not found!")
                else:
                    print("Enter the new info for the employee: ")
                    
                    while True:
                        HoTen = input("Enter full name: ")
                        if HoTen.strip() == "":
                            print("'Full name' cannot be blank. Please Try Again!!!.")
                        else: break
                            
                    NgaySinh = manager.get_formatted_date()
                    
                    while True:
                        Phai = input("Enter gender (Male/Female): ")
                        if Phai in ["Male", "Female"]: break
                        else: print("Error: Gender must be 'Male' or 'Female'. Please Try Again!!!.")
                            
                    while True:
                        Diachi = input("Enter address: ")
                        if Diachi.strip() == '':
                            print("'Address' cannot be blank. Please Try Again!!!.")
                        else: break
                        
                    while True:
                        Phong = input("Enter departments: ")
                        if Phong.strip() == '':
                            print("Departments cannot be blank. Please Try Again!!!.")
                        else: break
                            
                    new_data = {
                        "HoTen": HoTen,
                        "NgaySinh": NgaySinh,
                        "Phai": Phai,
                        "DiaChi": Diachi,
                        "Phong": Phong,
                    }
                    manager.edit_employee(MaNV, new_data)
                    manager.view_raw_data()
                    add = input("Do you want edit other employee's information? (Y/N) : ").lower()
                    if add != 'y': break
                        
    elif choice == "3":
        manager.view_raw_data()
        while True:
            while True:
                MaNV = input("Enter employee id you want delete: ")
                if not MaNV.isdigit():
                    print("Error: Employee id must be a number!")
                else: break
                
            delete = input( "Are you sure want to delete employee's information (Y/N) : ").lower()
            if delete == "y":
                manager.delete_employee(MaNV)
                manager.view_raw_data()
            want= input("Do you want delete other employee's information? (Y/N) : ").lower()
            if want != 'y': break
                
            
    elif choice == "4":
        while True:
            while True:
                Phong = input("Enter the departments type you want to view: ")
                if not Phong.isdigit():
                    print("Error: Departments type must be a number, Please Try Again!!!")
                else: break
                
            manager.view_employee_by_departments_type(Phong)
            want= input("Do you want to see information about employees of other departments? (Y/N) : ").lower()
            if want != 'y': break
            
    elif choice == "5":
        manager.view_raw_data()
        
    elif choice > "5":
        print("Error: Wrong choices, Please Try Again!!! (From 0 to 5)")

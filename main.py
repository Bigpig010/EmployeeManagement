from EmployeeManager import EmployeeManager
from Employees import Employees
manager= EmployeeManager()

while True:
    print('1: Add new employee')
    print('2: Edit employee info')
    print('3: Detele employee')
    print('4: view employee list by departments type')
    print('5: view raw in the file')
    print('0: Exit the program')
    
    choice= input('Enter number (0 to quit): ')
    
    if choice == '0':
        break
    elif choice == '1':
        MaNV= input('Enter employee id: ')
        if not MaNV.isdigit():
            print('Error: Employee id must be a number, Please Try Again!!!')
            continue
        if manager.check_employee_exists(MaNV):
            print(f'Error: Employee with id {MaNV} already exists!')
        else:
            HoTen= input('Enter full name: ')
            if HoTen.strip()
                continue
            else:
                print("'Full name' cannot be blank. Please Try Again!!!.")
            NgaySinh= input('Enter date of birth (Only number): ')
            if not NgaySinh.isdigit():
                print('Error: Date of birth must be a number!')
                    continue
                if NgaySinh.strip()
                    continue
                else:
                    print("'Date of birth' cannot be blank. Please Try Again!!!.")
            Phai = input('Enter gender (Male/Female): ')
                if Phai in ['Male', 'Female']:
                else:
                    print("Error: Gender must be 'Male' or 'Female'. Please Try Again!!!.")
            Diachi= input('Enter address: ')
            if DiaChi.strip()
                continue
            else:
                print("'Address' cannot be blank. Please Try Again!!!.")
            Phong= input('Enter departments: ')
            if Phong.strip()
                continue
            else:
                print("'Departments' cannot be blank. Please Try Again!!!.")
            employee= Employees(MaNV, HoTen, NgaySinh, Phai, Diachi, Phong)
            manager.add_employee(employee)
            manager.view_raw_data()      

    elif choice == '2':
        manager.view_raw_data()
        MaNV = input('Enter employee id you want to edit: ')
        if not MaNV.isdigit():
            print('Error: Employee id must be a number!')
            continue
        edit = input("Are you sure want to edit employee's information (y/n) : ").lower()
        if edit == 'y':
        # Kiểm tra xem MaNV có tồn tại trong danh sách nhân viên không
            found = False
            for employee in manager.employees:
                if employee['MaNV'] == MaNV:
                    found = True
            if not found:
                print('Error: Employee not found!')
            else:
                print('Enter the new info for the employee: ')
            HoTen = input('Enter full name: ')
                if HoTen.strip()
                    continue
                else:
                    print("'Full name' cannot be blank. Please Try Again!!!.")
            NgaySinh = input('Enter date of birth (Only number): ')
                if NgaySinh.isdigit():
                    print("'Date of birth' cannot be blank. Please Try Again!!!.")
                    continue
                if NgaySinh.strip()
                    continue
                else:
                    print("'Date of birth' cannot be blank. Please Try Again!!!.")
            Phai = input('Enter gender (Male/Female): ')
                if Phai in ['Male', 'Female']:
                else:
                    print("Error: Gender must be 'Male' or 'Female'. Please Try Again!!!.")
            Diachi= input('Enter address: ')
                if DiaChi.strip()
                    continue
                else:
                print("'Address' cannot be blank. Please Try Again!!!.")
            Phong= input('Enter departments: ')
                if Phong.strip()
                    continue
                else:
                print("'Departments' cannot be blank. Please Try Again!!!.")
                new_data = {'HoTen': HoTen, 'NgaySinh': NgaySinh, 'Phai': Phai, 'DiaChi': Diachi, 'Phong': Phong}
                manager.edit_employee(MaNV, new_data)
                manager.view_raw_data()

    elif choice == '3':
        MaNV= input('Enter employee id you want delete: ')
        if not MaNV.isdigit():
            print('Error: Employee id must be a number!')
            continue
        delete= input('Are you sure want to delete employee\'s information (Y/N) : ').lower()
        if delete  == 'y':
            manager.delete_employee(MaNV)
            manager.view_raw_data()
    elif choice == '4':
        Phong= input('Enter the departments type you want to view: ')
        if not Phong.isdigit()
        print('Error: Departments type must be a number, Please Try Again!!!')
            continue
        if Phong.strip()
            continue
        else:
            print("'Departments type' cannot be blank. Please Try Again!!!.")
        manager.view_employee_by_departments_type(Phong)
    elif choice == '5':
        manager.view_raw_data()
    elif choice > "5":
        print('Error: Wrong choices, Please Try Again!!! (From 0 to 5)')
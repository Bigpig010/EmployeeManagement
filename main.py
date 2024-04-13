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
        if manager.check_employee_exists(MaNV):
            print(f'Error: Employee with id {MaNV} already exists!')
        else:
            HoTen= input('Enter full name: ')
            NgaySinh= input('Enter date of birth (Only number): ')
            Phai = input('Enter gender (Male/Female): ')
            Diachi= input('Enter address: ')
            Phong= input('Enter departments: ')
            employee= Employees(MaNV, HoTen, NgaySinh, Phai, Diachi, Phong)
            manager.add_employee(employee)
            manager.view_raw_data()      

    elif choice == '2':
        manager.view_raw_data()
        MaNV = input('Enter employee id you want to edit: ')
        edit = input('Are you sure want to edit employee\'s information (Y/N) : ').lower()
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
                NgaySinh = input('Enter date of birth (Only number): ')
                Phai = input('Enter gender (Male/Female): ')
                Diachi = input('Enter address: ')
                Phong = input('Enter departments: ')
                new_data = {'HoTen': HoTen, 'NgaySinh': NgaySinh, 'Phai': Phai, 'DiaChi': Diachi, 'Phong': Phong}
                manager.edit_employee(MaNV, new_data)

    elif choice == '3':
        MaNV= input('Enter employee id you want delete: ')
        delete= input('Are you sure want to delete employee\'s information (Y/N) : ').lower()
        if delete  == 'y':
            manager.delete_employee(MaNV)
            manager.view_raw_data()
    elif choice == '4':
        Phong= input('Enter the departments type you want to view: ')
        manager.view_employee_by_departments_type(Phong)
    elif choice == '5':
        manager.view_raw_data()
    elif choice > "5":
        print('Error: Wrong choices, Please Try Again!!! (From 0 to 5)')
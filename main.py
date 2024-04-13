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
        HoTen= input('Enter full name: ')
        NgaySinh= input('Enter date of birth: ')
        Phai= input('Enter gender: ')
        Diachi= input('Enter address: ')
        Phong= input('Enter departments: ')
        employee= Employees(MaNV, HoTen, NgaySinh, Phai, Diachi, Phong)
        manager.add_employee(employee)
        manager.view_raw_data()      

    elif choice == '2':
        manager.view_raw_data()
        MaNV= input('Enter employee id you want edit: ')
        edit= input('Are you sure want to edit employee\'s information (Y/N) : ').lower()
        if edit  == 'y':
            print('Ener the new info for the employee: ')
            HoTen= input('Enter full name: ')
            NgaySinh= input('Enter date of birth: ')
            Phai= input('Enter gender: ')
            Diachi= input('Enter address: ')
            Phong= input('Enter departments: ')
            new_data= {'HoTen': HoTen, 'NgaySinh': NgaySinh, 'Phai': Phai, 'DiaChi': Diachi, 'Phong': Phong}
            manager.edit_employee(MaNV, new_data)
    elif choice == '3':
        MaNV= input('Enter employee id you want delete: ')
        delete= input('Are you sure want to delete employee\'s information (Y/N) : ').lower()
        if delete  == 'y':
            manager.delete_employee(MaNV)
    elif choice == '4':
        Phong= input('Enter the departments type you want to view: ')
        manager.view_employee_by_departments_type(Phong)
    elif choice == '5':
        manager.view_raw_data()
    elif choice > "5":
        print('Error: Wrong choices, Please Try Again!!! (From 0 to 5)')
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
        # manager.check_employee(MaNV, employee)
        HoTen= input('Enter full name: ')
        NgaySinh= input('Enter date of birth: ')
        Phai= input('Enter gender: ')
        Diachi= input('Enter address: ')
        Phong= input('Enter departments: ')
        employee= Employees(MaNV, HoTen, NgaySinh, Phai, Diachi, Phong)
        manager.add_employee(employee)
    elif choice == '2':
        MaNV= input('Enter employee id you want edit: ')
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
        manager.detele_employee(MaNV) 
    elif choice == '4':
        Phong= input('Enter the departments type you want to view: ')
        manager.view_employee_by_departments_type(Phong)
    elif choice == '5':
        manager.view_raw_data()


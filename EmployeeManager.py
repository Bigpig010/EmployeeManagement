import json
from prettytable import PrettyTable
class EmployeeManager:
    def __init__(self):
        self.employees = []
        self.load_data()

    def load_data(self):
        try:
            with open('DuLieu.txt', 'r') as f:
                self.employees = json.load(f)
        except FileNotFoundError:
            self.employees = []

    def save_data(self):
        with open('DuLieu.txt', 'w') as f:
            json.dump(self.employees, f)
            
    def add_employee(self, employee):
        for e in self.employees:
            if e['MaNV'] == employee.MaNV:
                print(f'Error: Employee with id {employee.MaNV} already exists!')
                return
        self.employees.append(employee.__dict__) 
        self.save_data()
        
    def edit_employee(self, MaNV, new_data):
        for e in self.employees:
            if e['MaNV'] == MaNV:
                e.update(new_data)
                self.save_data()
                return
            print('Error: Employee not found!')
        
    def detele_employee(self, MaNV):
        self.employees= [e for e in self.employees if e['MaNV'] != MaNV]
        self.save_data()
        
    def view_employee_by_departments_type(self, Phong):
        employees= self.get_employee_by_departments_type(Phong)
        table= PrettyTable(['STT', 'MaNV', 'HoTen', 'NgaySinh', 'Phai', 'DiaChi', 'Phong'])
        for i, employees in enumerate(employees):
            table.add_row([i+1, employees['MaNV'], employees['HoTen'], employees['NgaySinh'], employees['Phai'], employees['DiaChi'], employees['Phong']])
        print(table)
    
    def view_raw_data(self):
        data= self.get_raw_data()
        table= PrettyTable(['STT', 'MaNV', 'HoTen', 'NgaySinh', 'Phai', 'DiaChi', 'Phong'])
        for i, item in enumerate(data):
            table.add_row([i+1, item['MaNV'], item['HoTen'], item['NgaySinh'], item['Phai'], item['DiaChi'], item['Phong']])
        print(table)
    
    def get_employee_by_departments_type(self, Phong):
        return [employee for employee in self.employees if employee['Phong']== Phong]
    
    def get_raw_data(self):
        return self.employees
    
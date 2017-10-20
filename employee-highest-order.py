def highest_management_order(count): 
    emp_dict = {}
    root_node = None
    counter = 0

    while len(emp_dict) < count:
        user_input = str(input("Enter Name: "))

        if counter == 0:
            emp1 = user_input
        elif counter == 1:
            emp2 = user_input
        else:
            emps = user_input.split()
            # check manager exists in emp_dict
            manager = emp_dict.get(emps[0])
            if manager is None:
                manager = EmployeeTreeNode(emps[0])
                if manager.level == 0:
                    root_node = manager
                emp_dict[emps[0]] = manager

            # check employee exists in emp_dict
            employee = emp_dict.get(emps[1])
            if employee is None:
                employee = EmployeeTreeNode(emps[1], manager)
                emp_dict[emps[1]] = employee

        counter += 1

    employee1 = search_emp_by_name(emp1, root_node)
    employee2 = search_emp_by_name(emp2, root_node)
    print(highest_order_manager(employee1, employee2))    

def search_emp_by_name(name, node):
    if node.name == name:
        return node  
    for elem in node.children:
        found = search_emp_by_name(name, elem)
        if found:
            return found 

def highest_order_manager(emp1, emp2):    
    emp1_reporting_lines = get_reporting_line(emp1, [emp1])
    emp2_reporting_lines = get_reporting_line(emp2, [emp2])

    if emp1 > emp2:
        return (compare_reporting_lines(emp2_reporting_lines, emp1_reporting_lines))
    else:
        return (compare_reporting_lines(emp1_reporting_lines, emp2_reporting_lines))

def get_reporting_line(emp, reporting_lines):
    manager = emp.manager
    if manager is None:
        return reporting_lines

    reporting_lines.append(manager)
    return get_reporting_line(manager, reporting_lines)

def compare_reporting_lines(compare_from, compare_to):
    for reporting_line in compare_from:
        if reporting_line in compare_to:
            return reporting_line.name

class EmployeeTreeNode():
    def __init__(self, name, manager=None):
        self.name = name
        self.children = []
        self.manager = manager
        if self.manager is not None:
            self.level = manager.level + 1
            self.manager.children.append(self)
        else:
            self.level = 0

    def __gt__(self, other):
        return self.level < other.level

if __name__ == "__main__":
    _count = int(input("How many unique employee?"))
    highest_management_order(_count)

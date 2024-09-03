# print total salary of employee ?

employee={"name=":"hari",
          "dept":"r&d",
          "salary":50000,
          "combo_offer":1000,
          "extra_work":3}

if "extra_work" in employee:
    total_salary = (employee.get("combo_offer")*(employee.get("extra_work")))+(employee.get("salary"))
    print(total_salary)
else:
    total_salary=employee.get("salary")
    print(total_salary)
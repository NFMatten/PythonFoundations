# Pay rate will be 20 for control test
# Overtime 50 for control test
# 1100.00 per week, 52 weeks (No time off/holidays) = 1100.00 * 12 = 57200
# Colorado state income tax = 4.55%

normal_work_day = 8
weeks_in_year = 52
standard_work_week = 40
overtime_multiplier = 1.5
pay_rate = float(input("\nPlease enter your pay rate: "))
hours_worked = float(input("Please enter number of hours worked: "))

# Calculating pay before taxes
if hours_worked > standard_work_week:
    regular_pay = pay_rate * standard_work_week
    hours_of_overtime = hours_worked - standard_work_week
    pay_rate_on_overtime = pay_rate * overtime_multiplier
    overtime_pay = hours_of_overtime * pay_rate_on_overtime
    total_pay_before_taxes = overtime_pay + regular_pay
    annual_pay = total_pay_before_taxes * weeks_in_year
else:
    total_pay_before_taxes = pay_rate * hours_worked
    annual_pay = total_pay_before_taxes * weeks_in_year
print(f'\nWeekly pay: ${round(total_pay_before_taxes,2)}; Annual pay: ${round(annual_pay,2)}')
print("-" * 50)

# Income taxes
federal_tax = 0.0936
state_tax = 0.0455
social_security_tax = 0.062
medicare_tax = 0.0145
total_taxes = (federal_tax + state_tax + social_security_tax + medicare_tax)

# Taking taxes from pay
taxes_taken_out = annual_pay * total_taxes
total_pay = annual_pay - taxes_taken_out
print(f'Taxes taken out: ${round(taxes_taken_out,2)}. Total taxes: {round((total_taxes*100),2)}%\n')
print(f'Total Pay After Taxes: ${round(total_pay,2)}')
print("-" * 50)

# Accruing PTO
hours_needed_per_one_hour_PTO = 40
accrued_PTO = hours_worked / hours_needed_per_one_hour_PTO
print(f'\nPTO Balance after {hours_worked} work week: {accrued_PTO} hour(s).\n')

hours_worked_in_year = weeks_in_year * standard_work_week
print(f'Hours worked in a year at 40 hours per week for 52 weeks: {hours_worked_in_year} hours.\n')

annual_accrued_pto_hours = hours_worked_in_year / hours_needed_per_one_hour_PTO
print(f"Yearly PTO for normal 40 hour week for 52 weeks: {annual_accrued_pto_hours} hours.\n")

days_of_accrued_pto = annual_accrued_pto_hours / normal_work_day
print(f'Days of accrued PTO, 40hr/wk for 52 weeks: {days_of_accrued_pto} days.\n')
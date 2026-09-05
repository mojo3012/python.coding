field1 = 120

field2 = 85

field3 = 150

field4 = 95

field5 = 110
total= field1+field2+field3+field4+field5
average=total/5
unit_price=15
total_earnings=total*unit_price
print(f'Total in kg= {total}')
print(f'Average in kg= {average}')
print(f'Total earnings= {total_earnings}')
bags=total//25
leftover=total%25
print(f'Number of bags packed= {bags}' )
print(f'Leftover crop in kg= {leftover}')
last_year_production=500
extra=total-last_year_production
extra_earnings=extra*unit_price
print(f'Extra crops produced this year in kg= {extra}')
print(f'Extra earnings this year= {extra_earnings}')
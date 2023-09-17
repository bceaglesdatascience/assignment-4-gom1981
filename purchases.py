lst_cost = []
lst_cust = []


n = int(input("Number of purchases: "))
tax = float(input("Sales tax: "))
 
def add_tax(lstc,tax):
  new_list=[]
  for i,c in enumerate(lstc):
    new_list.append(lstc[i]*(tax+1.0))
  return new_list

for i in range(0, n):
    cust = input("Customer: ")
    lst_cust.append(cust) 
    cost = float(input("Cost: "))
    lst_cost.append(cost) 
 
lst_cost=add_tax(lst_cost,tax)

total_cost_dict={}

for i, cust in enumerate(lst_cust):
  if cust in total_cost_dict:
    total_cost_dict[cust]+=lst_cost[i]
  else:
    total_cost_dict[cust]=lst_cost[i]
    
print(total_cost_dict)

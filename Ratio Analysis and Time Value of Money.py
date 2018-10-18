# Financial Information and Analytics
# Assignment 1
# By Rajat Sudagade (UTD ID: 2021449378)

# Part 1: Ratio Analysis

# Question 1: Find change in Net working Capital (NWC)
def ratio1():
  currentAssets2008 = 1240 # Current Assets in 2008
  currentLiabilities2008 = 820 # Current Liabilities in 2008
  nwc2008 = currentAssets2008 - currentLiabilities2008 # Net Working Capital in 2008
  currentAssets2009 = 1660 # Current Assets in 2009
  currentLiabilities2009 = 1180 # Current Liabilities in 2009
  nwc2009 = currentAssets2009 - currentLiabilities2009 # Net Working Capital in 2009
  NWC = nwc2009 - nwc2008 # Changing in Net working Capital
  print("""Question 1:
  Saddle Creek, Inc.'s 2009 change in net working capital is ${:,.2f}\n""".format(NWC))

# Question 2: Find Cash Flow to Creditors
def ratio2():
  longTermDebt2008 = 2600000 # Long Term Debt in 2008
  longTermDebt2009 = 3900000 # Long Term debt in 2009
  interestExpense = 270000 # Interest Expense
  #Cash Flow To Creditors = CFTC = Interest Expense - Long Term Debt in 2009 - Long Term Debt in 2008
  CFTC = interestExpense - longTermDebt2009 + longTermDebt2008
  print("""Question 2:
  In 2009, Maria's Tennis Shop, Inc. had a cash flow to creditors of ${:,.2f}\n""".format(CFTC)) 

#Question 3: Cash Flow to StockHolders
def ratio3():
  cs2008 = 930000 #Common Stock in 2008
  surplus2008 = 6600000 # Additional paid-in surplus in 2008
  cs2009 = 955000 # Common stock in 2009
  surplus2009 = 8650000 # Additional paid-in surplus in 2009
  cd2009 = 530000 # Cash Dividends in 2009
  cs = cs2009 - cs2008 # Common Stock
  surplus = surplus2009 - surplus2008 # Surplus
  cashflowtostockholders = cd2009 - cs - surplus # Cash Flow to Stock Holders = Cash Dividends in 2009 - Common Stock - Surplus
  print("""Question 3:
  The Cash Flow to stockholders for 2009 was {:,.2f}\n""".format(cashflowtostockholders))

# Question 4: Operating Cash Flow
def ratio4():
  # Step 1: Calculate Cash Flow To Creditors
  interestExpense = 180000 # Interest Expenses
  longTermDebt2008 = 2700000 # Long Term Debt in 2008
  longTermDebt2009 = 4250000 # Long Term Debt in 2009
  longTermDebt = longTermDebt2009 - longTermDebt2008 # Long Term Debt
  cashFlowToCreditors = interestExpense - longTermDebt
  # Step 2: Calculate Cash Flow to Stockholders
  cashDividends = 650000 # Cash Dividends
  commonStock2008 = 730000 # Common Stock in 2008
  commonStock2009 = 955000 # Common Stock in 2009 
  commonStock = commonStock2009 - commonStock2008 # Common Stock
  surplus2008 = 6050000 # Surplus in 2008
  surplus2009 = 8650000 # Surplus in 2009
  surplus = surplus2009 - surplus2008 # Surplus
  cashflowstockholders = cashDividends  - ((commonStock2009 + surplus2009) - (commonStock2008 + surplus2008))
  # Step 3: Calculate total cash flow from assets
  cashFlowAssets = cashflowstockholders + cashFlowToCreditors
  # Step 4: Calculate Operating Cash Flow
  netCapitalSpending = 860000 # Net Capital Spending
  reduceNWC = -165000 # Reduce in Net Working Capital 
  ocf = cashFlowAssets + netCapitalSpending + reduceNWC
  print("""Question 4:
  The Operating Cash Flow will be ${:,.2f}\n""".format(ocf))

# Question 5: Determine Common Stock
def ratio5():
  # Information
  cash = 390000
  patentCopyright = 690000
  accountsPayable = 340000
  accountsReceivable = 139000
  tangibleNetFixedAssets = 4700000
  inventory =205000
  notesPayable = 170000
  accumulatedRetainedEarnings = 1335000
  longTermDebt = 1830000
  # Step 1: Calculate Total Assets
  totalAssets = cash + patentCopyright + accountsReceivable + tangibleNetFixedAssets + inventory
  # Step 2: Calculate Total Liabilities
  totalLiabilities = accountsPayable + notesPayable + longTermDebt
  # Note: Here, the total shareholder equity is equal to accumulated Retained Earnings
  # Step 3: Calculate common stocks
  commonStock = totalAssets - (totalLiabilities + accumulatedRetainedEarnings)
  print("""Question 5:
  The Common Stock of Bertinelli Corp. is {:,.2f}\n""".format(commonStock))

# Part 2: Time Value of Money

# Question 1: Percentage increase in money
def tvm1():
  # a. Percentage increase per year from 1895 to 2007 
  value1895 = 120 # Prize value in 1895
  value2007 = 1179000 # Prize value in 2007
  years = 2007 - 1895 # Number of years between 1895 and 2007
  increasePerYear = ((value2007/value1895)**(1/years)-1) # increase in prize value per year 
  percentageIncreasePerYear = increasePerYear * 100 # percentage of increase in prize value per year
  # b. Prize value in the year 2040
  newYears = 2040 - 1895 # Number of years between 2040 and 1895
  futureValue = value1895 * ((1 + (increasePerYear))**(newYears)) # Estimated future value of the prize in the year 2040
  print("""Question 1:
  The percentage increase per year is {0:,.2f}%"
  The winner's prize in 2040 is ${1:,.2f}\n""".format(percentageIncreasePerYear, futureValue))

# Question 2: Annual Rate of Return 
def tvm2():
  value2003 = 10305500 # Painting sold in 2003 for 
  value1999 = 12385500  # Painting sold in 1999 for
  years = 2003 - 1999 # Number of years between 1999 and 2003
  annualROR = ((value2003/value1999)**(1/years)) - 1 # Annual rate of return
  annualRORPercentage = annualROR * 100 # Annual Rate of return as percentage
  print("""Question 2:
  The Annual Rate of Return is {:,.2f}%\n""".format(annualRORPercentage))

# Question 3: Future Value of Money
def tvm3():
  # Value after 35 years?
  presentValue = 2000 # Present value
  rateofReturn = 0.1 # Rate of Return
  years = 35 # Investment duration
  futureValue = presentValue * ((1 + rateofReturn)**(years)) # Value of money after 35 years
  # waiting 7 years,
  newYears = 28 # 35 - 7 # New Investment duration
  newFutureValue = presentValue * ((1 + rateofReturn)**(newYears)) # Value of money after 28 years
  print("""Question 3:
  The account will be worth ${0:,.2f} in 35 years
  If you wait 7 years before contributing, then the account will be worth ${1:,.2f} after 35 years \n""".format(futureValue, newFutureValue))

# Question 4
def tvm4():
  principal = 29000 # Principal
  rateofReturn = 0.05 # Rate of Return
  period = 8 # Number of Years
  amount = principal*((1 + rateofReturn)**(period)) # Amount
  print("""Question 4:
  After 10 years, we will have ${:,.2f} \n""".format(amount))

# Question 5
def tvm5():
  import math
  presentValue = 8000 # Present value 
  futureValue = 95000 # Future Value
  ratePerPeriod = 0.12 # Interest rate per year
  time = (math.log(futureValue/presentValue))/(math.log(1 + ratePerPeriod)) + 2 # Number of years
  timePlus2 = time 
  print("Question 5:")
  print("We will have to wait for {:,.2f} years for the value to reach $95,000\n".format(time))

# Print functions
print("""Financial Information and Analytics\n
Assignment 1\n
Ratio Analysis and Time Value of Money\n
By Rajat Sudagade (UTD ID 2021449378)\n""")
def menu():
  a = int(input("""Press 1 for Ratio analysis\nPress 2 for Time Value of Money\nPress 3 for All\nPress any other number to exit\n"""))
  if (a == 1):
    print("\n")
    print("Displaying Part 1: Ratio Analysis\n")
    ratio1()
    ratio2()
    ratio3()
    ratio4()
    ratio5()
    menu()
  elif (a == 2):
    print("\n")
    print("Displaying Part 2: Time Value\n")
    tvm1()
    tvm2()
    tvm3()
    tvm4()
    tvm5()
    menu()
  elif (a == 3):
    print("\n")
    print("Displaying Part 1: Ratio Analysis\n")
    ratio1()
    ratio2()
    ratio3()
    ratio4()
    ratio5()
    print("\n")
    print("Displaying Part 2: Time Value\n")
    tvm1()
    tvm2()
    tvm3()
    tvm4()
    tvm5()
    menu()
  else:
    pass

menu()
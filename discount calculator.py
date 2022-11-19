orginalPrice = float(input("WHAT'S THE PRICE ? : $ "))
discountPercent = int(input("HOW MUCH PERCENT DISCOUNT  : % "))
#--------------------Formula to find Final price with offer----------------------------------
formulaFinalPrice = round((orginalPrice-orginalPrice*(discountPercent/100)),2)
#----------------------------------------------------------------------------------------
print(f"YOU SHOULD PAY -> $ {formulaFinalPrice}")
print(f"YOU SAVE -> $ {round((orginalPrice-formulaFinalPrice),2)}")

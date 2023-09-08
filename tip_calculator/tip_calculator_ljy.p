DECLARE bill : REAL
DECLARE percentage : INTEGER
DECLARE people : INTEGER
DECLARE eachpay : REAL

OUTPUT "Welcome to the tip calculator"
OUTPUT "What was the total bill?"
INPUT bill
OUTPUT "What percentage tip would you like to give? 10, 12 or 15?"
INPUT percentage
WHILE percentage<>10 AND percentage<>12 AND percentage<>15 DO
    OUTPUT "You cannot choose that percentage. Try 10, 12 or 15"
    INPUT percentage
ENDWHILE
OUTPUT "How many people to split the bill?"
INPUT people
eachpay <- ROUND((bill*(100+percentage)/100) / people,2)
OUTPUT "Each person should pay: ", eachpay
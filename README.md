# FINE3000-2026-A1
FINE 3000 Assignment 1: Currency Converter USD to CAD using Bank of Canada exange rates 2025

**FINE 3000 - Fall 2026**

# USD/CAD Currency Converter 2025 Rate

## Description
This code converts monirtary amounts between US dollars (USD) and Canadian dollars (CAD) using the latest rate.

## How It Works:
- Reads the Bank of Canada exchange rate file and takes the latest USD/CAD rate
- Asks the user for the amount and the 'from' and 'to' currency
- Converts the amount and prints the result with dollar signs, currency codes, and round to the nearest cent

## How to Use:
Keep the CSV file in the same folder as the code, then run the program and answer the prompts accurately.

## Write-Up
a) Link to GitHub repository
https://github.com/elyssadest/FINE3300-2026-A1.git

b) Program Output for $100,000
USD to CAD:
How much would you like to convert?: 100000
From which currency? (USD or CAD): USD
To which currency? (USD or CAD): CAD
Success! You have completed the conversion from $100,000.00 USD to $139,780.00 CAD

CAD to USD:
How much would you like to convert?: 100000
From which currency? (USD or CAD): CAD
To which currency? (USD or CAD): USD
Success! You have completed the conversion from $100,000.00 CAD to $71,540.99 USD

c) LLM Model and Prompts
Model used: Microsoft Copilot, free version

I used the free CoPilot application to complete the part 2 task.
Prompts give: 
1. (Uploaded the Bank of Canada exchange rate CSV file and the assignment file) "Use these files to complete the code of part 1 so I can do part 2."
2. "Compile all codes into one to paste into my coding platform."
3. "Add input so I can convert specific amounts of money."

d) Comparison:
Both programs perform the same function: they convert amounts between USD and CAD using the most recent exchange rate in the Bank of Canada file, and both produce identical results ($139,780.00 CAD and $71,540.99 USD for a $100,000 conversion). The primary difference lies in how the file is read
My code uses the pandas library to load the file and retrieve the latest rate in a single line with iloc[-1], whereas Copilot uses Python’s built-in csv to input the file and loops through every row to reach the last one, which requires more lines of code to achieve the same result.
As well, my class reads a fixed file name within the constructor, while Copilot’s class accepts the file name as a parameter, making it reusable with other exchange rate files.
Copilot’s initial version did not prompt the user for an amount and was fixing the amount as 100,000 so an additional prompt was required to add user input.
Copilot also included features beyond the assignment’s requirements, such as input validation despite the assignment stating that users would provide valid input.
Its code also has the user interaction in an if "__name__ == __main__:"  section which is sperating the class definition from the program’s output.
Copilot’s code is approximately 60 lines long, compared to roughly 25 lines for mine, about 50% shorter.
Ultimately, my code is more concise and easier to follow for the scope of this assignment.



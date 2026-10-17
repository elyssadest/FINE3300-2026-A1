import csv

class ExchangeRates:
    """
    A class to read USD/CAD exchange rates from a CSV file
    and convert amounts between USD and CAD.
    """

    def __init__(self, filename):
        """
        Initialize the ExchangeRates object with the CSV file name.
        Reads the latest FXAUSDCAD rate (CAD per 1 USD) from the file.
        """
        self.filename = filename
        self.usd_to_cad_rate = None
        self._load_latest_rate()

    def _load_latest_rate(self):
        """
        Read the CSV file using the csv module (encoding utf-8-sig),
        and store the FXAUSDCAD rate from the last row.
        """
        with open(self.filename, mode="r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            last_row = None

            for row in reader: # Iterate through all rows; the last one will be the latest rate
                last_row = row

            if last_row is None:
                raise ValueError("No data rows found in the exchange rate file.")

            self.usd_to_cad_rate = float(last_row["FXAUSDCAD"]) # FXAUSDCAD is Canadian dollars per 1 US dollar

    def convert(self, amount, from_currency, to_currency):
        """
        Convert the given amount between USD and CAD.

        - If from USD to CAD: multiply by the rate.
        - If from CAD to USD: divide by the rate.
        - If same currency: return the amount unchanged.
        """
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency == to_currency: # Same currency: no conversion needed
            return amount

        if from_currency == "USD" and to_currency == "CAD": # USD to CAD: multiply by rate
            return amount * self.usd_to_cad_rate

        if from_currency == "CAD" and to_currency == "USD": # CAD to USD: divide by rate
            return amount / self.usd_to_cad_rate

        raise ValueError("Supported currencies are only USD and CAD.") # If currencies are not USD or CAD, raise an error


if __name__ == "__main__":  # Main block: interact with the user

    rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv") # Create an ExchangeRates object using the Bank of Canada CSV file

    amount_str = input("Enter the amount you want to convert: ").strip() # Ask the user for the amount to convert

    try:
        amount = float(amount_str) # Convert the input string to a float
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        exit(1)

    from_currency = input("Convert FROM (USD or CAD): ").strip().upper() # Ask the user for the currency to convert from (USD or CAD)

    to_currency = input("Convert TO (USD or CAD): ").strip().upper() # Ask the user for the currency to convert to (USD or CAD)

    try:
        result = rates.convert(amount, from_currency, to_currency) # Perform the conversion using the convert method
    except ValueError as e:
        print(f"Error: {e}")  # Handle unsupported currency or other conversion errors
        exit(1)

    formatted_input = f"${amount:,.2f} {from_currency}" # Format the amounts with dollar signs, commas, and 2 decimal places
    formatted_output = f"${result:,.2f} {to_currency}"

    print(f"{formatted_input} = {formatted_output}")  # Print the final result in the required format


def parse_trip(text):
    if not isinstance(text, str) or not text.strip():
        return None

    parts = text.split(':')
    if len(parts) != 2:
        return None

    cab, km = parts

    try:
        km = float(km)
        if not cab.strip() or km <= 0:
            return None
        return cab.strip().title(), km
    except ValueError:
        return None


def fare_average(fares_csv):
    if not isinstance(fares_csv, str) or not fares_csv.strip():
        return None

    try:
        values = [int(r.strip()) for r in fares_csv.split(',')]
        if any(v < 0 for v in values):
            return None
        return sum(values) // len(values)
    except ValueError:
        return None


def payable_fare(text):
    if not isinstance(text, str) or not text.strip():
        return None

    parts = text.split('|')
    if len(parts) != 2:
        return None

    fare, promo = parts

    try:
        fare = float(fare)
        promo = float(promo)

        if fare < 0 or promo < 0:
            return None

        return max(fare * 1.18 - promo, 0)
    except ValueError:
        return None


def main():
    print("==== Running parse_trip ====")
    user_input = input("Enter cab:distance in km (e.g. sedan:12): ")
    result = parse_trip(user_input)
    print("Cab and Distance:", result)

    print("\n==== Running fare_average ====")
    user_input = input("Enter fares as CSV (e.g. 120,95,210): ")
    result = fare_average(user_input)
    print("Average Fare:", result)

    print("\n==== Running payable_fare ====")
    user_input = input("Enter fare|promo (e.g. 250|30): ")
    result = payable_fare(user_input)
    print("Payable Fare:", result)


if __name__ == "__main__":
    main()

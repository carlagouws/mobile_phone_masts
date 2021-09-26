from mobile_phone_masts import MobilePhoneMasts


def get_input():
    print("Please input requirement number to run or type 'all' to run them all")
    requirement = input()
    if requirement not in ['all', '1', '2', '3', '4']:
        print("Invalid input")
        get_input()
    return requirement


def task_1(filename):
    print("First 5 items from a list sorted by “Current Rent” in ascending order:")
    print(MobilePhoneMasts(filename).sorted_by_current_rent()[:6])


def task_2(filename):
    tenants = MobilePhoneMasts(filename)
    tenants_with_25_year_lease = tenants.lease_years_of_25()
    print("List of tenants with 25-year lease:")
    print(tenants_with_25_year_lease)
    print("Total Rent: \n" + f"{tenants.total_rent(tenants.lease_years_of_25())}")


def main():
    filename = "dataset.csv"
    input = get_input()

    if input == 'all':
        task_1(filename)
        print("")
        task_2(filename)
        print("")
    elif input == '1':
        task_1(filename)
    elif input == '2':
        task_2(filename)


main()

from mobile_phone_masts import MobilePhoneMasts
import datetime as dt


def get_input():
    print("Please input task number to run or type 'all' to run them all")
    task = input()
    if task not in ["all", "1", "2", "3", "4"]:
        print("Invalid input")
        get_input()
    return task


def task_1(filename):
    print("First 5 items from a list sorted by “Current Rent” in ascending order:")
    print(MobilePhoneMasts(filename).sorted_by_current_rent()[:6])


def task_2(filename):
    data_list = MobilePhoneMasts(filename)
    tenants_with_25_year_lease = data_list.lease_years_of_25()
    print("List of tenants with 25-year lease:")
    print(tenants_with_25_year_lease)
    print("Total Rent: \n" + f"{data_list.total_rent(data_list.lease_years_of_25())}")


def task_3(filename):
    print("Tenants with number of masts:")
    dict_of_masts = MobilePhoneMasts(filename).count_number_masts_per_tenant()
    for item in dict_of_masts.items():
        print(f"Tenant: {item[0]}, Number of masts: {item[1]}")


def task_4(filename):
    print("Tenants with “Lease Start Date” between 1st June 1999 and 31st August 2007:")
    print(
        MobilePhoneMasts(filename).rentals_lease_start_date_filter(
            dt.date(1999, 6, 1), dt.date(2007, 8, 31)
        )
    )


def main():
    filename = "dataset.csv"
    input = get_input()

    if input == "all":
        task_1(filename)
        print("")
        task_2(filename)
        print("")
        task_3(filename)
        print("")
        task_4(filename)
    elif input == "1":
        task_1(filename)
    elif input == "2":
        task_2(filename)
    elif input == "3":
        task_3(filename)
    else:
        task_4(filename)


main()

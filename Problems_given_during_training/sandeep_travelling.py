def calculate_tour_duration(total_km, speed_kmph, hours_per_day):
    km_per_day = speed_kmph * hours_per_day
    total_days = total_km / km_per_day

    years = int(total_days // 365)
    remaining_days = total_days % 365

    months = int(remaining_days // 30)
    days = int(remaining_days % 30)
    hours = int((remaining_days % 1) * 24)

    print(f"\nTo cover" ,total_km, "km at",speed_kmph,"km/h for",hours_per_day,"hours/day, Sandeep will take:")
    print(years,f"years,",months,"months,",days,"days, and",hours,"hours.")


speed_kmph = float(input("Enter average cycling speed (in km/h): "))
hours_per_day = float(input("Enter how many hours per day Sandeep cycles: "))

total_km = 10000 
calculate_tour_duration(total_km, speed_kmph, hours_per_day)

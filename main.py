import weather

# read the data from the file
input_data = weather.read_data("w.dat")

# generate the report
gather = weather.report_historical(input_data)

# write the report to a file
with open("output.txt", "w") as file:
    file.write(gather)

## Name: David Perera
# Student ID: 884532367
# Section: 07
# Assignment: Module 8 Assignment 2

with open("input.txt", "r") as input_file:
    data_list = input_file.readlines()

with open("output.txt", "w") as output_file:
    print("Here are the user agents:", file=output_file)
    for line in data_list:
        if line.startswith("User-agent:"):
            print(line.strip(), file=output_file)

    print("Here are the sitemaps:", file=output_file)
    for line in data_list:
        if line.startswith("Sitemap:"):
            print(line.strip(), file=output_file)

    print("Here are the crawl delays:", file=output_file)
    for line in data_list:
        if line.startswith("Crawl-Delay:"):
            print(line.strip(), file=output_file)
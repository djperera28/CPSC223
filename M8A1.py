## Name: David Perera
# Student ID: 884532367
# Section: 07
# Assignment: Module 8 Assignment 1

with open("input.txt", "r") as file_object:
    data_list = file_object.readlines()

print("Here are the user agents:")
for line in data_list:
    if line.startswith("User-agent:"):
        print(line.strip())

print("Here are the sitemaps:")
for line in data_list:
    if line.startswith("Sitemap:"):
        print(line.strip())

print("Here are the crawl delays:")
for line in data_list:
    if line.startswith("Crawl-Delay:"):
        print(line.strip())
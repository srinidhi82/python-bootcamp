databases = ["mysql", "oracle", "mongo", "nosql", "bigquery", "postgress"]
print(f"The best database for bigdata is {databases[4].title()}")
databases.append("Redis")
print(databases)
databases.insert(0, "MariaDB")
print(databases)
del databases[3]
databases.remove("bigquery")
print(databases)

name = ["Sam", "San", "John"]
pop_name = name.pop()
print(name)
import csv
from hash import ChainingHashTable


class Package:
    def __init__(self, id, address, city, state, zip_code, deadline, mass, special_notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.mass = mass
        self.special_notes = special_notes

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city, self.state, self.zip_code,
                                                   self.deadline, self.mass, self.special_notes)


def load_package_data(file_name):
    with open(file_name) as packageList:
        package_data = csv.reader(packageList, delimiter=',')
        next(package_data)
        for package in package_data:
            package_id = int(package[0])
            package_address = package[1]
            package_city = package[2]
            package_state = package[3]
            package_zip = package[4]
            package_deadline = package[5]
            package_mass = package[6]
            package_notes = package[7]
            if package_notes == '':
                package_notes = "None"

            package = Package(package_id, package_address, package_city, package_state, package_zip, package_deadline,
                              package_mass, package_notes)

            myHash.insert(package_id, package)


myHash = ChainingHashTable()

load_package_data('Data/WGUPS_Package_File.csv')

for i in range(len(myHash.table) + 1):
    print("Key: {} and Package: {}".format(i + 1, myHash.search(i + 1)))

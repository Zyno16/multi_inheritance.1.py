class otherdata:
    email="example@ac.uk"
    phone = "02211445566"


class employee():
    name = "amr"
    address = "algeria"
    def printdata(self):
        print(self.name + ";" + self.address)

class emp(employee ,otherdata):
    pass

e1 =emp()
print(e1.name)
print("===============")

print(e1.email)
print(e1.phone)

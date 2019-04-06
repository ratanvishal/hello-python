class electronic_device:
    jucier=3
    moblie=12
    fan=7
    telivision=20
class pocket_gadget(electronic_device):
    moblie = 9
    def pocket(self):
        return f"dear you have pocket phones {self.moblie}"
class phone(pocket_gadget):
    moblie = 50
    def phone(self):
        return f"son how many phones u have {self.moblie}"

e=electronic_device()
p=pocket_gadget()
ph=phone()
print(ph.pocket())




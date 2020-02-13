#initializes a class of bacteria
class bacteria:
	def __init__(self):
		self.organismType = "Prokaryotic"
        #sets the microorganism type as prokarotic
	def printName(self):
		print("Bacteria are microorganisms of the type " + self.organismType)
        #method that will print out the type of microorganism bacteria are
	
#initalizing an object of chlamydia that inherits the class of bacteria
class chlamydia(bacteria):
    def __init__(self,speciesName, aminoAcidLength, seqSample):
        #the information it holds is the species name, the length of the amino acid, and the sequence sample
        super().__init__()
        self.speciesName = speciesName
        self.aminoAcidLength = aminoAcidLength
        self.seqSample = seqSample
    def printInfo(self):
        print(self.speciesName + " has an amino acid length of " + str(self.aminoAcidLength) + " and a sequence sample of " + self.seqSample)
        #Prints all the information about that particular chlamydia
        
objOne = chlamydia("C.trachomatis", 200, "G1000")
objTwo = chlamydia("C.trachomatis D", 1042519	, "h")
objThree = chlamydia("C.pneumoniae AR39", 1229853, "h")
objFour = chlamydia("C.pneumoniae CWL029", 1230230, "h")
objFive = chlamydia("one more, idk ask ethan", 25, "h")
#creating 5 different chlamydia objects, pass in the name of the chlamydia, the length of the amino acid length, and the sequence sample

#this is the examples on how to access attributes of the object
print("Object Three is the species of " + objThree.speciesName)
print("Object Four has an amino acid length of " + str(objFour.aminoAcidLength))
print("Object Five has a sequence sample of " + objFive.seqSample)

#this is the examples on how to invoke methods
objOne.printName()
objTwo.printInfo()

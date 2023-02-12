drug_interactions = []

with open("drug_interactions.txt", "r") as file:
    for line in file:
        line = line.strip().split(":")
        if len(line) >= 2:
            drug = line[0].strip()
            interacting_drugs = [d.strip() for d in line[1].split(",")]
            drug_interactions.append((drug, interacting_drugs))

prescription = input("Enter your prescription (separated by commas): ")
prescription = [d.strip() for d in prescription.split(",")]

for drug, interacting_drugs in drug_interactions:
    if drug in prescription:
        for interacting_drug in interacting_drugs:
            if interacting_drug in prescription:
                print("Drug interaction found between {} and {}".format(drug, interacting_drug))

print("No drug interactions found.")

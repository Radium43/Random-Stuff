class IQCalculator:
    def __init__(self, species):
        self.species = species
        self.neuron_density_weight = 0.5
        self.brain_density_weight = 0.5

    def calculate_iq(self, neuron_density, brain_density):
        weighted_density = (
            self.neuron_density_weight * neuron_density +
            self.brain_density_weight * brain_density
        )
        iq = (weighted_density * 100) / 2
        return iq

def get_user_input():
    try:
        neuron_density = float(input("Enter neuron density: "))
        brain_density = float(input("Enter brain density: "))
        return neuron_density, brain_density
    except ValueError:
        print("Please enter valid numeric values.")
        return get_user_input()

def main():
    print("IQ Calculator")
    print("===============")
    species = "human"
    calculator = IQCalculator(species)
    neuron_density, brain_density = get_user_input()
    result = calculator.calculate_iq(neuron_density, brain_density)
    print(f"calculated IQ for {species} is: {result}")

if __name__ == "__main__":
    main()


'''
Thanks to one of my friends for some help on this hes good at this shit
'''
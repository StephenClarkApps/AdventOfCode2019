
# First sight solution

# PART ONE
class Solution:
    def findRequirementsForMass(self, the_mass):
        module_mass = int(the_mass)
        dividedByThree = module_mass / 3
        rounded_minus_two = int(dividedByThree) - 2
        return rounded_minus_two

    def findSolution(self, inputfile):
        total_fuel_requirements = 0
        for line in open(inputfile):
            total_fuel_requirements = total_fuel_requirements + Solution().findRequirementsForMass(line.strip())
        return int(total_fuel_requirements)

print("Day One Part One Solution: %d" % (Solution().findSolution('input.txt')))

# PART TWO
# My initial thoughts on this were that it sounded recursive, so thought this was the first
# approach. Took me longer to try it that way than I thought so I went with something more basic.

class SolutionPartTwo:
    def findRequirementsForMass(self, the_mass):
        module_mass = int(the_mass)
        dividedByThree = module_mass / 3
        rounded_minus_two = int(dividedByThree) - 2
        return rounded_minus_two

    def findSolution(self, inputfile):
        total_fuel_requirements = 0
        remaining = 0
        for line in open(inputfile):
            remaining = Solution().findRequirementsForMass(line.strip())
            while remaining > 0: # This bit kinda stands in for recursive calls to a function
                total_fuel_requirements = total_fuel_requirements + remaining
                remaining = Solution().findRequirementsForMass(remaining)
        return int(total_fuel_requirements)

print("Day One Part Two Solution: %d" % (SolutionPartTwo().findSolution('input.txt')))

# Find the frequency of each element in a list

input_values = input("Enter elements separated by spaces: ").split()

processed_elements = []

for element in input_values:
    if element not in processed_elements:
        frequency = 0

        for current_element in input_values:
            if current_element == element:
                frequency += 1

        print(element, ":", frequency)
        processed_elements.append(element)

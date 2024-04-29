import math


def bonding(argument_one, argument_two):
    list_of_args = [argument_one, argument_two]
    metal = argument_one
    non_metal = argument_two
    if metal.valency == 0 or non_metal.valency == 0:
        return "Group zero elements don't bond!"
    else:
        divisor = math.gcd(metal.valency, non_metal.valency)
        if non_metal.is_polyatomic and metal.valency / divisor != 1 and non_metal.valency / divisor != 1:
            return (metal.chemical_symbol + get_sub(
                str(int(non_metal.valency / divisor))) + "(" + non_metal.
                    chemical_symbol + ")" + get_sub(str(int(metal.valency / divisor))))
        elif non_metal.valency / divisor == 1 and metal.valency / divisor == 1:
            return (metal.chemical_symbol + get_sub(str(int(non_metal.valency / divisor))) + non_metal.
                    chemical_symbol + get_sub(str(int(metal.valency / divisor))))
        else:
            return (metal.chemical_symbol + get_sub(str(int(non_metal.valency / divisor))) + non_metal.
                    chemical_symbol + get_sub(str(int(metal.valency / divisor))))


class Element:

    def __init__(self, name, valency, chemical_symbol, metallic_character):
        self.name = name
        self.valency = valency
        self.chemical_symbol = chemical_symbol
        self.metallic_character = metallic_character
        self.is_polyatomic = False

    def __repr__(self):
        return self.name


class Radical(Element):

    def __init__(self, name, valency, chemical_symbol, is_polyatomic):
        super().__init__(name, valency, chemical_symbol, "non-Metal")
        self.is_polyatomic = is_polyatomic
        self.metallic_character = "non-Metal"


# function to convert to subscript
def get_sub(x, reverse=False):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans(''.join(normal), ''.join(sub_s), "1")
    anti_res = x.maketrans(''.join(sub_s), ''.join(normal), "1")
    if reverse:
        return x.translate(anti_res)
    else:
        return x.translate(res)


# function to convert to superscript
def get_super(x, reverse=False):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s), "1")
    anti_res = x.maketrans(''.join(super_s), ''.join(normal), "1")
    if reverse:
        return x.translate(anti_res)
    else:
        return x.translate(res)


Hydrogen = Element("Hydrogen", 1, "H", "Metal")
Helium = Element("Helium", 0, "He", "non-Metal")
Lithium = Element("Lithium", 1, "Li", "Metal")
Beryllium = Element("Beryllium", 2, "Be", "Metal")
Boron = Element("Boron", 3, "B", "Metalloid")
Carbon = Element("Carbon", 4, "C", "non-Metal")
Nitrogen = Element("Nitrogen", 3, "N", "non-Metal")
Oxygen = Element("Oxygen", 2, "O", "non-Metal")
Fluorine = Element("Fluorine", 1, "F", "non-Metal")
Neon = Element("Neon", 0, "Ne", "non-Metal")
Sodium = Element("Sodium", 1, "Na", "Metal")
Magnesium = Element("Magnesium", 2, "Mg", "Metal")
Aluminium = Element("Aluminium", 3, "Al", "Metalloid")
Silicon = Element("Silicon", 4, "Si", "Metalloid")
Phosphorus = Element("Phosphorus", 3, "Pa", "non-Metal")
Sulphur = Element("Sulphur", 2, "S", "non-Metal")
Chlorine = Element("Chlorine", 1, "Cl", "non-Metal")
Argon = Element("Argon", 0, "Ar", "non-Metal")
Potassium = Element("Potassium", 1, "K", "Metal")
Calcium = Element("Calcium", 2, "Ca", "Metal")
Nitrate = Radical("Nitrate", 1, f"NO{get_sub("3")}", True)
Carbonate = Radical("Carbonate", 2, f"CO{get_sub("3")}", True)
Chlorate = Radical("Chlorate", 2, f"ClO{get_sub("3")}", True)
Oxide = Radical("Oxide", 2, f"0{get_sub("2")}", False)
Phosphate = Radical("Phosphate", 3, f"PO{get_sub("3")}", True)
Sulphate = Radical("Sulphate", 2, f"SO{get_sub("4")}", True)

list_of_elements = [Hydrogen, Helium, Lithium, Beryllium, Boron, Carbon, Nitrogen, Oxygen, Fluorine, Neon, Sodium,
                    Magnesium, Aluminium, Silicon, Phosphorus, Sulphur, Chlorine, Argon, Potassium, Calcium]
list_of_radicals = [Nitrate, Carbonate, Chlorate, Oxide, Phosphate, Sulphate]
strings_of_elements = [element.name for element in list_of_elements]
strings_of_radicals = [radical.name for radical in list_of_radicals]
dictionary_of_elements = {strings_of_elements[x]: list_of_elements[x] for x in range(len(list_of_elements))}
dictionary_of_radicals = {strings_of_radicals[x]: list_of_radicals[x] for x in range(len(list_of_radicals))}
dictionary_of_stuff = dictionary_of_elements | dictionary_of_radicals


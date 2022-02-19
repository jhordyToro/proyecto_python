def main():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"name": "jhordy", "first_name": "toro"}

    super_dict = {
        "num1": ["Hello", True, 4.5],
        "num2": [1, "Hello", True],
        "num3": [1, "Hello", 4.5],
        "num4": [1, True, 4.5],
    }
    super_list = [
        {"name": "jhordy", "first_name": "toro"},
        {"name": "jhordy", "first_name": "toro"},
        {"name": "jhordy", "first_name": "toro"},
        {"name": "jhordy", "first_name": "toro"},
    ]

    for i, b in super_dict.items():
        print(i, " ", b)

    for valor in super_list:
        print(valor)
    
if __name__ == "__main__":
    main()
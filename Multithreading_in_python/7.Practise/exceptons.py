from concurrent.futures import ThreadPoolExecutor

from itertools import product

elements = ["#fW", "^1a", "!b2", "l(3", "`#5R", "e%1", "3Ff", "=b1", "vF^", "-F0"]

def compare_element(element):
    reference_element = 'vF^=b1!b2'
    if element == reference_element:
        return f"Элемент совпал = {element}"
    else:
        raise ValueError(f"Элемент {element} не совпадает с эталоном.")


def generate_cartesian_product(element_1, element_2, element_3):
    res = element_1 + element_2 + element_3
    result = compare_element(res)
    return result



with ThreadPoolExecutor(max_workers=10) as executor:
    futures = []
    for element_1 in elements:
        for element_2 in elements:
            for element_3 in elements:
                future = executor.submit(generate_cartesian_product,
                                         element_1,
                                         element_2,
                                         element_3)
                futures.append(future)
    
    for future in futures:
        try:
            future = future.result()
            print(future)
        except ValueError as e:
            print(e)

def thirdlargest(array):
    n = len(array)
    
    array.sort()
    
    return [n-3]

if __name__ == "__main__":
    array = [1, 14, 2, 16, 10, 20]
    print(thirdlargest(array))
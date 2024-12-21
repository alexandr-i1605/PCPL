data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
def abs_key(x):
        return abs(x)

if __name__ == '__main__':
    result = sorted(data, key=abs_key, reverse=True)
    print(result)

    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print(result_with_lambda)

    
    
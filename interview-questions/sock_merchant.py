def sockMerchant(n, ar):
    pairs = 0
    ar.sort()
    ar.append('#')
    i = 0
    while i<n:
        if ar[i]==ar[i+1]:
            pairs+=1
            i+=2
        else:
            i+=1
    return pairs

def main():
    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    print(sockMerchant(n,ar))

if __name__ == "__main__":
    main()
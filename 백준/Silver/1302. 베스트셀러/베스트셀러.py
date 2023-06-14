def best_seller(book_list):
    best_check = {}
    
    for book in book_list:
        if book not in best_check.keys():
            best_check[book] = 1
        else:
            best_check[book] += 1
            
    best_sell_num = max(best_check.values())
    
    best_list = [sell_book[0] for sell_book in best_check.items() if sell_book[1] == best_sell_num]
    
    return sorted(best_list)[0]

if __name__ == "__main__":
    book_list = []
    for _ in range(int(input())):
        book = input()
        book_list.append(book)
        
    best_seller = best_seller(book_list)
    
    print(best_seller)
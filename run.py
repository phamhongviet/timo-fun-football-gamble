import os

player_list = '''Alan Barker
Nguyen Thi Nguyet Que
Tran Ngoc Anh Tuyet
Nguyen Xuan Hieu
Ta Thi Phuong Loan
Nguyen Thi My Linh
Bui Van Loc
Truong Vo Thien Nhon
Nguyen Thanh Tien
Bui Le Tien Khanh
Nguyen Thanh Phuoc
Nguyen Quoc Hung
Vo Van Tri
Le Quang Chau Tri
Mai Quoc Vuong
Pham Hong Viet
Pham Tran Duy
Le Quoc Hung
Nguyen Thi Hoang Nhung
Tran Thien Thanh'''.split('\n')

player_number = len(player_list)

random_list = [ i%2 for i in map(ord, str(os.urandom(player_number)))]

r=0
list_0 = []
list_1 = []
for p in player_list:
    if len(list_0) >= player_number // 2:
        list_1.append(p)
    elif len(list_1) >= player_number // 2:
        list_0.append(p)
    elif random_list[r] == 0:
        list_0.append(p)
    elif random_list[r] == 1:
        list_1.append(p)
    else:
#       na ni ?!
        pass
    r += 1

print("VIET NAM:")
for i in list_0:
    print("\t{}".format(i))
print("Not VIET NAM:")
for i in list_1:
    print("\t{}".format(i))

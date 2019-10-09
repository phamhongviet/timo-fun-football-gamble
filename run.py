import random

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

random.shuffle(player_list)

n = len(player_list)//2

print("VIET NAM:")
for i in player_list[:n]:
    print("\t{}".format(i))
print("Not VIET NAM:")
for i in player_list[n:]:
    print("\t{}".format(i))

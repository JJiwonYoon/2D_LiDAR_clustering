data = [150.9999930858612, 150.9999930858612, 149.00000393390656, 149.00000393390656, 149.00000393390656, 148.00000190734863, 146.9999998807907, 145.9999978542328, 144.99999582767487, 143.00000667572021, 143.00000667572024, 143.00000667572021, 143.0000066757202, 143.00000667572024, 142.0000046491623, 142.00000464916232, 142.00000464916226, 143.0000066757202, 187.00000643730164, 187.00000643730164, 187.00000643730164, 185.00000238418576, 185.0000023841858, 180.9999942779541, 178.00000309944153, 178.00000309944153, 178.00000309944153, 177.0000010728836, 173.99999499320987, 173.99999499320987, 173.99999499320984]

# 리스트를 두 개씩 나누는 함수
def split_into_pairs(lst):
    pairs = [lst[i:i+2] for i in range(0, len(lst) - 1, 2)]
    if len(lst) % 2 == 1:
        pairs[-1:1].append([lst[-1]])
    return pairs

pairs = split_into_pairs(data)
print(pairs)
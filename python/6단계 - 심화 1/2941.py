Croatia_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
st = input()

for alphabet in Croatia_list:
    st = st.replace(alphabet, '@')
print(len(st))
def solve(st , k ):
    s = st
    for c in 'abcdefghijklmnopqrstuvwxyz':
        count = st.count(c)
        if st.count(c) >= k:

            s = s.replace(c, '', k)

            break

        else:

            k -= st.count(c)
            st = st.replace(c, "", st.count(c))

        return


print(solve(['abracadabra', 1]))
        if D:
            if Flag:
                if D == 3:
                    mstr += 'DM'
                    Flag = True
            else:
                if D == 4:
                    mstr += 'DM'
                    Flag = True
                else:
                    for i in range(D):
                        mstr += 'D'
                        Flag = False
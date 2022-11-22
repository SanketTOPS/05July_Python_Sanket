class student:
    __stid=12
    __stnm='Nirav'

    def __getdata(self):
        #print("This is getdata")
        print("Student ID:",self.__stid)
        print("Student Name:",self.__stnm)
    
    def stdata(self):
        self.__getdata()


st=student()
#print(st.stid)
#print(st.stnm)
#st.getdata()
st.stdata()
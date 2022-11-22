class student:
    def getdata(self,id,name):
        print("Student ID:",id)
        print("Student Name:",name)

class otherstudent(student):
    def getdata(self, id, name):
        return super().getdata(id, name)

st=student()
st.getdata(1,'Sanket')

ot=otherstudent()
ot.getdata(2,'NIrav')
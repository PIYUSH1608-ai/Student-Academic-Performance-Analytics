from flask import Flask, render_template, request, send_file, redirect
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

Professors = "database/Professors.csv"
Registered_Students = "database/Registered_students.csv"
app = Flask(__name__)
All_Prof=["MahavirSharma@iitbhilai.ac.in","AvijitPal@iitbhilai.ac.in","GaganRaj@iitbhilai.ac.in"]
total_scoring_area=["Project","Assignment","Midsem","Endsem"]
@app.route('/')
def home():
    return render_template('first_page.html')

def generate_attendance_chart(df, teacher_name):
    """Generates and saves the attendance bar chart for a teacher's students."""
    print(df)
    name = df["Name"].tolist()
    attendance = df["Attendance"].tolist()

    plt.bar(name, attendance, color='blue', width=0.4)
    plt.title("Student Attendance")
    plt.xlabel("Students")
    plt.ylabel("Present Days")

    chart_path = f"static/charts/{teacher_name}_attendance.png"
    plt.savefig(chart_path)
    plt.close()
    return f"/{chart_path}"

def generate_TotalMarks_chart(df, teacher_name):
    """Generates and saves the totalmarks bar chart for a teacher's students."""
    students=df.to_dict(orient="records")
    TotalMarks=[]
    for i in students:
        total=0
        for j in total_scoring_area:
            try:
                total += int(i[j])
            except (ValueError, TypeError):
                total += 0
        TotalMarks.append(total)
    name = df["Name"].tolist()

    plt.bar(name, TotalMarks, color='blue', width=0.4)
    plt.title("Student TotalMarks")
    plt.xlabel("Students")
    plt.ylabel("Total Marks")

    chart_path = f"static/charts/{teacher_name}_totalmarks.png"
    plt.savefig(chart_path)
    plt.close()
    return f"/{chart_path}"

@app.route('/sign_in_prof')# this route handles the sign in page of Professor
def sign_in_page1():
    return render_template('sign_in_prof.html')


@app.route('/signin_prof', methods=['post'])#this route handles the inputs of signin of Professor
def Prof_login():
    email = request.form['email']
    Teacher_name=email[0:email.index("@")]
    password = request.form['password']
    df_ = pd.read_csv(Professors)
    row_ = df_[df_["Email"]==email]
    if(row_.empty):
        return redirect('/sign_in_prof')
    req_row = row_.iloc[0].to_dict()
    if(req_row['Password']!=password):
        return redirect('/sign_in_prof')
    csv_path = f"database/{email}.csv"
    if not os.path.exists(csv_path):
        return f"No data found for {email}"

    df = pd.read_csv(csv_path)
    students = df.to_dict(orient='records')

    chart_path1=generate_attendance_chart(df,Teacher_name)
    chart_path2=generate_TotalMarks_chart(df,Teacher_name)
    return render_template('teacher_dashboard.html', teacher=Teacher_name, email=email,students=students, chart1=chart_path1,chart2=chart_path2)



@app.route('/sign_in_student')# this route handles the sign in page of student
def sign_in_page2():
    return render_template('sign_in_student.html')

@app.route('/signin_student', methods=['post'])#this route handles the inputs of signin of student
def Student_login():
    email = request.form['email']
    Roll=int(request.form['Roll'])
    password = request.form['password']

    df_ = pd.read_csv(Registered_Students)
    row_ = df_[df_["Roll"] == Roll]
    if(row_.empty):
        return redirect('/sign_in_student')
    req_row = row_.iloc[0].to_dict()
    if(req_row['Password']!=password or req_row['Email']!=email):
        return redirect('/sign_in_student')
    Total_Marks=[]
    Subjects=["Physics","Maths","CSL"]
    Complete_data={}
    Name=None

    for i in range(0,len(All_Prof)):
        df = pd.read_csv(f"database/{All_Prof[i]}.csv")
        row = df[df["Roll"] == Roll]
        if row.empty:
            continue
        row_dict = row.iloc[0].to_dict()

        Name=row_dict["Name"]
        sum=0
        dict={}
        for j in row_dict:
            if j in total_scoring_area:
                sum+=row_dict[j]
                dict[j]=int(row_dict[j])
        Complete_data[Subjects[i]]=dict
        Total_Marks.append(sum)
    plt.bar(Subjects, Total_Marks, color='blue', width=0.8)
    plt.title("Subject TotalMarks")
    plt.xlabel("Subjects")
    plt.ylabel("Total Marks")

    chart_path = f"static/charts/{Roll}_totalmarks.png"
    plt.savefig(chart_path)
    plt.close()
    print(Complete_data)
    return render_template('student_dashboard.html',Name=Name, email=email,Complete_data=Complete_data, chart=chart_path)


@app.route('/student/<email>/<int:roll>/data_updation')#this is the route for data updation page
def Open_data_updation_page(email,roll):
    return render_template('data_updation.html',email=email,roll=roll)

@app.route('/student/<email>/<int:roll>',methods=['post'])
def Data_updation(email,roll):
    csv_path = f"database/{email}.csv"
    Teacher_name=email[0:email.index('@')]
    df = pd.read_csv(csv_path)
    df.loc[df["Roll"] == roll, "Project"] = request.form['Project']
    df.loc[df["Roll"] == roll, "Assignment"] = request.form['Assignment']
    df.loc[df["Roll"] == roll, "Midsem"] = request.form['Midsem']
    df.loc[df["Roll"] == roll, "Endsem"] = request.form['Endsem']
    df.loc[df["Roll"] == roll, "Attendance"] = request.form['Attendance']
    df.to_csv(csv_path, index=False)
    students = df.to_dict(orient='records')
    chart_path1=generate_attendance_chart(df,Teacher_name)
    chart_path2=generate_TotalMarks_chart(df,Teacher_name)
    return render_template('teacher_dashboard.html', teacher=Teacher_name, email=email,students=students, chart1=chart_path1,chart2=chart_path2)

if __name__ == "__main__":
    app.run(debug=True)
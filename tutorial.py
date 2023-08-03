
from flask import Flask, redirect, render_template, url_for


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/companies")
def companies():
    return render_template("companies.html")


@app.route("/aboutus")
def aboutus():
    return render_template("about us.html")


@app.route("/resumebuilder")
def resumebuilder():
    return render_template("resumebuilder.html")


@app.route("/sampleresume")
def sampleresume():
    return render_template("sampleresume.html")


@app.route("/sign-in student")
def signinstudent():
    return render_template("signin student.html")


@app.route("/sign-in recruiter")
def signinrecruiter():
    return render_template("signin recruiter.html")


@app.route("/sign-up student")
def signupstudent():
    return render_template("signup student.html")


@app.route("/sign-up recruiter")
def signuprecruiter():
    return render_template("signup recruiter.html")


@app.route("/student profile")
def studentprofile():
    return render_template("student profile.html")


@app.route("/recruiter profile")
def recruiterprofile():
    return render_template("recruiter profile.html")


@app.route("/student editprofile")
def studenteditprofile():
    return render_template("student editprofile.html")


@app.route("/upload resume")
def uploadresume():
    return render_template("upload resume.html")


@app.route("/apply for job")
def applyforjob():
    return render_template("apply for job.html")


@app.route("/student past applications")
def studentpastapplications():
    return render_template("student past applications.html")


@app.route("/recruiter edit profile")
def recruitereditprofile():
    return render_template("recruiter edit profile.html")


@app.route("/recruiter job applications")
def recruiterjobapplications():
    return render_template("recruiter job applications.html")


@app.route("/recruiter send approval")
def recruitersendapproval():
    return render_template("recruiter send approval.html")


@app.route("/recruiter past approval")
def recruiterpastapproval():
    return render_template("recruiter past approval.html")


if __name__ == "__main__":
    app.run(debug=True)

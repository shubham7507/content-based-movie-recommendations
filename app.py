from flask import Flask, render_template,request
from forms import SignUpForm
from ml import  rcmd
app = Flask(__name__)
app.config['SECRET_KEY'] = 'thecodex'



#@app.route('/')
#def home():
 #   return render_template('base.html')





@app.route('/base')
def base():
    return render_template('base.html')



@app.route('/',methods=['GET','POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        re = request.form['moviename']
        print(re)

        posts = rcmd(re)
        ll = len(posts)
        return render_template('user.html', posts = posts,re = re,ll=ll)
        #return render_template('user.html',result=result)

    return render_template('signup.html', form=form)



if __name__ == "__main__":
    app.run(debug=True)
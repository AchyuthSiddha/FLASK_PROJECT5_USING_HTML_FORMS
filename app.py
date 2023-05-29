from flask import Flask,render_template,request

FAI=Flask(__name__)


@FAI.route('/Data',methods=['GET','POST'])
def Data():
    if request.method=='POST':
        form_data=request.form
        print(form_data)
        return form_data['ln']
        # return 'data submitted sucesfully:'
    return render_template('Data.html')

if __name__=='__main__':
    FAI.run(debug=True)
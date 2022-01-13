from flask import Flask,request, jsonify
app=Flask(__name__)
tasks=[
    {
        'id':1,
        'Name':u'Tamanash',
        'Contact':u'do homework',
        'done':False
    },
    {
        'id':2,
        'Name':u'Tojo',
        'Contact':u'do homework',
        'done':False
    }
]
@app.route('/',methods=['GET','POST'])
def index():
    return "Hello World!"
@app.route('/get-data') 
def get_data():
    return jsonify({'data':tasks})
@app.route('/post-data',methods=['POST'])   #post-data
def post_data():
  if not request.json:
    return jsonify({'error':'no data','status':400,'message':'provide json'})

  task={
    'id':tasks[-1]['id']+1,
    'Name':request.json['Name'],
    'Contact':request.json.get('Contact',""),
    'done':False
  }
  tasks.append(task)
  return jsonify({
    'status':200,
    'message':'success'
    })

if __name__=='__main__':
    app.run(debug=True)




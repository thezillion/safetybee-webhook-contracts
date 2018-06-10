from flask import Flask,request
import json
import sys
app = Flask(__name__)
app.config['SECRET_KEY'] = '223234455'

@app.route('/', methods=['GET'])
def mainRoute():
    return 'hello, world'

@app.route('/',methods=['POST'])
def send_recieve():
   flag = False
    # return 'hello'
   if request.method=='POST':
      try:
         data = request.get_json(silent=True, force=True)
         try:
            action = data.get('queryResult').get('action')
            text = data.get('originalDetectIntentRequest').get('payload').get('inputs')[0].get('arguments')[0].get('rawText')

            if text.find("save") != -1:
               flag = True

            if action == "save" or flag == True:
               # return json.dumps({"fulfillmentText": "We will save you."})
               # return json.dumps({ "intent": "actions.intent.PLACE", "inputValueData": { "@type": "type.googleapis.com/google.actions.v2.PlaceValueSpec", "dialog_spec": { "extension": { "@type": "type.googleapis.com/google.actions.v2.PlaceValueSpec.PlaceDialogSpec", "requestPrompt": "What is your location?", "permissionContext": "To locate a helper" } } } })
               return json.dumps({"fullfillmentText": "Help is on the way! "})
            elif action == "input.welcome":
               return json.dumps({"fulfillmentText": "Welcome to Safety Bee!"})

         except AttributeError:
            return json.dumps({"fulfillmentText": "An error occured."})
      except (ValueError,TypeError,KeyError):
         print("Error caught")
          #send response something is wrong
          #return json.dumps(control)
   else:
      return 'false'

def log(message):
   if message:
      print(str(message))
      sys.stdout.flush()
   else:
      print("Undefined")
      sys.stdout.flush()
#port_=int(sys.argv[1])

def store_blockchain_request(request):
   unicorns = w3.eth.contract(address=w3.getChecksum('0x88c37f6d84c5213fe209dd9d082ca4fa67aa729b'), abi=EIP20_ABI)
   unicorn_txn = unicorns.functions.transfer(
     '0xfB6916095ca1df60bB79Ce92cE3Ea74c37c5d359',
     1,
 ).buildTransaction({
     'chainId': 1,
     'gas': 70000,
     'gasPrice': w3.toWei('1', 'gwei'),
     'nonce': nonce,
 })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
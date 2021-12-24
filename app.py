from flask import Flask # SolBy: Bereket Siraw || Date: 12/16/2021 4 more Info:TG->@thunder_is_taken 
app = Flask(__name__)
@app.route('/')
def route():
   return '<script>setInterval(()=>{with(Math){let e=new Date("Jan 1, 2022 23:36:51").getTime()-(new Date().getTime()),t=floor(e/864e5),o=floor(e%864e5/36e5),n=floor(e%36e5/6e4),a=floor(e%6e4/1e3);document.documentElement.innerHTML=t+" dys "+o+" hrs "+n+" mints "+a+" scds";}},1e3);</script>'
app.run(None,80)

from flask import Flask, request, Response, stream_with_context, render_template
from streamer import Streamer

app = Flask( __name__ )
streamer = Streamer()

@app.route('/')
def main():
    return render_template("index.html", data='전달데이터')

@app.route('/stream')
def stream():
    src = request.args.get( 'src', default = 0, type = int )
    try :
        return Response(
                                stream_with_context( stream_gen( src ) ),
                                mimetype='multipart/x-mixed-replace; boundary=frame' )
    except Exception as e :
        print('[wandlab] ', 'stream error : ',str(e))

def stream_gen( src ):   
    try : 
        streamer.run( src )
        while True :
            frame = streamer.bytescode()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')         
    except GeneratorExit :
        streamer.stop()

app.run( host='0.0.0.0', port=5000 )
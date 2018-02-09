import face_recognition
import picamera
import numpy as np
from flask import Flask, jsonify, request, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/on_load')
def on_load():

    # Get a reference to the Raspberry Pi camera.
    # If this fails, make sure you have a camera connected to the RPi and that you
    # enabled your camera in raspi-config and rebooted first.
    camera = picamera.PiCamera()
    camera.resolution = (320, 240)
    output = np.empty((240, 320, 3), dtype=np.uint8)

    # Get and encode known images
    #me = face_recognition.load_image_file("../test-images/matt-1.jpg")
    #me_encoding = face_recognition.face_encodings(me)[0]

    known_face_encodings = []

    matt1_encoding = np.array([-7.62386397e-02, 3.01904138e-03, -2.38237213e-02, -5.60772009e-02,
     -8.77503380e-02,  3.29113789e-02, -5.91115952e-02, -1.35576516e-01,
      1.77747339e-01, -4.71483767e-02, 1.53783932e-01, -4.02787291e-02,
     -2.59692281e-01, -1.16651133e-01, 4.36959602e-02, 5.17890081e-02,
     -1.11357808e-01, -9.79429781e-02, -6.68500215e-02, -6.63109869e-02,
      2.59716548e-02,  5.23214266e-02, 5.82300313e-02, 4.12139855e-02,
     -1.22904457e-01, -3.29092592e-01, -1.35069624e-01, -2.05371961e-01,
      6.08246922e-02, -5.57530746e-02, 2.32655518e-02, 5.90997934e-02,
     -1.47523180e-01, -5.32861054e-02, 6.31168112e-02, 3.03123780e-02,
     -7.61529654e-02, -7.93362185e-02, 1.77059799e-01, -4.45145331e-02,
     -1.70076221e-01, -1.13955051e-01, 5.38403988e-02, 1.50000006e-01,
      1.59394413e-01,  5.75799383e-02, -1.53327361e-02, -7.95690119e-02,
      1.89084098e-01, -2.06442505e-01, 1.01871505e-01, 1.27010211e-01,
      2.82372087e-01, 5.64930514e-02, 1.50766015e-01, -1.28655583e-01,
      1.20605774e-01, 1.35679498e-01, -3.39231938e-01, 8.73107761e-02,
     -2.52260081e-03, -8.67664516e-02, -4.01429366e-03, 8.34699254e-03,
      2.03773916e-01, 1.30174741e-01, -6.89220056e-02, -1.67036444e-01,
      2.12155238e-01, -1.87735051e-01, -3.92972007e-02, 1.87190309e-01,
     -9.88179967e-02, -2.33143762e-01, -2.66150951e-01, -5.97811416e-02,
      3.69145930e-01, 1.51237547e-01, -1.75035641e-01, -1.48803517e-02,
     -7.94725865e-02, -1.01132117e-01, 4.81006131e-03, 4.05841023e-02,
     -1.03973173e-01, -1.11971922e-01, -6.84380755e-02, -5.84585369e-02,
      2.19163150e-01, -6.73950315e-02, -2.84745470e-02, 2.53344089e-01,
      1.00616096e-02, 3.80974412e-02, -4.52668406e-03, -6.36894489e-03,
     -7.18271434e-02, 7.44583085e-05, -1.03249531e-02, -2.80063786e-02,
      7.96435773e-03, -7.81379864e-02, 2.19520405e-02, 7.27147982e-02,
     -2.23828897e-01, 1.73344612e-01, 8.77884449e-04, -4.52344492e-02,
     -4.88692382e-03, -1.00253820e-01, -8.83731544e-02, -9.03083943e-03,
      1.98479578e-01, -3.58494580e-01, 1.87033236e-01, 1.05240174e-01,
      6.79169968e-02, 1.56795323e-01, -6.83606043e-02, 3.62067968e-02,
      7.23584695e-03, -1.32431507e-01, -2.11615205e-01, -8.07123259e-02,
      9.09725055e-02, -1.04741022e-01, -4.44041304e-02, 3.49725410e-02])

    biff_encoding = np.array([-7.36408681e-02, 3.57491300e-02, 2.91869566e-02, -4.50636521e-02,
     -6.47970811e-02, -2.08379682e-02, -2.27804519e-02, -4.02003340e-02,
      1.71529874e-01, -7.65034556e-02, 2.02388600e-01, -2.64601167e-02,
     -2.41155893e-01, 1.87889040e-02, -1.90105885e-02, 7.92029202e-02,
     -1.57083169e-01, -1.35717660e-01, -7.77554885e-02, -1.27099618e-01,
      1.29973352e-01, 7.07553402e-02, -5.67677878e-02, 3.41767333e-02,
     -2.04145253e-01, -2.74056375e-01, -1.07524797e-01, -1.79965809e-01,
      8.67966861e-02, -1.75399318e-01, 3.86188738e-02, -3.42885144e-02,
     -1.55868366e-01, -8.44979510e-02, 7.49962628e-02, 6.91338554e-02,
     -8.67691860e-02, -1.63659751e-01, 2.21971780e-01, -2.26073470e-02,
     -8.71847570e-02, 3.94672379e-02, 2.63878182e-02, 2.82875687e-01,
      8.06631818e-02, -8.36660899e-03, 4.37428504e-02, -1.67340681e-01,
      1.09604813e-01, -2.01630875e-01, 1.19248636e-01, 1.83809578e-01,
      1.89404413e-01, 1.66012913e-01, 1.49254918e-01, -1.63782865e-01,
      1.23227693e-01, 1.33142620e-01, -2.56956875e-01, 9.58035737e-02,
      1.02503553e-01, 4.10075448e-02, 2.63118930e-03, -5.51892631e-02,
      1.37997314e-01, 1.93285327e-02, -9.81142744e-02, -1.05889723e-01,
      1.73406169e-01, -1.04052700e-01, -6.12791702e-02, 5.97365461e-02,
     -1.20549999e-01, -2.37331778e-01, -1.89886957e-01, 2.90721171e-02,
      4.01251584e-01, 2.12867677e-01, -2.40168393e-01, 6.36014044e-02,
     -9.81972143e-02, -3.39517929e-02, 7.51983821e-02, 3.20168538e-03,
     -6.92419186e-02, -2.92676054e-02, -5.06228022e-02, 1.30953729e-01,
      1.39936820e-01, -3.44561413e-04, -2.25861836e-02, 1.58620775e-01,
      5.27134649e-02, -3.57398316e-02, 8.79117474e-02, 2.70466115e-02,
     -1.44140676e-01, 4.95377742e-03, -6.79346696e-02, -1.19591784e-02,
      5.68141863e-02, -7.25159422e-02, -1.33135449e-03, 1.20137975e-01,
     -1.84900731e-01, 2.40456685e-01, 3.73136103e-02, -8.66190642e-02,
     -4.27760556e-02, 2.39466224e-02, -1.24067023e-01, 3.41273807e-02,
      1.83868155e-01, -3.19298536e-01, 2.07869142e-01, 1.62098050e-01,
      1.64152291e-02, 1.66810393e-01, -6.01127464e-03, 6.26178384e-02,
     -1.96827985e-02, -6.33242726e-02, -2.66699880e-01, -8.48811269e-02,
      5.66965714e-03, 2.92378180e-02, 1.99208315e-02, 2.88708471e-02])

    known_face_encodings.append(matt1_encoding)
    known_face_encodings.append(biff_encoding)

    # Initialize some variables
    face_locations = []
    face_encodings = []

    names = []

    print("Capturing image.")
    # Grab a single frame of video from the RPi camera as a numpy array
    camera.capture(output, format="rgb")

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(output)
    print("Found {} faces in image.".format(len(face_locations)))
    if(len(face_locations) == 0):
        names.append("Nobody")
        camera.close()
        return jsonify(faces=names)
        
    face_encodings = face_recognition.face_encodings(output, face_locations)

    # Loop over each face found in the frame to see if it's someone we know.
    for face_encoding in face_encodings:

        for index, known_face_encoding in enumerate(known_face_encodings):
            
            # See if the face is a match for the known face(s)
            match = face_recognition.compare_faces([known_face_encoding], face_encoding)

            if match[0]:
                if index == 0:
                    names.append("Matt")
                if index == 1:
                    names.append("Biff")
                
                print(names)

            camera.close()
            return jsonify(faces=names)

@app.route('/', methods=['GET', 'POST'])
def index():
    print("landed on hompage")
    return render_template('index.html')


if __name__ == "__main__":
    # host='0.0.0.0' means the web app is available to any device on the network
    app.run(host='0.0.0.0', port=5001, debug=True)

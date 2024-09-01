# anonymisation_faces
This project implements a face detection and anonymization system in images using Python and the OpenCV library. The goal is to automatically identify faces in an image and apply a pixelation effect to protect the identity of the person. To do this, a pre-trained Haar cascade classifier (haarcascade_frontalface_default.xml) is used to accurately detect human faces. Images are converted to grayscale to optimize the detection process, improving the efficiency of the algorithm. Once detected, faces are anonymized using a pixelation effect, which is achieved by reducing the size of the face region and then scaling it back to its original size. This project is useful for applications where privacy is important, such as in the processing of personal data in images.


![image](https://github.com/user-attachments/assets/e61f2c0e-0a9d-42cf-83a0-e8f461cfa136)



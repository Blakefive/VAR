# 필요한 패키지 import
import cv2 # OpenCV(실시간 이미지 프로세싱) 모듈
import pickle # 바이트(bytes) 형식의 데이터 변환 모듈
import struct # 바이트(bytes) 형식의 데이터 처리 모듈

capture = cv2.VideoCapture(0)

# 프레임 크기 지정
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 800) # 가로
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # 세로

retval, frame = capture.read()
retval, frame = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 90])
        
frame = pickle.dumps(frame)

print(frame)
#client_socket.sendall(struct.pack(">L", len(frame)) + frame)

# 메모리를 해제
capture.release()

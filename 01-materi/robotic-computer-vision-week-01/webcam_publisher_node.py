#!/usr/bin/env python
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def publish_webcam():
    # Inisialisasi node ROS
    rospy.init_node('webcam_publisher_node', anonymous=True)
    
    # Buat publisher ke topic 'webcam/image_raw'
    image_pub = rospy.Publisher('webcam/image_raw', Image, queue_size=10)
    
    # Buat objek CvBridge
    bridge = CvBridge()
    
    # Buka webcam (biasanya device 0)
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        rospy.logerr("Error: Tidak bisa membuka webcam.")
        return
        
    rospy.loginfo("Webcam publisher node dimulai...")
    
    # Set rate (misal 10 Hz)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        # Baca satu frame dari webcam
        ret, frame = cap.read()
        
        if ret:
            try:
                # Konversi frame OpenCV (BGR) ke ROS Image message
                ros_image = bridge.cv2_to_imgmsg(frame, "bgr8")
                
                # Publikasikan message
                image_pub.publish(ros_image)
            except CvBridgeError as e:
                rospy.logerr(e)
        
        # Jaga rate loop
        rate.sleep()

    # Rilis webcam saat node berhenti
    cap.release()

if __name__ == '__main__':
    try:
        publish_webcam()
    except rospy.ROSInterruptException:
        pass

#!/usr/bin/env python
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class ImageSubscriber:
    def __init__(self):
        # Inisialisasi node ROS
        rospy.init_node('image_subscriber_node', anonymous=True)
        
        # Buat objek CvBridge
        self.bridge = CvBridge()
        
        # Buat subscriber ke topic 'webcam/image_raw'
        # Panggil self.image_callback setiap ada message baru
        self.image_sub = rospy.Subscriber('webcam/image_raw', Image, self.image_callback)
        
        rospy.loginfo("Image subscriber node dimulai...")

    def image_callback(self, ros_image):
        try:
            # Konversi ROS Image message kembali ke frame OpenCV (BGR)
            cv_image = self.bridge.imgmsg_to_cv2(ros_image, "bgr8")
        except CvBridgeError as e:
            rospy.logerr(e)
            return

        # Tampilkan gambar menggunakan OpenCV
        cv2.imshow("Webcam Feed via ROS", cv_image)
        cv2.waitKey(1) # Penting untuk me-refresh jendela imshow

def main():
    try:
        ImageSubscriber()
        # rospy.spin() menjaga skrip tetap berjalan sampai node dihentikan
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
    finally:
        # Tutup semua jendela OpenCV saat keluar
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

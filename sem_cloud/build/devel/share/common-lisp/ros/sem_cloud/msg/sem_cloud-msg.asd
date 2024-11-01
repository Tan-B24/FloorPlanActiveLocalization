
(cl:in-package :asdf)

(defsystem "sem_cloud-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :sensor_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "EnvSensor" :depends-on ("_package_EnvSensor"))
    (:file "_package_EnvSensor" :depends-on ("_package"))
    (:file "GPS" :depends-on ("_package_GPS"))
    (:file "_package_GPS" :depends-on ("_package"))
    (:file "GlobalDescriptor" :depends-on ("_package_GlobalDescriptor"))
    (:file "_package_GlobalDescriptor" :depends-on ("_package"))
    (:file "Goal" :depends-on ("_package_Goal"))
    (:file "_package_Goal" :depends-on ("_package"))
    (:file "Info" :depends-on ("_package_Info"))
    (:file "_package_Info" :depends-on ("_package"))
    (:file "KeyPoint" :depends-on ("_package_KeyPoint"))
    (:file "_package_KeyPoint" :depends-on ("_package"))
    (:file "Link" :depends-on ("_package_Link"))
    (:file "_package_Link" :depends-on ("_package"))
    (:file "MapData" :depends-on ("_package_MapData"))
    (:file "_package_MapData" :depends-on ("_package"))
    (:file "MapGraph" :depends-on ("_package_MapGraph"))
    (:file "_package_MapGraph" :depends-on ("_package"))
    (:file "NodeData" :depends-on ("_package_NodeData"))
    (:file "_package_NodeData" :depends-on ("_package"))
    (:file "OdomInfo" :depends-on ("_package_OdomInfo"))
    (:file "_package_OdomInfo" :depends-on ("_package"))
    (:file "Path" :depends-on ("_package_Path"))
    (:file "_package_Path" :depends-on ("_package"))
    (:file "Point2f" :depends-on ("_package_Point2f"))
    (:file "_package_Point2f" :depends-on ("_package"))
    (:file "Point3f" :depends-on ("_package_Point3f"))
    (:file "_package_Point3f" :depends-on ("_package"))
    (:file "RGBDImage" :depends-on ("_package_RGBDImage"))
    (:file "_package_RGBDImage" :depends-on ("_package"))
    (:file "RGBDImages" :depends-on ("_package_RGBDImages"))
    (:file "_package_RGBDImages" :depends-on ("_package"))
    (:file "RGBDS" :depends-on ("_package_RGBDS"))
    (:file "_package_RGBDS" :depends-on ("_package"))
    (:file "ScanDescriptor" :depends-on ("_package_ScanDescriptor"))
    (:file "_package_ScanDescriptor" :depends-on ("_package"))
    (:file "Semantic" :depends-on ("_package_Semantic"))
    (:file "_package_Semantic" :depends-on ("_package"))
    (:file "UserData" :depends-on ("_package_UserData"))
    (:file "_package_UserData" :depends-on ("_package"))
    (:file "commandsafe" :depends-on ("_package_commandsafe"))
    (:file "_package_commandsafe" :depends-on ("_package"))
    (:file "imagepose" :depends-on ("_package_imagepose"))
    (:file "_package_imagepose" :depends-on ("_package"))
    (:file "nodes" :depends-on ("_package_nodes"))
    (:file "_package_nodes" :depends-on ("_package"))
    (:file "particle_msg" :depends-on ("_package_particle_msg"))
    (:file "_package_particle_msg" :depends-on ("_package"))
    (:file "particle_struct" :depends-on ("_package_particle_struct"))
    (:file "_package_particle_struct" :depends-on ("_package"))
    (:file "rds" :depends-on ("_package_rds"))
    (:file "_package_rds" :depends-on ("_package"))
    (:file "rgbdss" :depends-on ("_package_rgbdss"))
    (:file "_package_rgbdss" :depends-on ("_package"))
    (:file "robot_struct" :depends-on ("_package_robot_struct"))
    (:file "_package_robot_struct" :depends-on ("_package"))
    (:file "topParticle" :depends-on ("_package_topParticle"))
    (:file "_package_topParticle" :depends-on ("_package"))
  ))
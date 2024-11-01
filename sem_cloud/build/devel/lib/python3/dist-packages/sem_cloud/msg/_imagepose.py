# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from sem_cloud/imagepose.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import sensor_msgs.msg
import std_msgs.msg

class imagepose(genpy.Message):
  _md5sum = "7690fb2db9b30a77e74c1a7930e4d8d9"
  _type = "sem_cloud/imagepose"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header

sensor_msgs/Image  rgb

sensor_msgs/Image  depth

sensor_msgs/Image semantic

int32[]              poseId

geometry_msgs/Pose[] pose

int32              length

int32              loopclosureId

int32		    proximityDetectionId

sensor_msgs/PointCloud2 rtabmapPcl

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: sensor_msgs/Image
# This message contains an uncompressed image
# (0, 0) is at top-left corner of image
#

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of camera
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image
                     # If the frame_id here and the frame_id of the CameraInfo
                     # message associated with the image conflict
                     # the behavior is undefined

uint32 height         # image height, that is, number of rows
uint32 width          # image width, that is, number of columns

# The legal values for encoding are in file src/image_encodings.cpp
# If you want to standardize a new string format, join
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.

string encoding       # Encoding of pixels -- channel meaning, ordering, size
                      # taken from the list of strings in include/sensor_msgs/image_encodings.h

uint8 is_bigendian    # is this data bigendian?
uint32 step           # Full row length in bytes
uint8[] data          # actual matrix data, size is (step * rows)

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: sensor_msgs/PointCloud2
# This message holds a collection of N-dimensional points, which may
# contain additional information such as normals, intensity, etc. The
# point data is stored as a binary blob, its layout described by the
# contents of the "fields" array.

# The point cloud data may be organized 2d (image-like) or 1d
# (unordered). Point clouds organized as 2d images may be produced by
# camera depth sensors such as stereo or time-of-flight.

# Time of sensor data acquisition, and the coordinate frame ID (for 3d
# points).
Header header

# 2D structure of the point cloud. If the cloud is unordered, height is
# 1 and width is the length of the point cloud.
uint32 height
uint32 width

# Describes the channels and their layout in the binary data blob.
PointField[] fields

bool    is_bigendian # Is this data bigendian?
uint32  point_step   # Length of a point in bytes
uint32  row_step     # Length of a row in bytes
uint8[] data         # Actual point data, size is (row_step*height)

bool is_dense        # True if there are no invalid points

================================================================================
MSG: sensor_msgs/PointField
# This message holds the description of one point entry in the
# PointCloud2 message format.
uint8 INT8    = 1
uint8 UINT8   = 2
uint8 INT16   = 3
uint8 UINT16  = 4
uint8 INT32   = 5
uint8 UINT32  = 6
uint8 FLOAT32 = 7
uint8 FLOAT64 = 8

string name      # Name of field
uint32 offset    # Offset from start of point struct
uint8  datatype  # Datatype enumeration, see above
uint32 count     # How many elements in the field
"""
  __slots__ = ['header','rgb','depth','semantic','poseId','pose','length','loopclosureId','proximityDetectionId','rtabmapPcl']
  _slot_types = ['std_msgs/Header','sensor_msgs/Image','sensor_msgs/Image','sensor_msgs/Image','int32[]','geometry_msgs/Pose[]','int32','int32','int32','sensor_msgs/PointCloud2']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,rgb,depth,semantic,poseId,pose,length,loopclosureId,proximityDetectionId,rtabmapPcl

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(imagepose, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.rgb is None:
        self.rgb = sensor_msgs.msg.Image()
      if self.depth is None:
        self.depth = sensor_msgs.msg.Image()
      if self.semantic is None:
        self.semantic = sensor_msgs.msg.Image()
      if self.poseId is None:
        self.poseId = []
      if self.pose is None:
        self.pose = []
      if self.length is None:
        self.length = 0
      if self.loopclosureId is None:
        self.loopclosureId = 0
      if self.proximityDetectionId is None:
        self.proximityDetectionId = 0
      if self.rtabmapPcl is None:
        self.rtabmapPcl = sensor_msgs.msg.PointCloud2()
    else:
      self.header = std_msgs.msg.Header()
      self.rgb = sensor_msgs.msg.Image()
      self.depth = sensor_msgs.msg.Image()
      self.semantic = sensor_msgs.msg.Image()
      self.poseId = []
      self.pose = []
      self.length = 0
      self.loopclosureId = 0
      self.proximityDetectionId = 0
      self.rtabmapPcl = sensor_msgs.msg.PointCloud2()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.rgb.header.seq, _x.rgb.header.stamp.secs, _x.rgb.header.stamp.nsecs))
      _x = self.rgb.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.rgb.height, _x.rgb.width))
      _x = self.rgb.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.rgb.is_bigendian, _x.rgb.step))
      _x = self.rgb.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.depth.header.seq, _x.depth.header.stamp.secs, _x.depth.header.stamp.nsecs))
      _x = self.depth.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.depth.height, _x.depth.width))
      _x = self.depth.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.depth.is_bigendian, _x.depth.step))
      _x = self.depth.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.semantic.header.seq, _x.semantic.header.stamp.secs, _x.semantic.header.stamp.nsecs))
      _x = self.semantic.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.semantic.height, _x.semantic.width))
      _x = self.semantic.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.semantic.is_bigendian, _x.semantic.step))
      _x = self.semantic.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.poseId)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.Struct(pattern).pack(*self.poseId))
      length = len(self.pose)
      buff.write(_struct_I.pack(length))
      for val1 in self.pose:
        _v1 = val1.position
        _x = _v1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v2 = val1.orientation
        _x = _v2
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
      _x = self
      buff.write(_get_struct_3i3I().pack(_x.length, _x.loopclosureId, _x.proximityDetectionId, _x.rtabmapPcl.header.seq, _x.rtabmapPcl.header.stamp.secs, _x.rtabmapPcl.header.stamp.nsecs))
      _x = self.rtabmapPcl.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.rtabmapPcl.height, _x.rtabmapPcl.width))
      length = len(self.rtabmapPcl.fields)
      buff.write(_struct_I.pack(length))
      for val1 in self.rtabmapPcl.fields:
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1
        buff.write(_get_struct_IBI().pack(_x.offset, _x.datatype, _x.count))
      _x = self
      buff.write(_get_struct_B2I().pack(_x.rtabmapPcl.is_bigendian, _x.rtabmapPcl.point_step, _x.rtabmapPcl.row_step))
      _x = self.rtabmapPcl.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.rtabmapPcl.is_dense
      buff.write(_get_struct_B().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.rgb is None:
        self.rgb = sensor_msgs.msg.Image()
      if self.depth is None:
        self.depth = sensor_msgs.msg.Image()
      if self.semantic is None:
        self.semantic = sensor_msgs.msg.Image()
      if self.pose is None:
        self.pose = None
      if self.rtabmapPcl is None:
        self.rtabmapPcl = sensor_msgs.msg.PointCloud2()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.rgb.header.seq, _x.rgb.header.stamp.secs, _x.rgb.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.rgb.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.rgb.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.rgb.height, _x.rgb.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.rgb.encoding = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.rgb.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.rgb.is_bigendian, _x.rgb.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.rgb.data = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.depth.header.seq, _x.depth.header.stamp.secs, _x.depth.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.depth.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.depth.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.depth.height, _x.depth.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.depth.encoding = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.depth.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.depth.is_bigendian, _x.depth.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.depth.data = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.semantic.header.seq, _x.semantic.header.stamp.secs, _x.semantic.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.semantic.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.semantic.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.semantic.height, _x.semantic.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.semantic.encoding = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.semantic.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.semantic.is_bigendian, _x.semantic.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.semantic.data = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.poseId = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.pose = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Pose()
        _v3 = val1.position
        _x = _v3
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v4 = val1.orientation
        _x = _v4
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.pose.append(val1)
      _x = self
      start = end
      end += 24
      (_x.length, _x.loopclosureId, _x.proximityDetectionId, _x.rtabmapPcl.header.seq, _x.rtabmapPcl.header.stamp.secs, _x.rtabmapPcl.header.stamp.nsecs,) = _get_struct_3i3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.rtabmapPcl.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.rtabmapPcl.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.rtabmapPcl.height, _x.rtabmapPcl.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.rtabmapPcl.fields = []
      for i in range(0, length):
        val1 = sensor_msgs.msg.PointField()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.name = str[start:end]
        _x = val1
        start = end
        end += 9
        (_x.offset, _x.datatype, _x.count,) = _get_struct_IBI().unpack(str[start:end])
        self.rtabmapPcl.fields.append(val1)
      _x = self
      start = end
      end += 9
      (_x.rtabmapPcl.is_bigendian, _x.rtabmapPcl.point_step, _x.rtabmapPcl.row_step,) = _get_struct_B2I().unpack(str[start:end])
      self.rtabmapPcl.is_bigendian = bool(self.rtabmapPcl.is_bigendian)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.rtabmapPcl.data = str[start:end]
      start = end
      end += 1
      (self.rtabmapPcl.is_dense,) = _get_struct_B().unpack(str[start:end])
      self.rtabmapPcl.is_dense = bool(self.rtabmapPcl.is_dense)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.rgb.header.seq, _x.rgb.header.stamp.secs, _x.rgb.header.stamp.nsecs))
      _x = self.rgb.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.rgb.height, _x.rgb.width))
      _x = self.rgb.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.rgb.is_bigendian, _x.rgb.step))
      _x = self.rgb.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.depth.header.seq, _x.depth.header.stamp.secs, _x.depth.header.stamp.nsecs))
      _x = self.depth.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.depth.height, _x.depth.width))
      _x = self.depth.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.depth.is_bigendian, _x.depth.step))
      _x = self.depth.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.semantic.header.seq, _x.semantic.header.stamp.secs, _x.semantic.header.stamp.nsecs))
      _x = self.semantic.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.semantic.height, _x.semantic.width))
      _x = self.semantic.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.semantic.is_bigendian, _x.semantic.step))
      _x = self.semantic.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.poseId)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.poseId.tostring())
      length = len(self.pose)
      buff.write(_struct_I.pack(length))
      for val1 in self.pose:
        _v5 = val1.position
        _x = _v5
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v6 = val1.orientation
        _x = _v6
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
      _x = self
      buff.write(_get_struct_3i3I().pack(_x.length, _x.loopclosureId, _x.proximityDetectionId, _x.rtabmapPcl.header.seq, _x.rtabmapPcl.header.stamp.secs, _x.rtabmapPcl.header.stamp.nsecs))
      _x = self.rtabmapPcl.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.rtabmapPcl.height, _x.rtabmapPcl.width))
      length = len(self.rtabmapPcl.fields)
      buff.write(_struct_I.pack(length))
      for val1 in self.rtabmapPcl.fields:
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1
        buff.write(_get_struct_IBI().pack(_x.offset, _x.datatype, _x.count))
      _x = self
      buff.write(_get_struct_B2I().pack(_x.rtabmapPcl.is_bigendian, _x.rtabmapPcl.point_step, _x.rtabmapPcl.row_step))
      _x = self.rtabmapPcl.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.rtabmapPcl.is_dense
      buff.write(_get_struct_B().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.rgb is None:
        self.rgb = sensor_msgs.msg.Image()
      if self.depth is None:
        self.depth = sensor_msgs.msg.Image()
      if self.semantic is None:
        self.semantic = sensor_msgs.msg.Image()
      if self.pose is None:
        self.pose = None
      if self.rtabmapPcl is None:
        self.rtabmapPcl = sensor_msgs.msg.PointCloud2()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.rgb.header.seq, _x.rgb.header.stamp.secs, _x.rgb.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.rgb.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.rgb.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.rgb.height, _x.rgb.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.rgb.encoding = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.rgb.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.rgb.is_bigendian, _x.rgb.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.rgb.data = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.depth.header.seq, _x.depth.header.stamp.secs, _x.depth.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.depth.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.depth.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.depth.height, _x.depth.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.depth.encoding = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.depth.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.depth.is_bigendian, _x.depth.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.depth.data = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.semantic.header.seq, _x.semantic.header.stamp.secs, _x.semantic.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.semantic.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.semantic.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.semantic.height, _x.semantic.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.semantic.encoding = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.semantic.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.semantic.is_bigendian, _x.semantic.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.semantic.data = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.poseId = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.pose = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Pose()
        _v7 = val1.position
        _x = _v7
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v8 = val1.orientation
        _x = _v8
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.pose.append(val1)
      _x = self
      start = end
      end += 24
      (_x.length, _x.loopclosureId, _x.proximityDetectionId, _x.rtabmapPcl.header.seq, _x.rtabmapPcl.header.stamp.secs, _x.rtabmapPcl.header.stamp.nsecs,) = _get_struct_3i3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.rtabmapPcl.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.rtabmapPcl.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.rtabmapPcl.height, _x.rtabmapPcl.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.rtabmapPcl.fields = []
      for i in range(0, length):
        val1 = sensor_msgs.msg.PointField()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.name = str[start:end]
        _x = val1
        start = end
        end += 9
        (_x.offset, _x.datatype, _x.count,) = _get_struct_IBI().unpack(str[start:end])
        self.rtabmapPcl.fields.append(val1)
      _x = self
      start = end
      end += 9
      (_x.rtabmapPcl.is_bigendian, _x.rtabmapPcl.point_step, _x.rtabmapPcl.row_step,) = _get_struct_B2I().unpack(str[start:end])
      self.rtabmapPcl.is_bigendian = bool(self.rtabmapPcl.is_bigendian)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.rtabmapPcl.data = str[start:end]
      start = end
      end += 1
      (self.rtabmapPcl.is_dense,) = _get_struct_B().unpack(str[start:end])
      self.rtabmapPcl.is_dense = bool(self.rtabmapPcl.is_dense)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
_struct_3i3I = None
def _get_struct_3i3I():
    global _struct_3i3I
    if _struct_3i3I is None:
        _struct_3i3I = struct.Struct("<3i3I")
    return _struct_3i3I
_struct_4d = None
def _get_struct_4d():
    global _struct_4d
    if _struct_4d is None:
        _struct_4d = struct.Struct("<4d")
    return _struct_4d
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
_struct_B2I = None
def _get_struct_B2I():
    global _struct_B2I
    if _struct_B2I is None:
        _struct_B2I = struct.Struct("<B2I")
    return _struct_B2I
_struct_BI = None
def _get_struct_BI():
    global _struct_BI
    if _struct_BI is None:
        _struct_BI = struct.Struct("<BI")
    return _struct_BI
_struct_IBI = None
def _get_struct_IBI():
    global _struct_IBI
    if _struct_IBI is None:
        _struct_IBI = struct.Struct("<IBI")
    return _struct_IBI

// Generated by gencpp from file sem_cloud/Goal.msg
// DO NOT EDIT!


#ifndef SEM_CLOUD_MESSAGE_GOAL_H
#define SEM_CLOUD_MESSAGE_GOAL_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace sem_cloud
{
template <class ContainerAllocator>
struct Goal_
{
  typedef Goal_<ContainerAllocator> Type;

  Goal_()
    : header()
    , node_id(0)
    , node_label()
    , frame_id()  {
    }
  Goal_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , node_id(0)
    , node_label(_alloc)
    , frame_id(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef int32_t _node_id_type;
  _node_id_type node_id;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _node_label_type;
  _node_label_type node_label;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _frame_id_type;
  _frame_id_type frame_id;





  typedef boost::shared_ptr< ::sem_cloud::Goal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::sem_cloud::Goal_<ContainerAllocator> const> ConstPtr;

}; // struct Goal_

typedef ::sem_cloud::Goal_<std::allocator<void> > Goal;

typedef boost::shared_ptr< ::sem_cloud::Goal > GoalPtr;
typedef boost::shared_ptr< ::sem_cloud::Goal const> GoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::sem_cloud::Goal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::sem_cloud::Goal_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::sem_cloud::Goal_<ContainerAllocator1> & lhs, const ::sem_cloud::Goal_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.node_id == rhs.node_id &&
    lhs.node_label == rhs.node_label &&
    lhs.frame_id == rhs.frame_id;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::sem_cloud::Goal_<ContainerAllocator1> & lhs, const ::sem_cloud::Goal_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace sem_cloud

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::sem_cloud::Goal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::sem_cloud::Goal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sem_cloud::Goal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sem_cloud::Goal_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sem_cloud::Goal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sem_cloud::Goal_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::sem_cloud::Goal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "70f8a16a321d4ec76904a9989a8798b7";
  }

  static const char* value(const ::sem_cloud::Goal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x70f8a16a321d4ec7ULL;
  static const uint64_t static_value2 = 0x6904a9989a8798b7ULL;
};

template<class ContainerAllocator>
struct DataType< ::sem_cloud::Goal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "sem_cloud/Goal";
  }

  static const char* value(const ::sem_cloud::Goal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::sem_cloud::Goal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n"
"Header header\n"
"\n"
"# Set either node_id or node_label\n"
"int32 node_id\n"
"string node_label\n"
"\n"
"# optional: if not set, the base frame of the robot is used\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
;
  }

  static const char* value(const ::sem_cloud::Goal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::sem_cloud::Goal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.node_id);
      stream.next(m.node_label);
      stream.next(m.frame_id);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Goal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::sem_cloud::Goal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::sem_cloud::Goal_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "node_id: ";
    Printer<int32_t>::stream(s, indent + "  ", v.node_id);
    s << indent << "node_label: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.node_label);
    s << indent << "frame_id: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.frame_id);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SEM_CLOUD_MESSAGE_GOAL_H
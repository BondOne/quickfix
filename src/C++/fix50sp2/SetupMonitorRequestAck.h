#ifndef FIX50SP2_SETUPMONITORREQUESTACK_H
#define FIX50SP2_SETUPMONITORREQUESTACK_H

#include "Message.h"

namespace FIX50SP2
{

  class SetupMonitorRequestAck : public Message
  {
  public:
    SetupMonitorRequestAck() : Message(MsgType()) {}
    SetupMonitorRequestAck(const FIX::Message& m) : Message(m) {}
    SetupMonitorRequestAck(const Message& m) : Message(m) {}
    SetupMonitorRequestAck(const SetupMonitorRequestAck& m) : Message(m) {}
    static FIX::MsgType MsgType() { return FIX::MsgType("USMQK"); }

    SetupMonitorRequestAck(
      const FIX::SetupMonitorRequestID& aSetupMonitorRequestID,
      const FIX::SetupMonitorRequestStatus& aSetupMonitorRequestStatus )
    : Message(MsgType())
    {
      set(aSetupMonitorRequestID);
      set(aSetupMonitorRequestStatus);
    }

    FIELD_SET(*this, FIX::SetupMonitorRequestID);
    FIELD_SET(*this, FIX::MDFeedType);
    FIELD_SET(*this, FIX::SetupMonitorRequestStatus);
    FIELD_SET(*this, FIX::Text);
  };

}

#endif

#ifndef FIX50SP2_PARTYDETAILSLISTREPORT_H
#define FIX50SP2_PARTYDETAILSLISTREPORT_H

#include "Message.h"

namespace FIX50SP2
{

  class PartyDetailsListReport : public Message
  {
  public:
    PartyDetailsListReport() : Message(MsgType()) {}
    PartyDetailsListReport(const FIX::Message& m) : Message(m) {}
    PartyDetailsListReport(const Message& m) : Message(m) {}
    PartyDetailsListReport(const PartyDetailsListReport& m) : Message(m) {}
    static FIX::MsgType MsgType() { return FIX::MsgType("CG"); }

    PartyDetailsListReport(
      const FIX::PartyDetailsListReportID& aPartyDetailsListReportID )
    : Message(MsgType())
    {
      set(aPartyDetailsListReportID);
    }

    FIELD_SET(*this, FIX::ApplID);
    FIELD_SET(*this, FIX::ApplSeqNum);
    FIELD_SET(*this, FIX::ApplLastSeqNum);
    FIELD_SET(*this, FIX::ApplResendFlag);
    FIELD_SET(*this, FIX::PartyDetailsListReportID);
    FIELD_SET(*this, FIX::PartyDetailsListRequestID);
    FIELD_SET(*this, FIX::PartyDetailsRequestResult);
    FIELD_SET(*this, FIX::TotNoPartyList);
    FIELD_SET(*this, FIX::LastFragment);
    FIELD_SET(*this, FIX::NoPartyList);
    class NoPartyList: public FIX::Group
    {
    public:
    NoPartyList() : FIX::Group(1513,448,FIX::message_order(448,447,452,1562,0)) {}
      FIELD_SET(*this, FIX::PartyID);
      FIELD_SET(*this, FIX::PartyIDSource);
      FIELD_SET(*this, FIX::PartyRole);
      FIELD_SET(*this, FIX::NoPartySubIDs);
      class NoPartySubIDs: public FIX::Group
      {
      public:
      NoPartySubIDs() : FIX::Group(802,523,FIX::message_order(523,803,0)) {}
        FIELD_SET(*this, FIX::PartySubID);
        FIELD_SET(*this, FIX::PartySubIDType);
      };
      FIELD_SET(*this, FIX::NoPartyAltIDs);
      class NoPartyAltIDs: public FIX::Group
      {
      public:
      NoPartyAltIDs() : FIX::Group(1516,1517,FIX::message_order(1517,1518,1519,0)) {}
        FIELD_SET(*this, FIX::PartyAltID);
        FIELD_SET(*this, FIX::PartyAltIDSource);
        FIELD_SET(*this, FIX::NoPartyAltSubIDs);
        class NoPartyAltSubIDs: public FIX::Group
        {
        public:
        NoPartyAltSubIDs() : FIX::Group(1519,1520,FIX::message_order(1520,1521,0)) {}
          FIELD_SET(*this, FIX::PartyAltSubID);
          FIELD_SET(*this, FIX::PartyAltSubIDType);
        };
      };
      FIELD_SET(*this, FIX::NoContextPartyIDs);
      class NoContextPartyIDs: public FIX::Group
      {
      public:
      NoContextPartyIDs() : FIX::Group(1522,1523,FIX::message_order(1523,1524,1525,1526,0)) {}
        FIELD_SET(*this, FIX::ContextPartyID);
        FIELD_SET(*this, FIX::ContextPartyIDSource);
        FIELD_SET(*this, FIX::ContextPartyRole);
        FIELD_SET(*this, FIX::NoContextPartySubIDs);
        class NoContextPartySubIDs: public FIX::Group
        {
        public:
        NoContextPartySubIDs() : FIX::Group(1526,1527,FIX::message_order(1527,1528,0)) {}
          FIELD_SET(*this, FIX::ContextPartySubID);
          FIELD_SET(*this, FIX::ContextPartySubIDType);
        };
      };
      FIELD_SET(*this, FIX::NoRiskLimits);
      class NoRiskLimits: public FIX::Group
      {
      public:
      NoRiskLimits() : FIX::Group(1529,1530,FIX::message_order(1530,1531,1532,1533,1534,1559,0)) {}
        FIELD_SET(*this, FIX::RiskLimitType);
        FIELD_SET(*this, FIX::RiskLimitAmount);
        FIELD_SET(*this, FIX::RiskLimitCurrency);
        FIELD_SET(*this, FIX::RiskLimitPlatform);
        FIELD_SET(*this, FIX::NoRiskInstruments);
        class NoRiskInstruments: public FIX::Group
        {
        public:
        NoRiskInstruments() : FIX::Group(1534,1535,FIX::message_order(1535,1536,1537,1538,1539,1540,1543,1544,1545,1546,1547,1548,1549,1550,1551,1552,1553,1554,1555,1616,1556,1620,1621,1557,1558,0)) {}
          FIELD_SET(*this, FIX::RiskInstrumentOperator);
          FIELD_SET(*this, FIX::RiskSymbol);
          FIELD_SET(*this, FIX::RiskSymbolSfx);
          FIELD_SET(*this, FIX::RiskSecurityID);
          FIELD_SET(*this, FIX::RiskSecurityIDSource);
          FIELD_SET(*this, FIX::NoRiskSecurityAltID);
          class NoRiskSecurityAltID: public FIX::Group
          {
          public:
          NoRiskSecurityAltID() : FIX::Group(1540,1541,FIX::message_order(1541,1542,0)) {}
            FIELD_SET(*this, FIX::RiskSecurityAltID);
            FIELD_SET(*this, FIX::RiskSecurityAltIDSource);
          };
          FIELD_SET(*this, FIX::RiskProduct);
          FIELD_SET(*this, FIX::RiskProductComplex);
          FIELD_SET(*this, FIX::RiskSecurityGroup);
          FIELD_SET(*this, FIX::RiskCFICode);
          FIELD_SET(*this, FIX::RiskSecurityType);
          FIELD_SET(*this, FIX::RiskSecuritySubType);
          FIELD_SET(*this, FIX::RiskMaturityMonthYear);
          FIELD_SET(*this, FIX::RiskMaturityTime);
          FIELD_SET(*this, FIX::RiskRestructuringType);
          FIELD_SET(*this, FIX::RiskSeniority);
          FIELD_SET(*this, FIX::RiskPutOrCall);
          FIELD_SET(*this, FIX::RiskFlexibleIndicator);
          FIELD_SET(*this, FIX::RiskCouponRate);
          FIELD_SET(*this, FIX::RiskSecurityExchange);
          FIELD_SET(*this, FIX::RiskSecurityDesc);
          FIELD_SET(*this, FIX::RiskEncodedSecurityDescLen);
          FIELD_SET(*this, FIX::RiskEncodedSecurityDesc);
          FIELD_SET(*this, FIX::RiskInstrumentSettlType);
          FIELD_SET(*this, FIX::RiskInstrumentMultiplier);
        };
        FIELD_SET(*this, FIX::NoRiskWarningLevels);
        class NoRiskWarningLevels: public FIX::Group
        {
        public:
        NoRiskWarningLevels() : FIX::Group(1559,1560,FIX::message_order(1560,1561,0)) {}
          FIELD_SET(*this, FIX::RiskWarningLevelPercent);
          FIELD_SET(*this, FIX::RiskWarningLevelName);
        };
      };
      FIELD_SET(*this, FIX::NoRelatedPartyIDs);
      class NoRelatedPartyIDs: public FIX::Group
      {
      public:
      NoRelatedPartyIDs() : FIX::Group(1562,1563,FIX::message_order(1563,1564,1565,1514,0)) {}
        FIELD_SET(*this, FIX::RelatedPartyID);
        FIELD_SET(*this, FIX::RelatedPartyIDSource);
        FIELD_SET(*this, FIX::RelatedPartyRole);
        FIELD_SET(*this, FIX::NoRelatedPartySubIDs);
        class NoRelatedPartySubIDs: public FIX::Group
        {
        public:
        NoRelatedPartySubIDs() : FIX::Group(1566,1567,FIX::message_order(1567,1568,0)) {}
          FIELD_SET(*this, FIX::RelatedPartySubID);
          FIELD_SET(*this, FIX::RelatedPartySubIDType);
        };
        FIELD_SET(*this, FIX::NoRelatedPartyAltIDs);
        class NoRelatedPartyAltIDs: public FIX::Group
        {
        public:
        NoRelatedPartyAltIDs() : FIX::Group(1569,1570,FIX::message_order(1570,1571,1572,0)) {}
          FIELD_SET(*this, FIX::RelatedPartyAltID);
          FIELD_SET(*this, FIX::RelatedPartyAltIDSource);
          FIELD_SET(*this, FIX::NoRelatedPartyAltSubIDs);
          class NoRelatedPartyAltSubIDs: public FIX::Group
          {
          public:
          NoRelatedPartyAltSubIDs() : FIX::Group(1572,1573,FIX::message_order(1573,1574,0)) {}
            FIELD_SET(*this, FIX::RelatedPartyAltSubID);
            FIELD_SET(*this, FIX::RelatedPartyAltSubIDType);
          };
        };
        FIELD_SET(*this, FIX::NoRelatedContextPartyIDs);
        class NoRelatedContextPartyIDs: public FIX::Group
        {
        public:
        NoRelatedContextPartyIDs() : FIX::Group(1575,1576,FIX::message_order(1576,1577,1578,1579,0)) {}
          FIELD_SET(*this, FIX::RelatedContextPartyID);
          FIELD_SET(*this, FIX::RelatedContextPartyIDSource);
          FIELD_SET(*this, FIX::RelatedContextPartyRole);
          FIELD_SET(*this, FIX::NoRelatedContextPartySubIDs);
          class NoRelatedContextPartySubIDs: public FIX::Group
          {
          public:
          NoRelatedContextPartySubIDs() : FIX::Group(1579,1580,FIX::message_order(1580,1581,0)) {}
            FIELD_SET(*this, FIX::RelatedContextPartySubID);
            FIELD_SET(*this, FIX::RelatedContextPartySubIDType);
          };
        };
        FIELD_SET(*this, FIX::NoRelationshipRiskLimits);
        class NoRelationshipRiskLimits: public FIX::Group
        {
        public:
        NoRelationshipRiskLimits() : FIX::Group(1582,1583,FIX::message_order(1583,1584,1585,1586,1587,1613,0)) {}
          FIELD_SET(*this, FIX::RelationshipRiskLimitType);
          FIELD_SET(*this, FIX::RelationshipRiskLimitAmount);
          FIELD_SET(*this, FIX::RelationshipRiskLimitCurrency);
          FIELD_SET(*this, FIX::RelationshipRiskLimitPlatform);
          FIELD_SET(*this, FIX::NoRelationshipRiskInstruments);
          class NoRelationshipRiskInstruments: public FIX::Group
          {
          public:
          NoRelationshipRiskInstruments() : FIX::Group(1587,1588,FIX::message_order(1588,1589,1590,1591,1592,1593,1596,1597,1598,1599,1600,1601,1602,1603,1604,1605,1606,1607,1608,1609,1610,1618,1619,1611,1612,0)) {}
            FIELD_SET(*this, FIX::RelationshipRiskInstrumentOperator);
            FIELD_SET(*this, FIX::RelationshipRiskSymbol);
            FIELD_SET(*this, FIX::RelationshipRiskSymbolSfx);
            FIELD_SET(*this, FIX::RelationshipRiskSecurityID);
            FIELD_SET(*this, FIX::RelationshipRiskSecurityIDSource);
            FIELD_SET(*this, FIX::NoRelationshipRiskSecurityAltID);
            class NoRelationshipRiskSecurityAltID: public FIX::Group
            {
            public:
            NoRelationshipRiskSecurityAltID() : FIX::Group(1593,1594,FIX::message_order(1594,1595,0)) {}
              FIELD_SET(*this, FIX::RelationshipRiskSecurityAltID);
              FIELD_SET(*this, FIX::RelationshipRiskSecurityAltIDSource);
            };
            FIELD_SET(*this, FIX::RelationshipRiskProduct);
            FIELD_SET(*this, FIX::RelationshipRiskProductComplex);
            FIELD_SET(*this, FIX::RelationshipRiskSecurityGroup);
            FIELD_SET(*this, FIX::RelationshipRiskCFICode);
            FIELD_SET(*this, FIX::RelationshipRiskSecurityType);
            FIELD_SET(*this, FIX::RelationshipRiskSecuritySubType);
            FIELD_SET(*this, FIX::RelationshipRiskMaturityMonthYear);
            FIELD_SET(*this, FIX::RelationshipRiskMaturityTime);
            FIELD_SET(*this, FIX::RelationshipRiskRestructuringType);
            FIELD_SET(*this, FIX::RelationshipRiskSeniority);
            FIELD_SET(*this, FIX::RelationshipRiskPutOrCall);
            FIELD_SET(*this, FIX::RelationshipRiskFlexibleIndicator);
            FIELD_SET(*this, FIX::RelationshipRiskCouponRate);
            FIELD_SET(*this, FIX::RelationshipRiskSecurityExchange);
            FIELD_SET(*this, FIX::RelationshipRiskSecurityDesc);
            FIELD_SET(*this, FIX::RelationshipRiskEncodedSecurityDescLen);
            FIELD_SET(*this, FIX::RelationshipRiskEncodedSecurityDesc);
            FIELD_SET(*this, FIX::RelationshipRiskInstrumentSettlType);
            FIELD_SET(*this, FIX::RelationshipRiskInstrumentMultiplier);
          };
          FIELD_SET(*this, FIX::NoRelationshipRiskWarningLevels);
          class NoRelationshipRiskWarningLevels: public FIX::Group
          {
          public:
          NoRelationshipRiskWarningLevels() : FIX::Group(1613,1614,FIX::message_order(1614,1615,0)) {}
            FIELD_SET(*this, FIX::RelationshipRiskWarningLevelPercent);
            FIELD_SET(*this, FIX::RelationshipRiskWarningLevelName);
          };
        };
        FIELD_SET(*this, FIX::NoPartyRelationships);
        class NoPartyRelationships: public FIX::Group
        {
        public:
        NoPartyRelationships() : FIX::Group(1514,1515,FIX::message_order(1515,0)) {}
          FIELD_SET(*this, FIX::PartyRelationship);
        };
      };
    };
    FIELD_SET(*this, FIX::Text);
    FIELD_SET(*this, FIX::EncodedTextLen);
    FIELD_SET(*this, FIX::EncodedText);
  };

}

#endif

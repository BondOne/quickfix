#ifndef FIX50SP2_MASSQUOTE_H
#define FIX50SP2_MASSQUOTE_H

#include "Message.h"

namespace FIX50SP2
{

  class MassQuote : public Message
  {
  public:
    MassQuote() : Message(MsgType()) {}
    MassQuote(const FIX::Message& m) : Message(m) {}
    MassQuote(const Message& m) : Message(m) {}
    MassQuote(const MassQuote& m) : Message(m) {}
    static FIX::MsgType MsgType() { return FIX::MsgType("i"); }

    MassQuote(
      const FIX::QuoteID& aQuoteID )
    : Message(MsgType())
    {
      set(aQuoteID);
    }

    FIELD_SET(*this, FIX::QuoteReqID);
    FIELD_SET(*this, FIX::QuoteID);
    FIELD_SET(*this, FIX::QuoteType);
    FIELD_SET(*this, FIX::QuoteResponseLevel);
    FIELD_SET(*this, FIX::NoPartyIDs);
    class NoPartyIDs: public FIX::Group
    {
    public:
    NoPartyIDs() : FIX::Group(453,448,FIX::message_order(448,447,452,2376,802,0)) {}
      FIELD_SET(*this, FIX::PartyID);
      FIELD_SET(*this, FIX::PartyIDSource);
      FIELD_SET(*this, FIX::PartyRole);
      FIELD_SET(*this, FIX::PartyRoleQualifier);
      FIELD_SET(*this, FIX::NoPartySubIDs);
      class NoPartySubIDs: public FIX::Group
      {
      public:
      NoPartySubIDs() : FIX::Group(802,523,FIX::message_order(523,803,0)) {}
        FIELD_SET(*this, FIX::PartySubID);
        FIELD_SET(*this, FIX::PartySubIDType);
      };
    };
    FIELD_SET(*this, FIX::Account);
    FIELD_SET(*this, FIX::AcctIDSource);
    FIELD_SET(*this, FIX::AccountType);
    FIELD_SET(*this, FIX::DefBidSize);
    FIELD_SET(*this, FIX::DefOfferSize);
    FIELD_SET(*this, FIX::NoQuoteSets);
    class NoQuoteSets: public FIX::Group
    {
    public:
    NoQuoteSets() : FIX::Group(296,302,FIX::message_order(302,311,312,309,305,462,463,310,763,313,542,1213,241,242,243,244,245,246,256,595,592,593,594,247,316,941,317,436,998,1423,1424,1425,1000,1419,435,308,306,362,363,307,364,365,877,878,972,318,879,975,973,974,810,882,883,884,885,886,1044,1045,1046,1038,1039,315,1437,1441,1453,1454,1455,1456,1459,1460,367,304,893,295,0)) {}
      FIELD_SET(*this, FIX::QuoteSetID);
      FIELD_SET(*this, FIX::UnderlyingSymbol);
      FIELD_SET(*this, FIX::UnderlyingSymbolSfx);
      FIELD_SET(*this, FIX::UnderlyingSecurityID);
      FIELD_SET(*this, FIX::UnderlyingSecurityIDSource);
      FIELD_SET(*this, FIX::UnderlyingProduct);
      FIELD_SET(*this, FIX::UnderlyingCFICode);
      FIELD_SET(*this, FIX::UnderlyingSecurityType);
      FIELD_SET(*this, FIX::UnderlyingSecuritySubType);
      FIELD_SET(*this, FIX::UnderlyingMaturityMonthYear);
      FIELD_SET(*this, FIX::UnderlyingMaturityDate);
      FIELD_SET(*this, FIX::UnderlyingMaturityTime);
      FIELD_SET(*this, FIX::UnderlyingCouponPaymentDate);
      FIELD_SET(*this, FIX::UnderlyingIssueDate);
      FIELD_SET(*this, FIX::UnderlyingRepoCollateralSecurityType);
      FIELD_SET(*this, FIX::UnderlyingRepurchaseTerm);
      FIELD_SET(*this, FIX::UnderlyingRepurchaseRate);
      FIELD_SET(*this, FIX::UnderlyingFactor);
      FIELD_SET(*this, FIX::UnderlyingCreditRating);
      FIELD_SET(*this, FIX::UnderlyingInstrRegistry);
      FIELD_SET(*this, FIX::UnderlyingCountryOfIssue);
      FIELD_SET(*this, FIX::UnderlyingStateOrProvinceOfIssue);
      FIELD_SET(*this, FIX::UnderlyingLocaleOfIssue);
      FIELD_SET(*this, FIX::UnderlyingRedemptionDate);
      FIELD_SET(*this, FIX::UnderlyingStrikePrice);
      FIELD_SET(*this, FIX::UnderlyingStrikeCurrency);
      FIELD_SET(*this, FIX::UnderlyingOptAttribute);
      FIELD_SET(*this, FIX::UnderlyingContractMultiplier);
      FIELD_SET(*this, FIX::UnderlyingUnitOfMeasure);
      FIELD_SET(*this, FIX::UnderlyingUnitOfMeasureQty);
      FIELD_SET(*this, FIX::UnderlyingPriceUnitOfMeasure);
      FIELD_SET(*this, FIX::UnderlyingPriceUnitOfMeasureQty);
      FIELD_SET(*this, FIX::UnderlyingTimeUnit);
      FIELD_SET(*this, FIX::UnderlyingExerciseStyle);
      FIELD_SET(*this, FIX::UnderlyingCouponRate);
      FIELD_SET(*this, FIX::UnderlyingSecurityExchange);
      FIELD_SET(*this, FIX::UnderlyingIssuer);
      FIELD_SET(*this, FIX::EncodedUnderlyingIssuerLen);
      FIELD_SET(*this, FIX::EncodedUnderlyingIssuer);
      FIELD_SET(*this, FIX::UnderlyingSecurityDesc);
      FIELD_SET(*this, FIX::EncodedUnderlyingSecurityDescLen);
      FIELD_SET(*this, FIX::EncodedUnderlyingSecurityDesc);
      FIELD_SET(*this, FIX::UnderlyingCPProgram);
      FIELD_SET(*this, FIX::UnderlyingCPRegType);
      FIELD_SET(*this, FIX::UnderlyingAllocationPercent);
      FIELD_SET(*this, FIX::UnderlyingCurrency);
      FIELD_SET(*this, FIX::UnderlyingQty);
      FIELD_SET(*this, FIX::UnderlyingSettlementType);
      FIELD_SET(*this, FIX::UnderlyingCashAmount);
      FIELD_SET(*this, FIX::UnderlyingCashType);
      FIELD_SET(*this, FIX::UnderlyingPx);
      FIELD_SET(*this, FIX::UnderlyingDirtyPrice);
      FIELD_SET(*this, FIX::UnderlyingEndPrice);
      FIELD_SET(*this, FIX::UnderlyingStartValue);
      FIELD_SET(*this, FIX::UnderlyingCurrentValue);
      FIELD_SET(*this, FIX::UnderlyingEndValue);
      FIELD_SET(*this, FIX::UnderlyingAdjustedQuantity);
      FIELD_SET(*this, FIX::UnderlyingFXRate);
      FIELD_SET(*this, FIX::UnderlyingFXRateCalc);
      FIELD_SET(*this, FIX::UnderlyingCapValue);
      FIELD_SET(*this, FIX::UnderlyingSettlMethod);
      FIELD_SET(*this, FIX::UnderlyingPutOrCall);
      FIELD_SET(*this, FIX::UnderlyingContractMultiplierUnit);
      FIELD_SET(*this, FIX::UnderlyingFlowScheduleType);
      FIELD_SET(*this, FIX::UnderlyingRestructuringType);
      FIELD_SET(*this, FIX::UnderlyingSeniority);
      FIELD_SET(*this, FIX::UnderlyingNotionalPercentageOutstanding);
      FIELD_SET(*this, FIX::UnderlyingOriginalNotionalPercentageOutstanding);
      FIELD_SET(*this, FIX::UnderlyingAttachmentPoint);
      FIELD_SET(*this, FIX::UnderlyingDetachmentPoint);
      FIELD_SET(*this, FIX::NoUnderlyingSecurityAltID);
      class NoUnderlyingSecurityAltID: public FIX::Group
      {
      public:
      NoUnderlyingSecurityAltID() : FIX::Group(457,458,FIX::message_order(458,459,0)) {}
        FIELD_SET(*this, FIX::UnderlyingSecurityAltID);
        FIELD_SET(*this, FIX::UnderlyingSecurityAltIDSource);
      };
      FIELD_SET(*this, FIX::NoUnderlyingStips);
      class NoUnderlyingStips: public FIX::Group
      {
      public:
      NoUnderlyingStips() : FIX::Group(887,888,FIX::message_order(888,889,0)) {}
        FIELD_SET(*this, FIX::UnderlyingStipType);
        FIELD_SET(*this, FIX::UnderlyingStipValue);
      };
      FIELD_SET(*this, FIX::NoUndlyInstrumentParties);
      class NoUndlyInstrumentParties: public FIX::Group
      {
      public:
      NoUndlyInstrumentParties() : FIX::Group(1058,1059,FIX::message_order(1059,1060,1061,1062,0)) {}
        FIELD_SET(*this, FIX::UnderlyingInstrumentPartyID);
        FIELD_SET(*this, FIX::UnderlyingInstrumentPartyIDSource);
        FIELD_SET(*this, FIX::UnderlyingInstrumentPartyRole);
        FIELD_SET(*this, FIX::NoUndlyInstrumentPartySubIDs);
        class NoUndlyInstrumentPartySubIDs: public FIX::Group
        {
        public:
        NoUndlyInstrumentPartySubIDs() : FIX::Group(1062,1063,FIX::message_order(1063,1064,0)) {}
          FIELD_SET(*this, FIX::UnderlyingInstrumentPartySubID);
          FIELD_SET(*this, FIX::UnderlyingInstrumentPartySubIDType);
        };
      };
      FIELD_SET(*this, FIX::QuoteSetValidUntilTime);
      FIELD_SET(*this, FIX::TotNoQuoteEntries);
      FIELD_SET(*this, FIX::LastFragment);
      FIELD_SET(*this, FIX::NoQuoteEntries);
      class NoQuoteEntries: public FIX::Group
      {
      public:
      NoQuoteEntries() : FIX::Group(295,299,FIX::message_order(299,55,65,48,22,460,1227,1151,461,167,762,200,541,1079,966,1049,965,224,225,239,226,227,228,255,543,470,471,472,240,202,947,967,968,206,231,969,1146,996,1147,1191,1192,1193,1194,1195,1196,1197,1198,1199,1200,201,1244,1242,997,223,207,970,971,106,348,349,107,350,351,691,667,875,876,873,874,1435,1439,1449,1450,1451,1452,1457,1458,1478,1479,1480,1481,1482,555,132,133,134,135,62,188,190,189,191,631,632,633,634,60,336,625,64,40,193,192,642,643,15,775,528,529,0)) {}
        FIELD_SET(*this, FIX::QuoteEntryID);
        FIELD_SET(*this, FIX::Symbol);
        FIELD_SET(*this, FIX::SymbolSfx);
        FIELD_SET(*this, FIX::SecurityID);
        FIELD_SET(*this, FIX::SecurityIDSource);
        FIELD_SET(*this, FIX::Product);
        FIELD_SET(*this, FIX::ProductComplex);
        FIELD_SET(*this, FIX::SecurityGroup);
        FIELD_SET(*this, FIX::CFICode);
        FIELD_SET(*this, FIX::SecurityType);
        FIELD_SET(*this, FIX::SecuritySubType);
        FIELD_SET(*this, FIX::MaturityMonthYear);
        FIELD_SET(*this, FIX::MaturityDate);
        FIELD_SET(*this, FIX::MaturityTime);
        FIELD_SET(*this, FIX::SettleOnOpenFlag);
        FIELD_SET(*this, FIX::InstrmtAssignmentMethod);
        FIELD_SET(*this, FIX::SecurityStatus);
        FIELD_SET(*this, FIX::CouponPaymentDate);
        FIELD_SET(*this, FIX::IssueDate);
        FIELD_SET(*this, FIX::RepoCollateralSecurityType);
        FIELD_SET(*this, FIX::RepurchaseTerm);
        FIELD_SET(*this, FIX::RepurchaseRate);
        FIELD_SET(*this, FIX::Factor);
        FIELD_SET(*this, FIX::CreditRating);
        FIELD_SET(*this, FIX::InstrRegistry);
        FIELD_SET(*this, FIX::CountryOfIssue);
        FIELD_SET(*this, FIX::StateOrProvinceOfIssue);
        FIELD_SET(*this, FIX::LocaleOfIssue);
        FIELD_SET(*this, FIX::RedemptionDate);
        FIELD_SET(*this, FIX::StrikePrice);
        FIELD_SET(*this, FIX::StrikeCurrency);
        FIELD_SET(*this, FIX::StrikeMultiplier);
        FIELD_SET(*this, FIX::StrikeValue);
        FIELD_SET(*this, FIX::OptAttribute);
        FIELD_SET(*this, FIX::ContractMultiplier);
        FIELD_SET(*this, FIX::MinPriceIncrement);
        FIELD_SET(*this, FIX::MinPriceIncrementAmount);
        FIELD_SET(*this, FIX::UnitOfMeasure);
        FIELD_SET(*this, FIX::UnitOfMeasureQty);
        FIELD_SET(*this, FIX::PriceUnitOfMeasure);
        FIELD_SET(*this, FIX::PriceUnitOfMeasureQty);
        FIELD_SET(*this, FIX::SettlMethod);
        FIELD_SET(*this, FIX::ExerciseStyle);
        FIELD_SET(*this, FIX::OptPayoutAmount);
        FIELD_SET(*this, FIX::PriceQuoteMethod);
        FIELD_SET(*this, FIX::ValuationMethod);
        FIELD_SET(*this, FIX::ListMethod);
        FIELD_SET(*this, FIX::CapPrice);
        FIELD_SET(*this, FIX::FloorPrice);
        FIELD_SET(*this, FIX::PutOrCall);
        FIELD_SET(*this, FIX::FlexibleIndicator);
        FIELD_SET(*this, FIX::FlexProductEligibilityIndicator);
        FIELD_SET(*this, FIX::TimeUnit);
        FIELD_SET(*this, FIX::CouponRate);
        FIELD_SET(*this, FIX::SecurityExchange);
        FIELD_SET(*this, FIX::PositionLimit);
        FIELD_SET(*this, FIX::NTPositionLimit);
        FIELD_SET(*this, FIX::Issuer);
        FIELD_SET(*this, FIX::EncodedIssuerLen);
        FIELD_SET(*this, FIX::EncodedIssuer);
        FIELD_SET(*this, FIX::SecurityDesc);
        FIELD_SET(*this, FIX::EncodedSecurityDescLen);
        FIELD_SET(*this, FIX::EncodedSecurityDesc);
        FIELD_SET(*this, FIX::Pool);
        FIELD_SET(*this, FIX::ContractSettlMonth);
        FIELD_SET(*this, FIX::CPProgram);
        FIELD_SET(*this, FIX::CPRegType);
        FIELD_SET(*this, FIX::DatedDate);
        FIELD_SET(*this, FIX::InterestAccrualDate);
        FIELD_SET(*this, FIX::ContractMultiplierUnit);
        FIELD_SET(*this, FIX::FlowScheduleType);
        FIELD_SET(*this, FIX::RestructuringType);
        FIELD_SET(*this, FIX::Seniority);
        FIELD_SET(*this, FIX::NotionalPercentageOutstanding);
        FIELD_SET(*this, FIX::OriginalNotionalPercentageOutstanding);
        FIELD_SET(*this, FIX::AttachmentPoint);
        FIELD_SET(*this, FIX::DetachmentPoint);
        FIELD_SET(*this, FIX::StrikePriceDeterminationMethod);
        FIELD_SET(*this, FIX::StrikePriceBoundaryMethod);
        FIELD_SET(*this, FIX::StrikePriceBoundaryPrecision);
        FIELD_SET(*this, FIX::UnderlyingPriceDeterminationMethod);
        FIELD_SET(*this, FIX::OptPayoutType);
        FIELD_SET(*this, FIX::NoSecurityAltID);
        class NoSecurityAltID: public FIX::Group
        {
        public:
        NoSecurityAltID() : FIX::Group(454,455,FIX::message_order(455,456,0)) {}
          FIELD_SET(*this, FIX::SecurityAltID);
          FIELD_SET(*this, FIX::SecurityAltIDSource);
        };
        FIELD_SET(*this, FIX::SecurityXMLLen);
        FIELD_SET(*this, FIX::SecurityXML);
        FIELD_SET(*this, FIX::SecurityXMLSchema);
        FIELD_SET(*this, FIX::NoEvents);
        class NoEvents: public FIX::Group
        {
        public:
        NoEvents() : FIX::Group(864,865,FIX::message_order(865,866,1145,867,868,0)) {}
          FIELD_SET(*this, FIX::EventType);
          FIELD_SET(*this, FIX::EventDate);
          FIELD_SET(*this, FIX::EventTime);
          FIELD_SET(*this, FIX::EventPx);
          FIELD_SET(*this, FIX::EventText);
        };
        FIELD_SET(*this, FIX::NoInstrumentParties);
        class NoInstrumentParties: public FIX::Group
        {
        public:
        NoInstrumentParties() : FIX::Group(1018,1019,FIX::message_order(1019,1050,1051,1052,0)) {}
          FIELD_SET(*this, FIX::InstrumentPartyID);
          FIELD_SET(*this, FIX::InstrumentPartyIDSource);
          FIELD_SET(*this, FIX::InstrumentPartyRole);
          FIELD_SET(*this, FIX::NoInstrumentPartySubIDs);
          class NoInstrumentPartySubIDs: public FIX::Group
          {
          public:
          NoInstrumentPartySubIDs() : FIX::Group(1052,1053,FIX::message_order(1053,1054,0)) {}
            FIELD_SET(*this, FIX::InstrumentPartySubID);
            FIELD_SET(*this, FIX::InstrumentPartySubIDType);
          };
        };
        FIELD_SET(*this, FIX::NoComplexEvents);
        class NoComplexEvents: public FIX::Group
        {
        public:
        NoComplexEvents() : FIX::Group(1483,1484,FIX::message_order(1484,1485,1486,1487,1488,1489,1490,1491,0)) {}
          FIELD_SET(*this, FIX::ComplexEventType);
          FIELD_SET(*this, FIX::ComplexOptPayoutAmount);
          FIELD_SET(*this, FIX::ComplexEventPrice);
          FIELD_SET(*this, FIX::ComplexEventPriceBoundaryMethod);
          FIELD_SET(*this, FIX::ComplexEventPriceBoundaryPrecision);
          FIELD_SET(*this, FIX::ComplexEventPriceTimeType);
          FIELD_SET(*this, FIX::ComplexEventCondition);
          FIELD_SET(*this, FIX::NoComplexEventDates);
          class NoComplexEventDates: public FIX::Group
          {
          public:
          NoComplexEventDates() : FIX::Group(1491,1492,FIX::message_order(1492,1493,1494,0)) {}
            FIELD_SET(*this, FIX::ComplexEventStartDate);
            FIELD_SET(*this, FIX::ComplexEventEndDate);
            FIELD_SET(*this, FIX::NoComplexEventTimes);
            class NoComplexEventTimes: public FIX::Group
            {
            public:
            NoComplexEventTimes() : FIX::Group(1494,1495,FIX::message_order(1495,1496,0)) {}
              FIELD_SET(*this, FIX::ComplexEventStartTime);
              FIELD_SET(*this, FIX::ComplexEventEndTime);
            };
          };
        };
        FIELD_SET(*this, FIX::NoLegs);
        class NoLegs: public FIX::Group
        {
        public:
        NoLegs() : FIX::Group(555,600,FIX::message_order(600,601,602,603,1788,607,608,609,764,610,611,1212,248,249,250,251,252,253,257,599,596,597,598,254,612,942,613,614,999,1224,1421,1422,1001,1420,615,616,617,618,619,620,621,622,623,624,556,740,739,955,956,1358,1017,1436,1440,22041,22049,0)) {}
          FIELD_SET(*this, FIX::LegSymbol);
          FIELD_SET(*this, FIX::LegSymbolSfx);
          FIELD_SET(*this, FIX::LegSecurityID);
          FIELD_SET(*this, FIX::LegSecurityIDSource);
          FIELD_SET(*this, FIX::LegID);
          FIELD_SET(*this, FIX::LegProduct);
          FIELD_SET(*this, FIX::LegCFICode);
          FIELD_SET(*this, FIX::LegSecurityType);
          FIELD_SET(*this, FIX::LegSecuritySubType);
          FIELD_SET(*this, FIX::LegMaturityMonthYear);
          FIELD_SET(*this, FIX::LegMaturityDate);
          FIELD_SET(*this, FIX::LegMaturityTime);
          FIELD_SET(*this, FIX::LegCouponPaymentDate);
          FIELD_SET(*this, FIX::LegIssueDate);
          FIELD_SET(*this, FIX::LegRepoCollateralSecurityType);
          FIELD_SET(*this, FIX::LegRepurchaseTerm);
          FIELD_SET(*this, FIX::LegRepurchaseRate);
          FIELD_SET(*this, FIX::LegFactor);
          FIELD_SET(*this, FIX::LegCreditRating);
          FIELD_SET(*this, FIX::LegInstrRegistry);
          FIELD_SET(*this, FIX::LegCountryOfIssue);
          FIELD_SET(*this, FIX::LegStateOrProvinceOfIssue);
          FIELD_SET(*this, FIX::LegLocaleOfIssue);
          FIELD_SET(*this, FIX::LegRedemptionDate);
          FIELD_SET(*this, FIX::LegStrikePrice);
          FIELD_SET(*this, FIX::LegStrikeCurrency);
          FIELD_SET(*this, FIX::LegOptAttribute);
          FIELD_SET(*this, FIX::LegContractMultiplier);
          FIELD_SET(*this, FIX::LegUnitOfMeasure);
          FIELD_SET(*this, FIX::LegUnitOfMeasureQty);
          FIELD_SET(*this, FIX::LegPriceUnitOfMeasure);
          FIELD_SET(*this, FIX::LegPriceUnitOfMeasureQty);
          FIELD_SET(*this, FIX::LegTimeUnit);
          FIELD_SET(*this, FIX::LegExerciseStyle);
          FIELD_SET(*this, FIX::LegCouponRate);
          FIELD_SET(*this, FIX::LegSecurityExchange);
          FIELD_SET(*this, FIX::LegIssuer);
          FIELD_SET(*this, FIX::EncodedLegIssuerLen);
          FIELD_SET(*this, FIX::EncodedLegIssuer);
          FIELD_SET(*this, FIX::LegSecurityDesc);
          FIELD_SET(*this, FIX::EncodedLegSecurityDescLen);
          FIELD_SET(*this, FIX::EncodedLegSecurityDesc);
          FIELD_SET(*this, FIX::LegRatioQty);
          FIELD_SET(*this, FIX::LegSide);
          FIELD_SET(*this, FIX::LegCurrency);
          FIELD_SET(*this, FIX::LegPool);
          FIELD_SET(*this, FIX::LegDatedDate);
          FIELD_SET(*this, FIX::LegContractSettlMonth);
          FIELD_SET(*this, FIX::LegInterestAccrualDate);
          FIELD_SET(*this, FIX::LegPutOrCall);
          FIELD_SET(*this, FIX::LegOptionRatio);
          FIELD_SET(*this, FIX::LegContractMultiplierUnit);
          FIELD_SET(*this, FIX::LegFlowScheduleType);
          FIELD_SET(*this, FIX::LegDV01);
          FIELD_SET(*this, FIX::LegNotionalNeutral);
          FIELD_SET(*this, FIX::NoLegSecurityAltID);
          class NoLegSecurityAltID: public FIX::Group
          {
          public:
          NoLegSecurityAltID() : FIX::Group(604,605,FIX::message_order(605,606,0)) {}
            FIELD_SET(*this, FIX::LegSecurityAltID);
            FIELD_SET(*this, FIX::LegSecurityAltIDSource);
          };
        };
        FIELD_SET(*this, FIX::BidPx);
        FIELD_SET(*this, FIX::OfferPx);
        FIELD_SET(*this, FIX::BidSize);
        FIELD_SET(*this, FIX::OfferSize);
        FIELD_SET(*this, FIX::ValidUntilTime);
        FIELD_SET(*this, FIX::BidSpotRate);
        FIELD_SET(*this, FIX::OfferSpotRate);
        FIELD_SET(*this, FIX::BidForwardPoints);
        FIELD_SET(*this, FIX::OfferForwardPoints);
        FIELD_SET(*this, FIX::MidPx);
        FIELD_SET(*this, FIX::BidYield);
        FIELD_SET(*this, FIX::MidYield);
        FIELD_SET(*this, FIX::OfferYield);
        FIELD_SET(*this, FIX::TransactTime);
        FIELD_SET(*this, FIX::TradingSessionID);
        FIELD_SET(*this, FIX::TradingSessionSubID);
        FIELD_SET(*this, FIX::SettlDate);
        FIELD_SET(*this, FIX::OrdType);
        FIELD_SET(*this, FIX::SettlDate2);
        FIELD_SET(*this, FIX::OrderQty2);
        FIELD_SET(*this, FIX::BidForwardPoints2);
        FIELD_SET(*this, FIX::OfferForwardPoints2);
        FIELD_SET(*this, FIX::Currency);
        FIELD_SET(*this, FIX::BookingType);
        FIELD_SET(*this, FIX::OrderCapacity);
        FIELD_SET(*this, FIX::OrderRestrictions);
      };
    };
  };

}

#endif

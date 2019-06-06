// Author: Felice Pantaleo - felice.pantaleo@cern.ch
// Date: 09/2018

#ifndef __RecoHGCal_TICL_PRbyMultiClusters_H__
#define __RecoHGCal_TICL_PRbyMultiClusters_H__
#include "RecoHGCal/TICL/interface/PatternRecognitionAlgoBase.h"

#include <iostream>

///
#include "DataFormats/Common/interface/ValueMap.h"

#include "DataFormats/CaloRecHit/interface/CaloClusterFwd.h"
#include "DataFormats/CaloRecHit/interface/CaloCluster.h"
///



namespace edm {
class ParameterSet;
class Event;
class EventSetup;
}

namespace ticl {
  class PatternRecognitionbyMultiClusters final : public PatternRecognitionAlgoBase {
    public:
      PatternRecognitionbyMultiClusters(const edm::ParameterSet& conf)
        : PatternRecognitionAlgoBase(conf) {
        }
      ~PatternRecognitionbyMultiClusters() override {};

      void makeTracksters(const edm::Event& ev, const edm::EventSetup& es,
          const std::vector<reco::CaloCluster>& layerClusters,
	  ///
	  const edm::Handle<std::vector<reco::CaloCluster>> &cluster_h,
	  const edm::ValueMap<float> &TwoDTime,
	  ///
          const ticl::HgcalClusterFilterMask & mask,
          std::vector<Trackster>& result) override;
  };
}
#endif

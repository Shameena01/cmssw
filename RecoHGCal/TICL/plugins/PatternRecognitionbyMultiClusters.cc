#include "PatternRecognitionbyMultiClusters.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

///
#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/CaloRecHit/interface/CaloClusterFwd.h"
#include "DataFormats/CaloRecHit/interface/CaloCluster.h"
///



void ticl::PatternRecognitionbyMultiClusters::makeTracksters(
    const edm::Event& ev, const edm::EventSetup& es,
    const std::vector<reco::CaloCluster>& layerClusters,
    const edm::Handle<std::vector<reco::CaloCluster>> &cluster_h,
    ///
    const edm::ValueMap<float> &TwoDTime,
    ///
    const ticl::HgcalClusterFilterMask & mask, std::vector<Trackster>& result) {
  LogDebug("HGCPatterRecoTrackster") << "making Tracksters" << std::endl;
}

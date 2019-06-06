#include "RecoHGCal/TICLTests/test/TICLAnalyzer.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "DataFormats/CaloRecHit/interface/CaloClusterFwd.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Common/interface/ValueMap.h"
#include <algorithm>

using namespace std;
using namespace edm;
using namespace reco;

TICLAnalyzer::TICLAnalyzer(const edm::ParameterSet& iConfig) :
  genToken_(consumes<std::vector<CaloParticle> >(edm::InputTag("mix:MergedCaloTruth"))),
  simclusToken_(consumes<std::vector<SimCluster> >(edm::InputTag("mix:MergedCaloTruth"))),
  // tkToken_(consumes<std::vector<reco::CaloCluster> >(edm::InputTag("hgcTracks::RECO2"))),
  mcMIPToken_(consumes<std::vector<reco::HGCalMultiCluster> >(edm::InputTag("MultiClustersFromTrackstersMIP:MIPMultiClustersFromTracksterByCA"))),
  mcToken_(consumes<std::vector<reco::HGCalMultiCluster> >(edm::InputTag("MultiClustersFromTracksters:MultiClustersFromTracksterByCA"))),

  _caloClusters(consumes<reco::CaloClusterCollection>(edm::InputTag("hgcalLayerClusters"))),
  _2DClTime(consumes<edm::ValueMap<float> >(edm::InputTag("hgcalLayerClusters","timeLayerCluster"))),
  hits_eeToken_(consumes<HGCRecHitCollection>(edm::InputTag("HGCalRecHit","HGCEERecHits"))),
  hits_fhToken_(consumes<HGCRecHitCollection>(edm::InputTag("HGCalRecHit","HGCHEFRecHits"))),
  hits_bhToken_(consumes<HGCRecHitCollection>(edm::InputTag("HGCalRecHit","HGCHEBRecHits")))
{
  //book some histos here
  TString est[]={"tk","mcMIP","mc","all"};
  TString tit[]={"hgcTracks","trackstersMIP","tracksters2DCl","all"};
  for(size_t i=0; i<sizeof(est)/sizeof(TString); i++){
    histos_["hitsFraction_"+est[i]]    = new TH1F("hitsFraction_"+est[i],  tit[i]+ ";Fraction of gen-matched hits;", 101,0,1.1);
    histos_["noiseFraction_"+est[i]]   = new TH1F("noiseFraction_"+est[i],  tit[i]+ ";Fraction of noise hits;", 101,0,1.1);
    histos_["EFraction_"+est[i]]       = new TH1F("EFraction_"+est[i],  tit[i]+ ";Fraction of gen-matched energy;", 101,0,1.1);
    histos_["noiseEFraction_"+est[i]]  = new TH1F("noiseEFraction_"+est[i],  tit[i]+ ";Fraction of noise energy;", 101,0,1.1);
  }
}



TICLAnalyzer::~TICLAnalyzer() { 
  TFile *outF = TFile::Open("ticl_analysis.root","RECREATE");
  for(std::map<TString,TH1 *>::iterator it=histos_.begin();
      it!=histos_.end();
      it++)
    it->second->Write();
  outF->Close();

}



void TICLAnalyzer::beginRun(const edm::Run& run, 
                            const edm::EventSetup & es) { }


void  TICLAnalyzer::analyze(const Event& iEvent, 
                            const EventSetup& iSetup) {

  edm::Handle<std::vector<CaloParticle> > gpH;
  iEvent.getByToken( genToken_, gpH);

  edm::Handle<std::vector<SimCluster> > scH;
  iEvent.getByToken( simclusToken_, scH);

  //edm::Handle<std::vector<reco::CaloCluster> > tkH;
  //iEvent.getByToken( tkToken_, tkH);

  edm::Handle<std::vector<reco::HGCalMultiCluster> > mcMIPH,mcH;
  iEvent.getByToken( mcMIPToken_,mcMIPH);
  iEvent.getByToken( mcToken_,mcH);


  edm::Handle<HGCRecHitCollection> ee_hits;
  edm::Handle<HGCRecHitCollection> fh_hits;
  edm::Handle<HGCRecHitCollection> bh_hits;
  iEvent.getByToken(hits_eeToken_,ee_hits);
  iEvent.getByToken(hits_fhToken_,fh_hits);
  iEvent.getByToken(hits_bhToken_,bh_hits);


  //2D CLUSTER COLLECTION (all)
  Handle<reco::CaloClusterCollection> caloClusters;
  iEvent.getByToken(_caloClusters, caloClusters);



  

  edm::Handle<edm::ValueMap<float> > TwoDClTimeHandle;
  iEvent.getByToken(_2DClTime, TwoDClTimeHandle);





  std::map<uint32_t, const HGCRecHit*> hitmap;
  for(auto const& it: *ee_hits) hitmap[it.detid().rawId()] = &it;
  for(auto const& it: *fh_hits) hitmap[it.detid().rawId()] = &it;
  for(auto const& it: *bh_hits) hitmap[it.detid().rawId()] = &it;
  

  //looking into TICL Multiclusters
  for (auto trackster:*mcH){
    std::cout<<"the size of the trackster is "<<trackster.size()<<std::endl;
    const edm::PtrVector<reco::BasicCluster> TwoDclusterList = trackster.clusters();//vector of pointers to the 2D in trackster
    // std::cout<<TwoDclusterList.size()<<std::endl;

    float TracksterSize = trackster.size();
    for (int i=0;i<TracksterSize;i++){

    }
   
  }

  for (auto trackster:*mcH){
  //loop over all the layer clusters in the multicluster
    std::cout<<"NEW TRACKSTER"<<std::endl;
    std::cout<<"the size of the trackster is "<<trackster.size()<<std::endl;
    
  for(reco::HGCalMultiCluster::component_iterator it = trackster.begin(); it!=trackster.end(); it++){
    
    //    std::cout<<it->position()->z()<<std::endl;
    

   }
  }





  for(auto cp : *gpH) {
    
    float eta=cp.eta();
    float cpEnergy = cp.energy();

    std::vector<std::pair<uint32_t,float> > allHits;
    //std::vector<uint32_t> allMatched_tk,allNoise_tk;
    std::vector<uint32_t> allMatched_mcMIP,allNoise_mcMIP,allMatched_mc,allNoise_mc,allSimHits;
    //iterate over all the attached sim clusters
    for(CaloParticle::sc_iterator scIt=cp.simCluster_begin();
        scIt!=cp.simCluster_end();
        scIt++) {

      //all hits and energy fractions at sim level
      std::vector<std::pair<uint32_t,float> > hits=scH->at( scIt->key() ).hits_and_fractions();
      allHits.insert(allHits.end(),hits.begin(),hits.end());
      int allHitsSize = allHits.size();
      for (int i=0; i<allHitsSize;i++){
	//std::cout<<allHits[i].first<<std::endl;
        allSimHits.push_back(allHits[i].first);
      }
      //check which ones are matched by HGC tracking
      //std::vector<uint32_t> matched_tk = getTrackedHitsList(eta>0,hits,*tkH);
      //std::vector<uint32_t> noise_tk = getTrackedHitsList(eta>0,hits,*tkH,true);
      //allMatched_tk.insert(allMatched_tk.end(),matched_tk.begin(),matched_tk.end());
      //allNoise_tk.insert(allNoise_tk.end(),noise_tk.begin(),noise_tk.end());

      //check which ones are matched by the multicluster algorithmb
      std::vector<uint32_t> matched_mcMIP=getClusteredHitsList(eta>0,hits,*mcMIPH);
      std::vector<uint32_t> noise_mcMIP=getClusteredHitsList(eta>0,hits,*mcMIPH,true);
      allMatched_mcMIP.insert(allMatched_mcMIP.end(),matched_mcMIP.begin(),matched_mcMIP.end());
      allNoise_mcMIP.insert(allNoise_mcMIP.end(),noise_mcMIP.begin(),noise_mcMIP.end());
      std::vector<uint32_t> matched_mc=getClusteredHitsList(eta>0,hits,*mcH);
      std::vector<uint32_t> noise_mc=getClusteredHitsList(eta>0,hits,*mcMIPH,true);
      allMatched_mc.insert(allMatched_mc.end(),matched_mc.begin(),matched_mc.end());
      allNoise_mc.insert(allNoise_mc.end(),noise_mc.begin(),noise_mc.end());
    }


    //message before removing duplicates
    std::cout<<"BEFORE REMOVING DUPLICATES"<<std::endl;
    std::cout<<"MIP hits matched to SIM = "<<allMatched_mcMIP.size()<<std::endl;
    std::cout<<"Trackster hits matched to SIM = "<<allMatched_mc.size()<<std::endl;
   
    std::cout<<"MIP hits matched to noise SIM = "<<allNoise_mcMIP.size()<<std::endl;
    std::cout<<"Trackster hits matched to noise SIM = "<<allNoise_mc.size()<<std::endl;



    //remove duplicates

    std::vector<uint32_t>::iterator it_MIP;
    std::vector<uint32_t>::iterator it_trkstr;
    std::vector<uint32_t>::iterator it_MIP_noise;
    std::vector<uint32_t>::iterator it_trkstr_noise;

    std::vector<uint32_t>::iterator it_sim;
    std::sort(allSimHits.begin(),allSimHits.end());
    it_sim = std::unique(allSimHits.begin(),allSimHits.end());
    allSimHits.resize(std::distance(allSimHits.begin(),it_sim));



    std::sort(allMatched_mcMIP.begin(), allMatched_mcMIP.end());
    it_MIP = std::unique(allMatched_mcMIP.begin(), allMatched_mcMIP.end());
    allMatched_mcMIP.resize(std::distance(allMatched_mcMIP.begin(),it_MIP));


    std::sort(allMatched_mc.begin(),allMatched_mc.end());
    it_trkstr = std::unique (allMatched_mc.begin(),allMatched_mc.end());
    allMatched_mc.resize(std::distance(allMatched_mc.begin(),it_trkstr));

    std::sort(allNoise_mcMIP.begin(),allNoise_mcMIP.end());
    it_MIP_noise = std::unique(allNoise_mcMIP.begin(),allNoise_mcMIP.end());
    allNoise_mcMIP.resize(std::distance(allNoise_mcMIP.begin(),it_MIP_noise));

    std::sort(allNoise_mc.begin(), allNoise_mc.end());
    it_trkstr_noise = std::unique(allNoise_mc.begin(), allNoise_mc.end());
    allNoise_mc.resize(std::distance(allNoise_mc.begin(),it_trkstr_noise));


   

    //remove duplicates (just in case)---pruneListdoesn't seem to work
    // pruneList(allMatched_tk);
    // pruneList(allMatched_mcMIP);
    //pruneList(allMatched_mc);
    //pruneList(allNoise_tk);
    //pruneList(allNoise_mcMIP);
    //pruneList(allNoise_mc);
    

    std::cout<<"AFTER REMOVING DUPLICATES"<<std::endl;
    std::cout<<"MIP hits matched to SIM = "<<allMatched_mcMIP.size()<<std::endl;
    std::cout<<"Trackster hits matched to SIM = "<<allMatched_mc.size()<<std::endl;

    std::cout<<"MIP hits matched to noise SIM = "<<allNoise_mcMIP.size()<<std::endl;
    std::cout<<"Trackster hits matched to noise SIM = "<<allNoise_mc.size()<<std::endl;


    // float allMatched_tkE = sumUpEnergy(allMatched_tk,hitmap);
    float allMatched_mcMIPE = sumUpEnergy(allMatched_mcMIP,hitmap);
    float allMatched_mcE = sumUpEnergy(allMatched_mc,hitmap);
    //float allNoise_tkE = sumUpEnergy(allNoise_tk,hitmap);
    float allNoise_mcMIPE = sumUpEnergy(allNoise_mcMIP,hitmap);
    float allNoise_mcE = sumUpEnergy(allNoise_mc,hitmap);

    float RecoEallSimH = sumUpEnergy(allSimHits, hitmap);
    std::cout<<"Reco energy of all sim hits is "<<RecoEallSimH<<std::endl;

    
    //all matched hits
    std::vector<uint32_t> allMatched_global;
    allMatched_global.insert(allMatched_global.end(),allMatched_mcMIP.begin(),allMatched_mcMIP.end());
    allMatched_global.insert(allMatched_global.end(),allMatched_mc.begin(),allMatched_mc.end());
    pruneList(allMatched_global);
    float allMatched_globalE = sumUpEnergy(allMatched_global,hitmap);

    //noise hits
    std::vector<uint32_t> allNoise_global;
    allNoise_global.insert(allNoise_global.end(),allNoise_mcMIP.begin(),allNoise_mcMIP.end());
    allNoise_global.insert(allNoise_global.end(),allNoise_mc.begin(),allNoise_mc.end());
    pruneList(allNoise_global);
    float allNoise_globalE = sumUpEnergy(allNoise_global,hitmap);

    if(allMatched_global.size()>allHits.size()) {
      std::cout << cp.pdgId() << " nSimClusters = " << cp.simClusters().size()
                << " no. of sim hits " << allHits.size()
	//<< " tk " << allMatched_tk.size() << "(" << allNoise_tk.size() << ") "
                << " no. mcMIP matched to sim " << allMatched_mcMIP.size() <<  "(noise: " << allNoise_mcMIP.size() << ") "
                << " no. of mc2D hits matched to sim" << allMatched_mc.size() <<  "(noise: " << allNoise_mc.size() << ") "
                << " no. of hits matched to sim = " << allMatched_global.size() << " (noise: " << allNoise_global.size() << ") "
                << " cpE = " << cpEnergy 
	//      << " tkE = " << allMatched_tkE << " (" << allNoise_tkE << ") " 
                << "reco energy of hits in  mcMIP matched to SIM = " << allMatched_mcMIPE << " (noise " << allNoise_mcMIPE << ") " 
                << "reco energy of hits in  mc2D matched to SIM  = " << allMatched_mcE << " (noise " << allNoise_mcE << ") " 
                << "total reco energy in hits matched to sim = " << allMatched_globalE << " (noise " << allNoise_globalE << ") " 
                << std::endl;
    }
    //if(cp.simClusters().size() > 1) continue;

    //histos_["hitsFraction_tk"]->Fill(1.*allMatched_tk.size()/allHits.size());
    histos_["hitsFraction_mcMIP"]->Fill(1.*allMatched_mcMIP.size()/allHits.size());
    histos_["hitsFraction_mc"]->Fill(1.*allMatched_mc.size()/allHits.size());
    histos_["hitsFraction_all"]->Fill(1.*allMatched_global.size()/allHits.size());
    //histos_["EFraction_tk"]->Fill(1.*allMatched_tkE/cpEnergy);
    histos_["EFraction_mcMIP"]->Fill(1.*allMatched_mcMIPE/RecoEallSimH);
    histos_["EFraction_mc"]->Fill(1.*allMatched_mcE/RecoEallSimH);
    histos_["EFraction_all"]->Fill(1.*allMatched_globalE/RecoEallSimH);

    //histos_["noiseFraction_tk"]->Fill(1.*allNoise_tk.size()/allHits.size());
    histos_["noiseFraction_mcMIP"]->Fill(1.*allNoise_mcMIP.size()/allHits.size());
    histos_["noiseFraction_mc"]->Fill(1.*allNoise_mc.size()/allHits.size());
    histos_["noiseFraction_all"]->Fill(1.*allNoise_global.size()/allHits.size());
    //histos_["noiseEFraction_tk"]->Fill(1.*allNoise_tkE/cpEnergy);
    histos_["noiseEFraction_mcMIP"]->Fill(1.*allNoise_mcMIPE/RecoEallSimH);
    histos_["noiseEFraction_mc"]->Fill(1.*allNoise_mcE/RecoEallSimH);
    histos_["noiseEFraction_all"]->Fill(1.*allNoise_globalE/RecoEallSimH);

    if(allMatched_globalE/RecoEallSimH > 1.) std::cout << " problem " << std::endl;
  }
}


//
float TICLAnalyzer::sumUpEnergy(std::vector<uint32_t> &detIdColl, std::map<uint32_t, const HGCRecHit*> &hitmap){
  
  float totalEn(0);
  int nmissed(0);
  std::map<uint32_t, const HGCRecHit*>::iterator it=hitmap.end();
  for(auto ij : detIdColl) {

    //check if it exists
    it=hitmap.find(ij);
    if(it==hitmap.end()) {     
      nmissed++; 
      continue;
    }

    totalEn+=it->second->energy();
  }

  if(nmissed>0) 
    std::cout << nmissed << " hits were not found ?! "<< std::endl;
 
  return totalEn;
}


//
std::vector<uint32_t> TICLAnalyzer::getClusteredHitsList(bool pos,
                                                         const std::vector<std::pair<uint32_t,float> > &hits,
                                                         const std::vector<reco::HGCalMultiCluster> &mcs,
                                                         bool doNoise) {
  
  std::vector<uint32_t> matchedList;
  
  for(auto mc : mcs) {
    
    //require on the same side
    bool mcPos(mc.eta()>0);
    if(mcPos^pos) continue;
    
    //loop over all the layer clusters in the multicluster
    for(reco::HGCalMultiCluster::component_iterator it = mc.begin(); it!=mc.end(); it++){
      const std::vector< std::pair<DetId, float> > &recHits = (*it)->hitsAndFractions();
      std::vector<uint32_t> imatches=getMatched(hits,recHits,doNoise);
      matchedList.insert(matchedList.end(), imatches.begin(), imatches.end());
    }
    
  }

  return matchedList;
}


//
std::vector<uint32_t> TICLAnalyzer::getTrackedHitsList(bool pos,
                                                       const std::vector<std::pair<uint32_t,float> >  &hits,
                                                       const std::vector<reco::CaloCluster> &ccs,
                                                       bool doNoise) {
  
  std::vector<uint32_t> matchedList;
  
  for(auto cc : ccs) {
    
    //require on the same side
    bool ccPos(cc.eta()>0);
    if(ccPos^pos) continue;
    
    const std::vector< std::pair<DetId, float> > &recHits =cc.hitsAndFractions();
    std::vector<uint32_t> imatches=getMatched(hits,recHits,doNoise);
    matchedList.insert(matchedList.end(), imatches.begin(), imatches.end());
    
  }
  
  return matchedList;  
}

//
std::vector<uint32_t> TICLAnalyzer::getMatched(const std::vector<std::pair<uint32_t,float> > &a,
                                               const std::vector<std::pair<DetId,float> > &b,
                                               bool invert){

  std::vector<uint32_t> selHitList;
  for(size_t i=0; i<a.size(); i++) {

    //if the energy fraction is 0 we shouldn't care about this hit...
    //not sure though why it should be attached in the first place
    if(a[i].second<=0) continue;

    //find first match in second list
    bool isMatched(false);
    for(size_t j=0; j<b.size(); j++) {
      if(a[i].first!=b[j].first.rawId()) continue;
      isMatched=true;
      break;
    }

    //add to the list of selected hits
    if(invert^isMatched) selHitList.push_back(a[i].first);
  }

  return selHitList;
}





DEFINE_FWK_MODULE(TICLAnalyzer);

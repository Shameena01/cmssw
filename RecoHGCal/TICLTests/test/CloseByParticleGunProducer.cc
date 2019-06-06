#include <ostream>

#include "IOMC/ParticleGuns/interface/CloseByParticleGunProducer.h"

#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/RandomNumberGenerator.h"

#include "CLHEP/Random/RandFlat.h"

using namespace edm;
using namespace std;

CloseByParticleGunProducer::CloseByParticleGunProducer(const ParameterSet& pset) : 
   BaseFlatGunProducer(pset)
{

  ParameterSet defpset ;
  ParameterSet pgun_params = 
    pset.getParameter<ParameterSet>("PGunParameters") ;
  
  fEn = pgun_params.getParameter<double>("En");
  fR = pgun_params.getParameter<double>("R");
  fPartIDs = pgun_params.getParameter< vector<int> >("PartID");
  
  produces<HepMCProduct>("unsmeared");
  produces<GenEventInfoProduct>();
}

CloseByParticleGunProducer::~CloseByParticleGunProducer()
{
   // no need to cleanup GenEvent memory - done in HepMCProduct
}

void CloseByParticleGunProducer::produce(Event &e, const EventSetup& es) 
{
   edm::Service<edm::RandomNumberGenerator> rng;
   CLHEP::HepRandomEngine* engine = &rng->getEngine(e.streamID());

   if ( fVerbosity > 0 )
     {
       cout << " CloseByParticleGunProducer : Begin New Event Generation" << endl ; 
     }
   // event loop (well, another step in it...)
   
   // no need to clean up GenEvent memory - done in HepMCProduct
   // 
   
   // here re-create fEvt (memory)
   //
   fEvt = new HepMC::GenEvent() ;
   
   // now actualy, cook up the event from PDGTable and gun parameters
   //

   // loop over particles
   //
   int barcode = 1 ;
   for (unsigned int ip=0; ip<fPartIDs.size(); ++ip)
   {

     int PartID = fPartIDs[ip] ;
     const HepPDT::ParticleData *PData = fPDGTable->particle(HepPDT::ParticleID(abs(PartID))) ;
     double mass   = PData->mass().value() ;
     double mom    = sqrt(fEn*fEn-mass*mass);
     double px     = 0.;
     double py     = 0.;
     double pz     = mom;
     double energy = fEn;
     
     HepMC::FourVector p(px,py,pz,energy) ;
     HepMC::GenParticle* Part = new HepMC::GenParticle(p,PartID,1);
     Part->suggest_barcode( barcode ) ;
     barcode++ ;

     double phi = CLHEP::RandFlat::shoot(engine, -3.14159265358979323846, 3.14159265358979323846);
     double x=fR*cos(phi);
     double y=fR*sin(phi);
     HepMC::GenVertex* Vtx = new HepMC::GenVertex(HepMC::FourVector(x,y,0.));
     Vtx->add_particle_out(Part);
     fEvt->add_vertex(Vtx) ;
   }


   fEvt->set_event_number(e.id().event()) ;
   fEvt->set_signal_process_id(20) ; 
   
   if ( fVerbosity > 0 )
   {
      fEvt->print() ;  
   }

   unique_ptr<HepMCProduct> BProduct(new HepMCProduct()) ;
   BProduct->addHepMCData( fEvt );
   e.put(std::move(BProduct), "unsmeared");

   unique_ptr<GenEventInfoProduct> genEventInfo(new GenEventInfoProduct(fEvt));
   e.put(std::move(genEventInfo));

   if ( fVerbosity > 0 )
     {
       cout << " CloseByParticleGunProducer : Event Generation Done " << endl;
     }
}


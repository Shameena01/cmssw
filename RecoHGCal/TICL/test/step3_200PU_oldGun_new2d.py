# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --datatier GEN-SIM-RECO --runUnscheduled --conditions auto:run1_mc -s RAW2DIGI,L1Reco,RECO,RECOSIM --eventcontent FEVTDEBUGHLT -n 100 --era Phase2C4 --geometry Extended2023D28 --filein file:RECO_22E30_VtxZ320_LowEta_106_100.root --fileout file:step3.root --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RECO2',eras.Phase2C4)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2023D28Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.RecoSim_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('RecoLocalCalo.HGCalRecProducers.hgcalLayerClusters_cff')
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(500)
)

process.hgcalLayerClusters_step = cms.Path(process.hgcalLayerClusters)





# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
#'file:RECO_22E30_VtxZ320_LowEta_106_100.root'),
'/store/relval/CMSSW_10_6_0_pre4/RelValPhotonGunPt8To150/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/20000/FFFD7990-7D9D-334D-B822-561E29E0747E.root', '/store/relval/CMSSW_10_6_0_pre4/RelValPhotonGunPt8To150/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/20000/FFFD7990-7D9D-334D-B822-561E29E0747E.root','/store/relval/CMSSW_10_6_0_pre4/RelValPhotonGunPt8To150/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/20000/FFFD7990-7D9D-334D-B822-561E29E0747E.root','/store/relval/CMSSW_10_6_0_pre4/RelValPhotonGunPt8To150/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/20000/FFFD7990-7D9D-334D-B822-561E29E0747E.root','/store/relval/CMSSW_10_6_0_pre4/RelValPhotonGunPt8To150/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/20000/FFFD7990-7D9D-334D-B822-561E29E0747E.root','/store/relval/CMSSW_10_6_0_pre4/RelValPhotonGunPt8To150/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/20000/FFFD7990-7D9D-334D-B822-561E29E0747E.root','/store/relval/CMSSW_10_6_0_pre4/RelValPhotonGunPt8To150/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/20000/FFFD7990-7D9D-334D-B822-561E29E0747E.root','/store/relval/CMSSW_10_6_0_pre4/RelValPhotonGunPt8To150/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/20000/FFFD7990-7D9D-334D-B822-561E29E0747E.root','/store/relval/CMSSW_10_6_0_pre4/RelValPhotonGunPt8To150/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/20000/FFFD7990-7D9D-334D-B822-561E29E0747E.root'),




    secondaryFileNames = cms.untracked.vstring()
)



process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3_200PU_new2d_oldGun_withOUTTimeDoublet.root'),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)




# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run1_mc', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.recosim_step = cms.Path(process.recosim)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)





##TICL customization
from ticl_iterations import TICL_iterations_withReco
process = TICL_iterations_withReco(process)





# Schedule definition
process.schedule = cms.Schedule(process.hgcalLayerClusters_step,process.TICL,process.endjob_step,process.FEVTDEBUGHLToutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)



#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)


# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

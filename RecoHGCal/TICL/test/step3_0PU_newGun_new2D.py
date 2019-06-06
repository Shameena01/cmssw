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
    input = cms.untracked.int32(2000)
)

process.hgcalLayerClusters_step = cms.Path(process.hgcalLayerClusters)





# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
#'file:RECO_22E30_VtxZ320_LowEta_106_100.root'),

'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_1.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_155.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_211.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_43.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_10.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_156.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_212.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_44.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_100.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_157.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_213.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_45.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_101.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_158.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_214.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_46.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_102.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_159.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_215.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_47.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_103.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_16.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_216.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_48.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_104.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_160.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_217.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_49.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_105.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_161.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_218.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_5.root',
##'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_106.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_162.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_219.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_50.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_107.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_163.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_22.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_51.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_108.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_164.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_220.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_52.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_109.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_165.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_221.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_53.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_11.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_166.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_222.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_54.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_110.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_167.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_223.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_55.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_111.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_168.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_224.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_56.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_112.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_169.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_225.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_57.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_113.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_17.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_226.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_58.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_114.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_170.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_227.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_59.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_115.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_171.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_228.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_6.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_116.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_172.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_229.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_60.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_117.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_173.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_23.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_61.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_118.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_174.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_230.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_62.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_119.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_175.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_231.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_63.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_12.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_176.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_232.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_64.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_120.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_177.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_233.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_65.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_121.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_178.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_234.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_66.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_122.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_179.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_235.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_67.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_123.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_18.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_236.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_68.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_124.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_180.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_237.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_69.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_125.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_181.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_238.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_7.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_126.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_182.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_239.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_70.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_127.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_183.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_24.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_71.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_128.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_184.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_240.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_72.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_129.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_185.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_241.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_73.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_13.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_186.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_242.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_74.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_130.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_187.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_243.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_75.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_131.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_188.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_244.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_76.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_132.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_189.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_245.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_77.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_133.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_19.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_246.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_78.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_134.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_190.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_247.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_79.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_135.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_191.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_248.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_8.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_136.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_192.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_249.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_80.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_137.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_193.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_25.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_81.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_138.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_195.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_250.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_82.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_139.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_196.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_26.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_83.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_14.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_197.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_27.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_84.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_140.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_198.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_28.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_85.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_141.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_199.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_29.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_86.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_142.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_2.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_3.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_87.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_143.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_20.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_30.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_88.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_144.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_200.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_31.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_89.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_145.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_201.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_33.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_9.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_146.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_202.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_34.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_90.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_147.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_203.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_35.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_91.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_148.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_204.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_36.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_92.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_149.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_205.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_37.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_93.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_15.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_206.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_38.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_94.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_150.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_207.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_39.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_95.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_151.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_208.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_4.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_96.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_152.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_209.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_40.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_97.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_153.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_21.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_41.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_98.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_154.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_210.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_42.root',
'file:/eos/cms/store/group/dpg_hgcal/comm_hgcal/amartell/HGCAL_Timing_vtxStudies/RECO_22E30_VtxZ320_LowEta_106/RECO_22E30_VtxZ320_LowEta_106_99.root'),


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
    fileName = cms.untracked.string('file:step3_new2d_newGun_withOUTTimeDoublet.root'),
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

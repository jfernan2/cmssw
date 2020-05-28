import FWCore.ParameterSet.Config as cms

# last update: $Date: 2012/08/23 13:38:14 $ by $Author: demattia $

# AlCaReco sequence definitions:

###############################################################
# Tracker Alignment
###############################################################
# AlCaReco for track based alignment using ZMuMu events
from Alignment.CommonAlignmentProducer.ALCARECOTkAlZMuMu_cff import *
# AlCaReco for track based alignment using ZMuMu events for PA data-taking
from Alignment.CommonAlignmentProducer.ALCARECOTkAlZMuMuPA_cff import *
# AlCaReco for track based alignment using Cosmic muon events
from Alignment.CommonAlignmentProducer.ALCARECOTkAlCosmicsInCollisions_cff import *
from Alignment.CommonAlignmentProducer.ALCARECOTkAlCosmics_cff import *
from Alignment.CommonAlignmentProducer.ALCARECOTkAlCosmicsHLT_cff import *
from Alignment.CommonAlignmentProducer.ALCARECOTkAlCosmics0T_cff import *
from Alignment.CommonAlignmentProducer.ALCARECOTkAlCosmics0THLT_cff import *
# AlCaReco for track based alignment using isoMu events
from Alignment.CommonAlignmentProducer.ALCARECOTkAlMuonIsolated_cff import *
# AlCaReco for track based alignment using isoMu events for PA data-taking
from Alignment.CommonAlignmentProducer.ALCARECOTkAlMuonIsolatedPA_cff import *
# AlCaReco for track based alignment using J/Psi events
from Alignment.CommonAlignmentProducer.ALCARECOTkAlJpsiMuMu_cff import *
# AlCaReco for track based alignment using Upsilon events
from Alignment.CommonAlignmentProducer.ALCARECOTkAlUpsilonMuMu_cff import *
# AlCaReco for track based alignment using Upsilon events for PA data-taking
from Alignment.CommonAlignmentProducer.ALCARECOTkAlUpsilonMuMuPA_cff import *
# AlCaReco for track based alignment using MinBias events
from Alignment.CommonAlignmentProducer.ALCARECOTkAlMinBias_cff import *

###############################################################
# Tracker Calibration
###############################################################
# AlCaReco for pixel calibration using muons
from Calibration.TkAlCaRecoProducers.ALCARECOSiPixelCalSingleMuon_cff import *
from Calibration.TkAlCaRecoProducers.ALCARECOSiPixelCalCosmics_cff import *
# AlCaReco for tracker calibration using MinBias events
from Calibration.TkAlCaRecoProducers.ALCARECOSiStripCalMinBias_cff import *
from Calibration.TkAlCaRecoProducers.ALCARECOSiStripCalMinBiasAAG_cff import *
# AlCaReco for tracker ageing monitoring
from Calibration.TkAlCaRecoProducers.ALCARECOSiStripCalSmallBiasScan_cff import *
# AlCaReco for tracker calibration using ZeroBias events (noise)
from Calibration.TkAlCaRecoProducers.ALCARECOSiStripCalZeroBias_cff import *
# AlCaReco for SiPixel Bad Components using ZeroBias events in ExpressPhysics stream
from CalibTracker.SiPixelQuality.ALCARECOSiPixelCalZeroBias_cff import *
# AlCaReco for tracker calibration using Cosmics events 
from Calibration.TkAlCaRecoProducers.ALCARECOSiStripCalCosmics_cff import *

###############################################################
# LUMI Calibration
###############################################################
# AlCaReco for A stream (PD=MinBias)
from Calibration.LumiAlCaRecoProducers.ALCARECOLumiPixelsMinBias_cff import *
from Calibration.LumiAlCaRecoProducers.ALCARECOAlCaPCCZeroBiasFromRECO_cff import *
from Calibration.LumiAlCaRecoProducers.ALCARECOAlCaPCCRandomFromRECO_cff import *

###############################################################
# ECAL Calibration
###############################################################
# ECAL calibration with isol. electrons
# -- alcareco
from Calibration.EcalAlCaRecoProducers.ALCARECOEcalCalIsolElectron_cff import *
# -- alcaraw
from Calibration.EcalAlCaRecoProducers.ALCARECOEcalUncalIsolElectron_cff import *
# -- alcarereco (rereco done starting from alcaraw
#from Calibration.EcalAlCaRecoProducers.ALCARECOEcalRecalIsolElectron_cff import *
from Calibration.EcalAlCaRecoProducers.ALCARECOEcalESAlign_cff import *
# -- alcareco for trigger studies
from Calibration.EcalAlCaRecoProducers.ALCARECOEcalTrg_cff import *
# -- alcareco which selects RAW from test enables
from Calibration.EcalAlCaRecoProducers.ALCARECOEcalTestPulsesRaw_cff import *

###############################################################
# HCAL Calibration
###############################################################
# HCAL calibration with dijets
from Calibration.HcalAlCaRecoProducers.ALCARECOHcalCalDijets_cff import *
# HCAL calibration with gamma+jet (obsolete)
from Calibration.HcalAlCaRecoProducers.ALCARECOHcalCalGammaJet_cff import *
# HCAL calibration from HO (muons)
#  include "Calibration/HcalAlCaRecoProducers/data/ALCARECOHcalCalZMuMu.cff"
from Calibration.HcalAlCaRecoProducers.ALCARECOHcalCalHO_cff import *
from Calibration.HcalAlCaRecoProducers.ALCARECOHcalCalHOCosmics_cff import *
# HCAL isotrack
from Calibration.HcalAlCaRecoProducers.ALCARECOHcalCalIsoTrk_cff import *
from Calibration.HcalAlCaRecoProducers.ALCARECOHcalCalIsoTrkFilter_cff import *
# HCAL noise
from Calibration.HcalAlCaRecoProducers.ALCARECOHcalCalNoise_cff import *
#HCAL calibration iterative PhiSym
from Calibration.HcalAlCaRecoProducers.ALCARECOHcalCalIterativePhiSym_cff import *
# HCAL isolated bunch
from Calibration.HcalAlCaRecoProducers.ALCARECOHcalCalIsolatedBunchFilter_cff import *
from Calibration.HcalAlCaRecoProducers.ALCARECOHcalCalIsolatedBunchSelector_cff import *
# HCAL calibration with muons in HB/HE
from Calibration.HcalAlCaRecoProducers.ALCARECOHcalCalHBHEMuonFilter_cff import *
# HCAL calibration with muons at low luminosity in HB/HE
from Calibration.HcalAlCaRecoProducers.ALCARECOHcalCalLowPUHBHEMuonFilter_cff import *
# HCAL calibration with muons in HE high eta
from Calibration.HcalAlCaRecoProducers.ALCARECOHcalCalHEMuonFilter_cff import *

###############################################################
# Muon alignment
###############################################################
# Muon Alignment with cosmics
from Alignment.CommonAlignmentProducer.ALCARECOMuAlGlobalCosmicsInCollisions_cff import *
from Alignment.CommonAlignmentProducer.ALCARECOMuAlGlobalCosmics_cff import *
# Muon Alignment/Calibration with isolated muons
from Alignment.CommonAlignmentProducer.ALCARECOMuAlCalIsolatedMu_cff import *
# Muon Alignment using ZMuMu events
from Alignment.CommonAlignmentProducer.ALCARECOMuAlZMuMu_cff import *
# Muon Alignment using CSC overlaps
from Alignment.CommonAlignmentProducer.ALCARECOMuAlOverlaps_cff import *
###############################################################
# RPC calibration
###############################################################
from CalibMuon.RPCCalibration.ALCARECORpcCalHLT_cff import *


###############################################################
# nonbeam alcas
###############################################################
from Alignment.CommonAlignmentProducer.ALCARECOTkAlBeamHalo_cff import *
from Alignment.CommonAlignmentProducer.ALCARECOTkAlLAS_cff import *
from Alignment.CommonAlignmentProducer.ALCARECOMuAlBeamHalo_cff import *
from Alignment.CommonAlignmentProducer.ALCARECOMuAlBeamHaloOverlaps_cff import *

###############################################################
# stream for prompt-calibration @ Tier0
###############################################################
from Calibration.TkAlCaRecoProducers.ALCARECOPromptCalibProd_cff import *
from Calibration.TkAlCaRecoProducers.ALCARECOPromptCalibProdBeamSpotHP_cff import *
from Calibration.TkAlCaRecoProducers.ALCARECOPromptCalibProdBeamSpotHPLowPU_cff import *

from Calibration.TkAlCaRecoProducers.ALCARECOPromptCalibProdSiStrip_cff import *
from Calibration.TkAlCaRecoProducers.ALCARECOPromptCalibProdSiStripGains_cff import *
from Calibration.TkAlCaRecoProducers.ALCARECOPromptCalibProdSiStripGainsAAG_cff import *

from Calibration.TkAlCaRecoProducers.ALCARECOSiStripPCLHistos_cff import *
from Alignment.CommonAlignmentProducer.ALCARECOPromptCalibProdSiPixelAli_cff import *

from CalibTracker.SiPixelQuality.ALCARECOPromptCalibProdSiPixel_cff import *

from Calibration.EcalCalibAlgos.ALCARECOPromptCalibProdEcalPedestals_cff import *
from Calibration.LumiAlCaRecoProducers.ALCARECOPromptCalibProdLumiPCC_cff import *
###############################################################
# hotline skim workflows
###############################################################
from Calibration.Hotline.hotlineSkims_cff import *

# NOTE: the ALCARECO DQM modules can not be placed together in a single path
# because the non-DQM sequences act as filters.
# They are therefore inserted per ALCARECO path.
from DQMOffline.Configuration.AlCaRecoDQM_cff import *

# AlCaReco path definitions:

pathALCARECOTkAlZMuMu = cms.Path(seqALCARECOTkAlZMuMu*ALCARECOTkAlZMuMuDQM)
pathALCARECOTkAlZMuMuPA = cms.Path(seqALCARECOTkAlZMuMuPA*ALCARECOTkAlZMuMuPADQM)
pathALCARECOTkAlMuonIsolated = cms.Path(seqALCARECOTkAlMuonIsolated*ALCARECOTkAlMuonIsolatedDQM)
pathALCARECOTkAlMuonIsolatedPA = cms.Path(seqALCARECOTkAlMuonIsolatedPA*ALCARECOTkAlMuonIsolatedPADQM)
pathALCARECOTkAlJpsiMuMu = cms.Path(seqALCARECOTkAlJpsiMuMu*ALCARECOTkAlJpsiMuMuDQM)
pathALCARECOTkAlUpsilonMuMu = cms.Path(seqALCARECOTkAlUpsilonMuMu*ALCARECOTkAlUpsilonMuMuDQM)
pathALCARECOTkAlUpsilonMuMuPA = cms.Path(seqALCARECOTkAlUpsilonMuMuPA*ALCARECOTkAlUpsilonMuMuPADQM)
pathALCARECOTkAlMinBias = cms.Path(seqALCARECOTkAlMinBias*ALCARECOTkAlMinBiasDQM)
pathALCARECOTkAlMinBias = cms.Path(seqALCARECOTkAlMinBias*ALCARECOTkAlMinBiasDQM)
pathALCARECOSiPixelCalSingleMuon = cms.Path(seqALCARECOSiPixelCalSingleMuon)
pathALCARECOSiPixelCalCosmics = cms.Path(seqALCARECOSiPixelCalCosmics)
pathALCARECOSiStripCalMinBias = cms.Path(seqALCARECOSiStripCalMinBias*ALCARECOSiStripCalMinBiasDQM)
pathALCARECOSiStripCalCosmics = cms.Path(seqALCARECOSiStripCalCosmics)
pathALCARECOSiStripCalMinBiasAAG = cms.Path(seqALCARECOSiStripCalMinBiasAAG*ALCARECOSiStripCalMinBiasAAGDQM)
pathALCARECOSiStripCalSmallBiasScan = cms.Path(seqALCARECOSiStripCalSmallBiasScan)
pathALCARECOSiStripCalZeroBias = cms.Path(seqALCARECOSiStripCalZeroBias*ALCARECOSiStripCalZeroBiasDQM)
pathALCARECOSiPixelCalZeroBias = cms.Path(seqALCARECOSiPixelCalZeroBias)

pathALCARECOLumiPixelsMinBias       = cms.Path(seqALCARECOLumiPixelsMinBias)
pathALCARECOAlCaPCCZeroBiasFromRECO = cms.Path(seqALCARECOAlCaPCCZeroBiasFromRECO)
pathALCARECOAlCaPCCRandomFromRECO   = cms.Path(seqALCARECOAlCaPCCRandomFromRECO)

#### ECAL
pathALCARECOEcalCalZElectron     = cms.Path(seqALCARECOEcalCalZElectron)
pathALCARECOEcalCalZSCElectron   = cms.Path(seqALCARECOEcalCalZSCElectron)
pathALCARECOEcalCalWElectron     = cms.Path(seqALCARECOEcalCalWElectron)
pathALCARECOEcalUncalZElectron   = cms.Path(seqALCARECOEcalUncalZElectron)
pathALCARECOEcalUncalZSCElectron = cms.Path(seqALCARECOEcalUncalZSCElectron)
pathALCARECOEcalUncalWElectron   = cms.Path(seqALCARECOEcalUncalWElectron)
pathALCARECOEcalTestPulsesRaw    = cms.Path(seqALCARECOEcalTestPulsesRaw)

#### Not meant to be used for central production
#pathALCARECOEcalRecalElectron = cms.Path(seqALCARECOEcalRecalElectron)

pathALCARECOEcalESAlign      = cms.Path(seqEcalESAlign)
pathALCARECOEcalTrg          = cms.Path(seqALCARECOEcalTrg)
####
pathALCARECOHcalCalDijets = cms.Path(seqALCARECOHcalCalDijets*ALCARECOHcalCalDiJetsDQM)
pathALCARECOHcalCalGammaJet = cms.Path(seqALCARECOHcalCalGammaJet)
pathALCARECOHcalCalHO = cms.Path(seqALCARECOHcalCalHO*ALCARECOHcalCalHODQM)
pathALCARECOHcalCalHOCosmics = cms.Path(seqALCARECOHcalCalHOCosmics)
pathALCARECOHcalCalIsoTrk = cms.Path(seqALCARECOHcalCalIsoTrk*ALCARECOHcalCalIsoTrackDQM)
pathALCARECOHcalCalIsoTrkFilter = cms.Path(seqALCARECOHcalCalIsoTrkFilter)
pathALCARECOHcalCalNoise = cms.Path(seqALCARECOHcalCalNoise)
pathALCARECOHcalCalIterativePhiSym = cms.Path(seqALCARECOHcalCalIterativePhiSym*ALCARECOHcalCalPhisymDQM)
pathALCARECOHcalCalIsolatedBunchFilter = cms.Path(seqALCARECOHcalCalIsolatedBunchFilter)
pathALCARECOHcalCalIsolatedBunchSelector = cms.Path(seqALCARECOHcalCalIsolatedBunchSelector*ALCARECOHcalCalIsolatedBunchDQM)
pathALCARECOHcalCalHBHEMuonFilter = cms.Path(seqALCARECOHcalCalHBHEMuonFilter)
pathALCARECOHcalCalLowPUHBHEMuonFilter = cms.Path(seqALCARECOHcalCalLowPUHBHEMuonFilter)
pathALCARECOHcalCalHEMuonFilter = cms.Path(seqALCARECOHcalCalHEMuonFilter)
pathALCARECOMuAlCalIsolatedMu = cms.Path(seqALCARECOMuAlCalIsolatedMu)
pathALCARECOMuAlCalIsolatedMuGeneralTracks = cms.Path(seqALCARECOMuAlCalIsolatedMuGeneralTracks)
pathALCARECOMuAlZMuMu = cms.Path(seqALCARECOMuAlZMuMu)
pathALCARECOMuAlZMuMuGeneralTracks = cms.Path(seqALCARECOMuAlZMuMuGeneralTracks)
pathALCARECOMuAlOverlaps = cms.Path(seqALCARECOMuAlOverlaps)
pathALCARECOMuAlOverlapsGeneralTracks = cms.Path(seqALCARECOMuAlOverlapsGeneralTracks)
pathALCARECORpcCalHLT = cms.Path(seqALCARECORpcCalHLT)
pathALCARECOTkAlBeamHalo = cms.Path(seqALCARECOTkAlBeamHalo*ALCARECOTkAlBeamHaloDQM)
pathALCARECOMuAlBeamHaloOverlaps = cms.Path(seqALCARECOMuAlBeamHaloOverlaps)
pathALCARECOMuAlBeamHalo = cms.Path(seqALCARECOMuAlBeamHalo)
pathALCARECOTkAlLAS = cms.Path(seqALCARECOTkAlLAS*ALCARECOTkAlLASDQM)
pathALCARECOTkAlCosmicsInCollisions = cms.Path(seqALCARECOTkAlCosmicsInCollisions*ALCARECOTkAlCosmicsInCollisionsDQM)
pathALCARECOTkAlCosmicsCTF = cms.Path(seqALCARECOTkAlCosmicsCTF*ALCARECOTkAlCosmicsCTFDQM)
pathALCARECOTkAlCosmicsCosmicTF = cms.Path(seqALCARECOTkAlCosmicsCosmicTF*ALCARECOTkAlCosmicsCosmicTFDQM)
pathALCARECOTkAlCosmicsRegional = cms.Path(seqALCARECOTkAlCosmicsRegional*ALCARECOTkAlCosmicsRegionalDQM)
pathALCARECOTkAlCosmicsCTF0T = cms.Path(seqALCARECOTkAlCosmicsCTF0T*ALCARECOTkAlCosmicsCTF0TDQM)
pathALCARECOTkAlCosmicsCosmicTF0T = cms.Path(seqALCARECOTkAlCosmicsCosmicTF0T*ALCARECOTkAlCosmicsCosmicTF0TDQM)
pathALCARECOTkAlCosmicsRegional0T = cms.Path(seqALCARECOTkAlCosmicsRegional0T*ALCARECOTkAlCosmicsRegional0TDQM)
pathALCARECOTkAlCosmicsCTFHLT = cms.Path(seqALCARECOTkAlCosmicsCTFHLT*ALCARECOTkAlCosmicsCTFDQM)
pathALCARECOTkAlCosmicsCosmicTFHLT = cms.Path(seqALCARECOTkAlCosmicsCosmicTFHLT*ALCARECOTkAlCosmicsCosmicTFDQM)
pathALCARECOTkAlCosmicsRegionalHLT = cms.Path(seqALCARECOTkAlCosmicsRegionalHLT*ALCARECOTkAlCosmicsRegionalDQM)
pathALCARECOTkAlCosmicsCTF0THLT = cms.Path(seqALCARECOTkAlCosmicsCTF0THLT*ALCARECOTkAlCosmicsCTF0TDQM)
pathALCARECOTkAlCosmicsCosmicTF0THLT = cms.Path(seqALCARECOTkAlCosmicsCosmicTF0THLT*ALCARECOTkAlCosmicsCosmicTF0TDQM)
pathALCARECOTkAlCosmicsRegional0THLT = cms.Path(seqALCARECOTkAlCosmicsRegional0THLT*ALCARECOTkAlCosmicsRegional0TDQM)
pathALCARECOMuAlGlobalCosmicsInCollisions = cms.Path(seqALCARECOMuAlGlobalCosmicsInCollisions)
pathALCARECOMuAlGlobalCosmics = cms.Path(seqALCARECOMuAlGlobalCosmics)
pathALCARECOPromptCalibProd = cms.Path(seqALCARECOPromptCalibProd)
pathALCARECOPromptCalibProdBeamSpotHP = cms.Path(seqALCARECOPromptCalibProdBeamSpotHP)
pathALCARECOPromptCalibProdBeamSpotHPLowPU = cms.Path(seqALCARECOPromptCalibProdBeamSpotHPLowPU)
pathALCARECOPromptCalibProdSiStrip = cms.Path(seqALCARECOPromptCalibProdSiStrip)
pathALCARECOPromptCalibProdSiStripGains = cms.Path(seqALCARECOPromptCalibProdSiStripGains)
pathALCARECOPromptCalibProdSiStripGainsAAG = cms.Path(seqALCARECOPromptCalibProdSiStripGainsAAG)
pathALCARECOPromptCalibProdSiPixelAli = cms.Path(seqALCARECOPromptCalibProdSiPixelAli)
pathALCARECOPromptCalibProdSiPixel = cms.Path(seqALCARECOPromptCalibProdSiPixel)
pathALCARECOPromptCalibProdEcalPedestals = cms.Path(seqALCARECOPromptCalibProdEcalPedestals)
pathALCARECOPromptCalibProdLumiPCC = cms.Path(seqALCARECOPromptCalibProdLumiPCC)
pathALCARECOSiStripPCLHistos = cms.Path(seqALCARECOSiStripPCLHistos)
pathHotlineSkimSingleMuon = cms.Path(seqHotlineSkimSingleMuon)
pathHotlineSkimDoubleMuon = cms.Path(seqHotlineSkimDoubleMuon)
pathHotlineSkimTripleMuon = cms.Path(seqHotlineSkimTripleMuon)
pathHotlineSkimSingleElectron = cms.Path(seqHotlineSkimSingleElectron)
pathHotlineSkimDoubleElectron = cms.Path(seqHotlineSkimDoubleElectron)
pathHotlineSkimTripleElectron = cms.Path(seqHotlineSkimTripleElectron)
pathHotlineSkimSinglePhoton = cms.Path(seqHotlineSkimSinglePhoton)
pathHotlineSkimDoublePhoton = cms.Path(seqHotlineSkimDoublePhoton)
pathHotlineSkimTriplePhoton = cms.Path(seqHotlineSkimTriplePhoton)
pathHotlineSkimSingleJet = cms.Path(seqHotlineSkimSingleJet)
pathHotlineSkimDoubleJet = cms.Path(seqHotlineSkimDoubleJet)
pathHotlineSkimMultiJet = cms.Path(seqHotlineSkimMultiJet)
pathHotlineSkimHT = cms.Path(seqHotlineSkimHT)
pathHotlineSkimMassiveDimuon = cms.Path(seqHotlineSkimMassiveDimuon)
pathHotlineSkimMassiveDielectron = cms.Path(seqHotlineSkimMassiveDielectron)
pathHotlineSkimMassiveEMu = cms.Path(seqHotlineSkimMassiveEMu)
pathHotlineSkimPFMET = cms.Path(seqHotlineSkimPFMET)
pathHotlineSkimCaloMET = cms.Path(seqHotlineSkimCaloMET)
pathHotlineSkimCondMET = cms.Path(seqHotlineSkimCondMET)

# AlCaReco event content definitions:

from Configuration.EventContent.AlCaRecoOutput_cff import *

# AlCaReco stream definitions:

ALCARECOStreamTkAlMinBias = cms.FilteredStream(
	responsible = 'Andreas Mussgiller',
	name = 'TkAlMinBias',
	paths  = (pathALCARECOTkAlMinBias),
	content = OutALCARECOTkAlMinBias.outputCommands,
	selectEvents = OutALCARECOTkAlMinBias.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamTkAlMuonIsolated = cms.FilteredStream(
	responsible = 'Andreas Mussgiller',
	name = 'TkAlMuonIsolated',
	paths  = (pathALCARECOTkAlMuonIsolated),
	content = OutALCARECOTkAlMuonIsolated.outputCommands,
	selectEvents = OutALCARECOTkAlMuonIsolated.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamTkAlMuonIsolatedPA = cms.FilteredStream(
	responsible = 'James Castle',
	name = 'TkAlMuonIsolatedPA',
	paths  = (pathALCARECOTkAlMuonIsolatedPA),
	content = OutALCARECOTkAlMuonIsolatedPA.outputCommands,
	selectEvents = OutALCARECOTkAlMuonIsolatedPA.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamTkAlZMuMu = cms.FilteredStream(
	responsible = 'Andreas Mussgiller',
	name = 'TkAlZMuMu',
	paths  = (pathALCARECOTkAlZMuMu),
	content = OutALCARECOTkAlZMuMu.outputCommands,
	selectEvents = OutALCARECOTkAlZMuMu.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamTkAlZMuMuPA = cms.FilteredStream(
        responsible = 'James Castle',
        name = 'TkAlZMuMuPA',
        paths  = (pathALCARECOTkAlZMuMuPA),
        content = OutALCARECOTkAlZMuMuPA.outputCommands,
        selectEvents = OutALCARECOTkAlZMuMuPA.SelectEvents,
        dataTier = cms.untracked.string('ALCARECO')
        )

ALCARECOStreamTkAlJpsiMuMu = cms.FilteredStream(
	responsible = 'Andreas Mussgiller',
	name = 'TkAlJpsiMuMu',
	paths  = (pathALCARECOTkAlJpsiMuMu),
	content = OutALCARECOTkAlJpsiMuMu.outputCommands,
	selectEvents = OutALCARECOTkAlJpsiMuMu.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamTkAlUpsilonMuMu = cms.FilteredStream(
	responsible = 'Andreas Mussgiller',
	name = 'TkAlUpsilonMuMu',
	paths  = (pathALCARECOTkAlUpsilonMuMu),
	content = OutALCARECOTkAlUpsilonMuMu.outputCommands,
	selectEvents = OutALCARECOTkAlUpsilonMuMu.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamTkAlUpsilonMuMuPA = cms.FilteredStream(
        responsible = 'James Castle',
        name = 'TkAlUpsilonMuMuPA',
        paths  = (pathALCARECOTkAlUpsilonMuMuPA),
        content = OutALCARECOTkAlUpsilonMuMuPA.outputCommands,
        selectEvents = OutALCARECOTkAlUpsilonMuMuPA.SelectEvents,
        dataTier = cms.untracked.string('ALCARECO')
        )

ALCARECOStreamSiPixelCalSingleMuon = cms.FilteredStream(
	responsible = 'Tamas Almos Vami',
	name = 'SiPixelCalSingleMuon',
	paths  = (pathALCARECOSiPixelCalSingleMuon),
	content = OutALCARECOSiPixelCalSingleMuon.outputCommands,
	selectEvents = OutALCARECOSiPixelCalSingleMuon.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamSiPixelCalCosmics = cms.FilteredStream(
	responsible = 'Tamas Almos Vami',
	name = 'SiPixelCalCosmics',
	paths  = (pathALCARECOSiPixelCalCosmics),
	content = OutALCARECOSiPixelCalCosmics.outputCommands,
	selectEvents = OutALCARECOSiPixelCalCosmics.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamSiStripCalMinBias = cms.FilteredStream(
	responsible = 'Vitaliano Ciulli',
	name = 'SiStripCalMinBias',
	paths  = (pathALCARECOSiStripCalMinBias),
	content = OutALCARECOSiStripCalMinBias.outputCommands,
	selectEvents = OutALCARECOSiStripCalMinBias.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamSiStripCalSmallBiasScan = cms.FilteredStream(
	responsible = 'Marco Musich',
	name = 'SiStripCalSmallBiasScan',
	paths  = (pathALCARECOSiStripCalSmallBiasScan),
	content = OutALCARECOSiStripCalSmallBiasScan.outputCommands,
	selectEvents = OutALCARECOSiStripCalSmallBiasScan.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamSiStripCalMinBiasAAG = cms.FilteredStream(
        responsible = 'Alessandro Di Mattia',
        name = 'SiStripCalMinBiasAAG',
        paths  = (pathALCARECOSiStripCalMinBiasAAG),
        content = OutALCARECOSiStripCalMinBiasAAG.outputCommands,
        selectEvents = OutALCARECOSiStripCalMinBiasAAG.SelectEvents,
        dataTier = cms.untracked.string('ALCARECO')
        )

ALCARECOStreamSiStripCalCosmics = cms.FilteredStream(
	responsible = 'Marco Musich',
	name = 'SiStripCalCosmics',
	paths  = (pathALCARECOSiStripCalCosmics),
	content = OutALCARECOSiStripCalCosmics.outputCommands,
	selectEvents = OutALCARECOSiStripCalCosmics.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamSiStripCalZeroBias = cms.FilteredStream(
	responsible = 'Gordon Kaussen',
	name = 'SiStripCalZeroBias',
	paths  = (pathALCARECOSiStripCalZeroBias),
	content = OutALCARECOSiStripCalZeroBias.outputCommands,
	selectEvents = OutALCARECOSiStripCalZeroBias.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamSiPixelCalZeroBias = cms.FilteredStream(
        responsible = 'Tongguang Cheng',
        name = 'SiPixelCalZeroBias',
        paths  = (pathALCARECOSiPixelCalZeroBias),
        content = OutALCARECOSiPixelCalZeroBias.outputCommands,
        selectEvents = OutALCARECOSiPixelCalZeroBias.SelectEvents,
        dataTier = cms.untracked.string('ALCARECO')
        )

ALCARECOStreamLumiPixelsMinBias = cms.FilteredStream(
	responsible = 'Chris Palmer',
	name = 'LumiPixelsMinBias',
	paths  = (pathALCARECOLumiPixelsMinBias),
	content = OutALCARECOLumiPixelsMinBias.outputCommands,
	selectEvents = OutALCARECOLumiPixelsMinBias.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamAlCaPCCZeroBiasFromRECO = cms.FilteredStream(
	responsible = 'Chris Palmer',
	name = 'AlCaPCCZeroBiasFromRECO',
	paths  = (pathALCARECOAlCaPCCZeroBiasFromRECO),
	content = OutALCARECOAlCaPCCZeroBiasFromRECO.outputCommands,
	selectEvents = OutALCARECOAlCaPCCZeroBiasFromRECO.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamAlCaPCCRandomFromRECO = cms.FilteredStream(
	responsible = 'Chris Palmer',
	name = 'AlCaPCCRandomFromRECO',
	paths  = (pathALCARECOAlCaPCCRandomFromRECO),
	content = OutALCARECOAlCaPCCRandomFromRECO.outputCommands,
	selectEvents = OutALCARECOAlCaPCCRandomFromRECO.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamEcalCalZElectron = cms.FilteredStream(
	responsible = 'Shervin Nourbakhsh',
	name = 'EcalCalZElectron',
	paths  = (pathALCARECOEcalCalZElectron, pathALCARECOEcalCalZSCElectron),
	content = OutALCARECOEcalCalElectron.outputCommands,
	selectEvents =  cms.untracked.PSet(
          SelectEvents = cms.vstring('pathALCARECOEcalCalZElectron', 'pathALCARECOEcalCalZSCElectron')
          ),
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamEcalCalWElectron = cms.FilteredStream(
	responsible = 'Shervin Nourbakhsh',
	name = 'EcalCalWElectron',
	paths  = (pathALCARECOEcalCalWElectron),
	content = OutALCARECOEcalCalElectron.outputCommands,
	selectEvents =  cms.untracked.PSet(
          SelectEvents = cms.vstring('pathALCARECOEcalCalWElectron')
          ),
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamEcalUncalZElectron = cms.FilteredStream(
	responsible = 'Shervin Nourbakhsh',
	name = 'EcalUncalZElectron',
	paths  = (pathALCARECOEcalUncalZElectron, pathALCARECOEcalUncalZSCElectron),
	content = OutALCARECOEcalUncalElectron.outputCommands,
	selectEvents =  cms.untracked.PSet(
          SelectEvents = cms.vstring('pathALCARECOEcalUncalZElectron', 'pathALCARECOEcalUncalZSCElectron')
          ),
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamEcalUncalWElectron = cms.FilteredStream(
	responsible = 'Shervin Nourbakhsh',
	name = 'EcalUncalWElectron',
	paths  = (pathALCARECOEcalUncalWElectron),
	content = OutALCARECOEcalUncalElectron.outputCommands,
	selectEvents =  cms.untracked.PSet(
          SelectEvents = cms.vstring('pathALCARECOEcalUncalWElectron')
          ),
	dataTier = cms.untracked.string('ALCARECO')
	)

# ALCARECOStreamEcalRecalElectron = cms.FilteredStream(
# 	responsible = 'Shervin Nourbakhsh',
# 	name = 'EcalRecalElectron',
# 	paths  = (pathALCARECOEcalRecalElectron),
# 	content = OutALCARECOEcalRecalElectron.outputCommands,
# 	selectEvents = cms.PSet(),
# 	dataTier = cms.untracked.string('ALCARECO')
# 	)

ALCARECOStreamEcalESAlign    = cms.FilteredStream(
    responsible = 'Shervin Nourbakhsh',
    name = 'EcalESAlign',
    paths = (pathALCARECOEcalESAlign),
    content = OutALCARECOEcalESAlign.outputCommands,
    selectEvents = OutALCARECOEcalESAlign.SelectEvents,
    dataTier = cms.untracked.string('ALCARECO')
)

ALCARECOStreamEcalTrg = cms.FilteredStream(
    responsible = 'Shervin Nourbakhsh',
    name = 'EcalTrg',
    paths = pathALCARECOEcalTrg,
    content=  OutALCARECOEcalTrg.outputCommands,
    selectEvents = OutALCARECOEcalTrg.SelectEvents,
    dataTier = cms.untracked.string('ALCARECO')
)

ALCARECOStreamEcalTestPulsesRaw = cms.FilteredStream(
    responsible = 'Stefano Argiro',
    name = 'EcalTestPulsesRaw',
    paths = pathALCARECOEcalTestPulsesRaw,
    content=  OutALCARECOEcalTestPulsesRaw.outputCommands,
    selectEvents = OutALCARECOEcalTestPulsesRaw.SelectEvents,
    dataTier = cms.untracked.string('ALCARECO')
)

ALCARECOStreamHcalCalDijets = cms.FilteredStream(
	responsible = 'Grigory Safronov',
	name = 'HcalCalDijets',
	paths  = (pathALCARECOHcalCalDijets),
	content = OutALCARECOHcalCalDijets.outputCommands,
	selectEvents = OutALCARECOHcalCalDijets.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamHcalCalGammaJet = cms.FilteredStream(
	responsible = 'Grigory Safronov',
	name = 'HcalCalGammaJet',
	paths  = (pathALCARECOHcalCalGammaJet),
	content = OutALCARECOHcalCalGammaJet.outputCommands,
	selectEvents = OutALCARECOHcalCalGammaJet.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamHcalCalHO = cms.FilteredStream(
	responsible = 'Gobinda Majumder',
	name = 'HcalCalHO',
	paths  = (pathALCARECOHcalCalHO),
	content = OutALCARECOHcalCalHO.outputCommands,
	selectEvents = OutALCARECOHcalCalHO.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamHcalCalHOCosmics = cms.FilteredStream(
	responsible = 'Gobinda Majumder',
	name = 'HcalCalHOCosmics',
	paths  = (pathALCARECOHcalCalHOCosmics),
	content = OutALCARECOHcalCalHOCosmics.outputCommands,
	selectEvents = OutALCARECOHcalCalHOCosmics.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamHcalCalIsoTrk = cms.FilteredStream(
	responsible = 'Sunanda Banerjee',
	name = 'HcalCalIsoTrk',
	paths  = (pathALCARECOHcalCalIsoTrk),
	content = OutALCARECOHcalCalIsoTrk.outputCommands,
	selectEvents = OutALCARECOHcalCalIsoTrk.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamHcalCalIsoTrkFilter = cms.FilteredStream(
	responsible = 'Sunanda Banerjee',
	name = 'HcalCalIsoTrkFilter',
	paths  = (pathALCARECOHcalCalIsoTrkFilter),
	content = OutALCARECOHcalCalIsoTrkFilter.outputCommands,
	selectEvents = OutALCARECOHcalCalIsoTrkFilter.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamHcalCalNoise = cms.FilteredStream(
	responsible = 'Grigory Safronov',
	name = 'HcalCalNoise',
	paths  = (pathALCARECOHcalCalNoise),
	content = OutALCARECOHcalCalNoise.outputCommands,
	selectEvents = OutALCARECOHcalCalNoise.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamHcalCalIterativePhiSym = cms.FilteredStream(
    responsible = 'Natalia Lychkovskaya',
    name = 'HcalCalIterativePhiSym',
    paths  = (pathALCARECOHcalCalIterativePhiSym),
    content = OutALCARECOHcalCalIterativePhiSym.outputCommands,
    selectEvents = OutALCARECOHcalCalIterativePhiSym.SelectEvents,
    dataTier = cms.untracked.string('ALCARECO')
    )

ALCARECOStreamHcalCalIsolatedBunchFilter = cms.FilteredStream(
	responsible = 'Sunanda Banerjee',
	name = 'HcalCalIsolatedBunchFilter',
	paths  = (pathALCARECOHcalCalIsolatedBunchFilter),
	content = OutALCARECOHcalCalIsolatedBunchFilter.outputCommands,
	selectEvents = OutALCARECOHcalCalIsolatedBunchFilter.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamHcalCalIsolatedBunchSelector = cms.FilteredStream(
	responsible = 'Sunanda Banerjee',
	name = 'HcalCalIsolatedBunchSelector',
	paths  = (pathALCARECOHcalCalIsolatedBunchSelector),
	content = OutALCARECOHcalCalIsolatedBunchSelector.outputCommands,
	selectEvents = OutALCARECOHcalCalIsolatedBunchSelector.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamHcalCalHBHEMuonFilter = cms.FilteredStream(
	responsible = 'Sunanda Banerjee',
	name = 'HcalCalHBHEMuonFilter',
	paths  = (pathALCARECOHcalCalHBHEMuonFilter),
	content = OutALCARECOHcalCalHBHEMuonFilter.outputCommands,
	selectEvents = OutALCARECOHcalCalHBHEMuonFilter.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamHcalCalLowPUHBHEMuonFilter = cms.FilteredStream(
	responsible = 'Nan Lu',
	name = 'HcalCalLowPUHBHEMuonFilter',
	paths  = (pathALCARECOHcalCalLowPUHBHEMuonFilter),
	content = OutALCARECOHcalCalLowPUHBHEMuonFilter.outputCommands,
	selectEvents = OutALCARECOHcalCalLowPUHBHEMuonFilter.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamHcalCalHEMuonFilter = cms.FilteredStream(
	responsible = 'Nan Lu',
	name = 'HcalCalHEMuonFilter',
	paths  = (pathALCARECOHcalCalHEMuonFilter),
	content = OutALCARECOHcalCalHEMuonFilter.outputCommands,
	selectEvents = OutALCARECOHcalCalHEMuonFilter.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamMuAlCalIsolatedMu = cms.FilteredStream(
	responsible = 'Luca Pernie',
	name = 'MuAlCalIsolatedMu',
	paths  = (pathALCARECOMuAlCalIsolatedMu,pathALCARECOMuAlCalIsolatedMuGeneralTracks),
	content = OutALCARECOMuAlCalIsolatedMu.outputCommands,
	selectEvents = OutALCARECOMuAlCalIsolatedMu.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamMuAlZMuMu = cms.FilteredStream(
	responsible = 'Luca Pernie',
	name = 'MuAlZMuMu',
	paths  = (pathALCARECOMuAlZMuMu,pathALCARECOMuAlZMuMuGeneralTracks),
	content = OutALCARECOMuAlZMuMu.outputCommands,
	selectEvents = OutALCARECOMuAlZMuMu.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamMuAlOverlaps = cms.FilteredStream(
	responsible = 'Luca Pernie',
	name = 'MuAlOverlaps',
	paths  = (pathALCARECOMuAlOverlaps,pathALCARECOMuAlOverlapsGeneralTracks),
	content = OutALCARECOMuAlOverlaps.outputCommands,
	selectEvents = OutALCARECOMuAlOverlaps.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamRpcCalHLT = cms.FilteredStream(
	responsible = 'Marcello Maggi',
	name = 'RpcCalHLT',
	paths  = (pathALCARECORpcCalHLT),
	content = OutALCARECORpcCalHLT.outputCommands,
	selectEvents = OutALCARECORpcCalHLT.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamDtCalib = cms.FilteredStream(
	responsible = 'Mario Pelliccioni',
	name = 'DtCalib',
	paths  = (pathALCARECODtCalib),
	content = OutALCARECODtCalib.outputCommands,
	selectEvents = OutALCARECODtCalib.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamDtCalibCosmics = cms.FilteredStream(
	responsible = 'Antonio Vilela Pereira',
	name = 'DtCalibCosmics',
	paths  = (pathALCARECODtCalibCosmics),
	content = OutALCARECODtCalibCosmics.outputCommands,
	selectEvents = OutALCARECODtCalibCosmics.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamTkAlCosmicsInCollisions = cms.FilteredStream(
	responsible = 'Andreas Mussgiller',
	name = 'TkAlCosmicsInCollisions',
	paths  = (pathALCARECOTkAlCosmicsInCollisions),
	content = OutALCARECOTkAlCosmicsInCollisions.outputCommands,
	selectEvents = OutALCARECOTkAlCosmicsInCollisions.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamTkAlCosmics = cms.FilteredStream(
	responsible = 'Andreas Mussgiller',
	name = 'TkAlCosmics',
	paths  = (pathALCARECOTkAlCosmicsCTF,pathALCARECOTkAlCosmicsCosmicTF,pathALCARECOTkAlCosmicsRegional),
	content = OutALCARECOTkAlCosmics.outputCommands,
	selectEvents = OutALCARECOTkAlCosmics.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamTkAlCosmicsHLT = cms.FilteredStream(
	responsible = 'Andreas Mussgiller',
	name = 'TkAlCosmicsHLT',
	paths  = (pathALCARECOTkAlCosmicsCTFHLT,pathALCARECOTkAlCosmicsCosmicTFHLT,pathALCARECOTkAlCosmicsRegionalHLT),
	content = OutALCARECOTkAlCosmicsHLT.outputCommands,
	selectEvents = OutALCARECOTkAlCosmicsHLT.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamTkAlCosmics0T = cms.FilteredStream(
	responsible = 'Andreas Mussgiller',
	name = 'TkAlCosmics0T',
	paths  = (pathALCARECOTkAlCosmicsCTF0T,pathALCARECOTkAlCosmicsCosmicTF0T,pathALCARECOTkAlCosmicsRegional0T),
	content = OutALCARECOTkAlCosmics0T.outputCommands,
	selectEvents = OutALCARECOTkAlCosmics0T.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamTkAlCosmics0THLT = cms.FilteredStream(
	responsible = 'Andreas Mussgiller',
	name = 'TkAlCosmics0THLT',
	paths  = (pathALCARECOTkAlCosmicsCTF0THLT,pathALCARECOTkAlCosmicsCosmicTF0THLT,pathALCARECOTkAlCosmicsRegional0THLT),
	content = OutALCARECOTkAlCosmics0THLT.outputCommands,
	selectEvents = OutALCARECOTkAlCosmics0THLT.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamMuAlGlobalCosmics = cms.FilteredStream(
	responsible = 'Luca Pernie',
	name = 'MuAlGlobalCosmics',
	paths  = (pathALCARECOMuAlGlobalCosmics),
	content = OutALCARECOMuAlGlobalCosmics.outputCommands,
	selectEvents = OutALCARECOMuAlGlobalCosmics.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamMuAlGlobalCosmicsInCollisions = cms.FilteredStream(
	responsible = 'Luca Pernie',
	name = 'MuAlGlobalCosmicsInCollisions',
	paths  = (pathALCARECOMuAlGlobalCosmicsInCollisions),
	content = OutALCARECOMuAlGlobalCosmicsInCollisions.outputCommands,
	selectEvents = OutALCARECOMuAlGlobalCosmicsInCollisions.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamTkAlBeamHalo = cms.FilteredStream(
	responsible = 'Andreas Mussgiller',
	name = 'TkAlBeamHalo',
	paths  = (pathALCARECOTkAlBeamHalo),
	content = OutALCARECOTkAlBeamHalo.outputCommands,
	selectEvents = OutALCARECOTkAlBeamHalo.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamMuAlBeamHalo = cms.FilteredStream(
	responsible = 'Luca Pernie',
	name = 'MuAlBeamHalo',
	paths  = (pathALCARECOMuAlBeamHalo),
	content = OutALCARECOMuAlBeamHalo.outputCommands,
	selectEvents = OutALCARECOMuAlBeamHalo.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamMuAlBeamHaloOverlaps = cms.FilteredStream(
	responsible = 'Luca Pernie',
	name = 'MuAlBeamHaloOverlaps',
	paths  = (pathALCARECOMuAlBeamHaloOverlaps),
	content = OutALCARECOMuAlBeamHaloOverlaps.outputCommands,
	selectEvents = OutALCARECOMuAlBeamHaloOverlaps.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamTkAlLAS = cms.FilteredStream(
	responsible = 'Jan Olzem',
	name = 'TkAlLAS',
	paths  = (pathALCARECOTkAlLAS),
	content = OutALCARECOTkAlLAS.outputCommands,
	selectEvents = OutALCARECOTkAlLAS.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)


ALCARECOStreamPromptCalibProd = cms.FilteredStream(
	responsible = 'Gianluca Cerminara',
	name = 'PromptCalibProd',
	paths  = (pathALCARECOPromptCalibProd),
	content = OutALCARECOPromptCalibProd.outputCommands,
	selectEvents = OutALCARECOPromptCalibProd.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamPromptCalibProdBeamSpotHP = cms.FilteredStream(
	responsible = 'Gianluca Cerminara',
	name = 'PromptCalibProdBeamSpotHP',
	paths  = (pathALCARECOPromptCalibProdBeamSpotHP),
	content = OutALCARECOPromptCalibProdBeamSpotHP.outputCommands,
	selectEvents = OutALCARECOPromptCalibProdBeamSpotHP.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamPromptCalibProdBeamSpotHPLowPU = cms.FilteredStream(
	responsible = 'Gianluca Cerminara',
	name = 'PromptCalibProdBeamSpotHPLowPU',
	paths  = (pathALCARECOPromptCalibProdBeamSpotHPLowPU),
	content = OutALCARECOPromptCalibProdBeamSpotHPLowPU.outputCommands,
	selectEvents = OutALCARECOPromptCalibProdBeamSpotHPLowPU.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamPromptCalibProdSiStrip = cms.FilteredStream(
	responsible = 'Gianluca Cerminara',
	name = 'PromptCalibProdSiStrip',
	paths  = (pathALCARECOPromptCalibProdSiStrip),
	content = OutALCARECOPromptCalibProdSiStrip.outputCommands,
	selectEvents = OutALCARECOPromptCalibProdSiStrip.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamPromptCalibProdSiPixel = cms.FilteredStream(
        responsible = 'Tongguang Cheng',
        name = 'PromptCalibProdSiPixel',
        paths  = (pathALCARECOPromptCalibProdSiPixel),
        content = OutALCARECOPromptCalibProdSiPixel.outputCommands,
        selectEvents = OutALCARECOPromptCalibProdSiPixel.SelectEvents,
        dataTier = cms.untracked.string('ALCARECO')
        )


ALCARECOStreamPromptCalibProdSiStripGains = cms.FilteredStream(
	responsible = 'Gianluca Cerminara',
	name = 'PromptCalibProdSiStripGains',
        paths  = (pathALCARECOPromptCalibProdSiStripGains),
	content = OutALCARECOPromptCalibProdSiStripGains.outputCommands,
	selectEvents = OutALCARECOPromptCalibProdSiStripGains.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamPromptCalibProdSiStripGainsAAG = cms.FilteredStream(
        responsible = 'Alessandro Di Mattia',
        name = 'PromptCalibProdSiStripGainsAAG',
        paths  = (pathALCARECOPromptCalibProdSiStripGainsAAG),
        content = OutALCARECOPromptCalibProdSiStripGainsAAG.outputCommands,
        selectEvents = OutALCARECOPromptCalibProdSiStripGainsAAG.SelectEvents,
        dataTier = cms.untracked.string('ALCARECO')
        )



ALCARECOStreamPromptCalibProdSiPixelAli = cms.FilteredStream(
	responsible = 'Gianluca Cerminara',
	name = 'PromptCalibProdSiPixelAli',
	paths  = (pathALCARECOPromptCalibProdSiPixelAli),
	content = OutALCARECOPromptCalibProdSiPixelAli.outputCommands,
	selectEvents = OutALCARECOPromptCalibProdSiPixelAli.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamSiStripPCLHistos = cms.FilteredStream(
	responsible = 'Gianluca Cerminara',
	name = 'SiStripPCLHistos',
	paths  = (pathALCARECOSiStripPCLHistos),
	content = OutALCARECOSiStripPCLHistos.outputCommands,
	selectEvents = OutALCARECOSiStripPCLHistos.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)

ALCARECOStreamPromptCalibProdEcalPedestals = cms.FilteredStream(
	responsible = 'Stefano Argiro',
	name = 'PromptCalibProdEcalPedestals',
	paths  = (pathALCARECOPromptCalibProdEcalPedestals),
	content = OutALCARECOPromptCalibProdEcalPedestals.outputCommands,
	selectEvents = OutALCARECOPromptCalibProdEcalPedestals.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)


ALCARECOStreamPromptCalibProdLumiPCC = cms.FilteredStream(
	responsible = 'Chris Palmer',
	name = 'PromptCalibProdLumiPCC',
	paths  = (pathALCARECOPromptCalibProdLumiPCC),
	content = OutALCARECOPromptCalibProdLumiPCC.outputCommands,
	selectEvents = OutALCARECOPromptCalibProdLumiPCC.SelectEvents,
	dataTier = cms.untracked.string('ALCARECO')
	)


ALCARECOStreamHotline = cms.FilteredStream(
        responsible = 'Dustin Anderson',
        name = 'Hotline',
        paths = (
            pathHotlineSkimSingleMuon,
            pathHotlineSkimDoubleMuon,
            pathHotlineSkimTripleMuon,
            pathHotlineSkimSingleElectron,
            pathHotlineSkimDoubleElectron,
            pathHotlineSkimTripleElectron,
            pathHotlineSkimSinglePhoton,
            pathHotlineSkimDoublePhoton,
            pathHotlineSkimTriplePhoton,
            pathHotlineSkimSingleJet,
            pathHotlineSkimDoubleJet,
            pathHotlineSkimMultiJet,
            pathHotlineSkimHT,
            pathHotlineSkimMassiveDimuon,
            pathHotlineSkimMassiveDielectron,
            pathHotlineSkimMassiveEMu,
            pathHotlineSkimPFMET,
            pathHotlineSkimCaloMET,
            pathHotlineSkimCondMET
            ),
        content = OutALCARECOHotline.outputCommands,
        selectEvents = OutALCARECOHotline.SelectEvents,
        dataTier = cms.untracked.string('ALCARECO')
        )

from Configuration.StandardSequences.AlCaRecoStream_Specials_cff import *

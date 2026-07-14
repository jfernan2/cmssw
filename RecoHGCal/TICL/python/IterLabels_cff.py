import FWCore.ParameterSet.Config as cms

ticlIterLabelsPSet = cms.PSet(
    labels=cms.vstring(
        "ticlTrackstersCLUE3DHigh",
        "ticlTracksterLinks",
        "ticlCandidate",
        "ticlTracksterLinksSuperclusteringDNN"
    )
)


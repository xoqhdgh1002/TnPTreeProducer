import FWCore.ParameterSet.Config as cms

# Some miniAOD testfiles, about 1000 events copied to our eos storage
# (not running directly on datasets because they get moved around all the time and xrootd sucks)
filesMiniAOD_2018 = {
    'mc' :   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIIAutumn18MiniAOD-DYJetsToLL_M-50.root'),
    'data' : cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/Egamma-Run2018A-17Sep2018-v2.root'),
}

filesMiniAOD_2017 = {
    'mc' :   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIIFall17MiniAODv2-DYJetsToLL_M-50.root'),
    'data' : cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2017B-31Mar2018-v1.root'),
}

filesMiniAOD_2016 = {
    'mc' :   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIISummer16MiniAODv3-DYJetsToLL_M-50.root'),
    'data' : cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2016B-17Jul2018_ver2-v1.root'),
}


# Some miniAOD UL testfiles, which are available now and hopefully don't get deleted too soon
filesMiniAOD_UL2016preVFP = {
    #'mc':   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIISummer19UL16MiniAODAPV-DYJetsToLL_M-50.root'), # this file no longer seems to work
    'mc':   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIISummer20UL16MiniAODv2-DY1JetsToLL_M-50-106X_mcRun2_asymptotic_v17-v1.root'),
    'data': cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2016E-21Feb2020_UL2016_HIPM.root'),
}

filesMiniAOD_UL2016postVFP = {
    'mc':   cms.untracked.vstring(''),
    'data': cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2016F-21Feb2020_UL2016-postVFP.root'),
}

filesMiniAOD_UL2016miniAODv2 = {
    # test samples specifically for lowpt electron tnp production
    # later switch to Jpsi, might be better for lowpt electrons
    #'mc' :  cms.untracked.vstring('/store/mc/RunIISummer20UL16MiniAODv2/DY1JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/00061BF0-5BB0-524E-A539-0CAAD8579386.root'),

    'mc':   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIISummer20UL16MiniAODv2-DY1JetsToLL_M-50-106X_mcRun2_asymptotic_v17-v1.root'),
    'data': cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-UL2016_MiniAODv2-v2-Run2016H-02A3E4FE-B0AA-F546-981D-283EB73FBAC9.root'),

    #'mc' :  cms.untracked.vstring('/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/C2390145-5FF1-5E45-97B0-925095E9BAD9.root'),  
    #'data' : cms.untracked.vstring('/store/data/Run2016H/SingleElectron/MINIAOD/UL2016_MiniAODv2-v2/120000/02A3E4FE-B0AA-F546-981D-283EB73FBAC9.root'),
}



filesMiniAOD_UL2018 = {
    'mc' :   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIISummer19UL18MiniAOD-DYJetsToEE_M-50.root'),
    'data' : cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/Egamma-Run2018D-12Nov2019_UL2018.root'),
}

filesMiniAOD_UL2017 = {
    'mc' :   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIISummer19UL17MiniAOD-DYJetsToLL_M-50.root'),
    'data' : cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2017F-09Aug2019_UL2017.root'),
}


# AOD UL testfiles
filesAOD_UL2016preVFP = {
    'mc':   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIISummer19UL16RECOAPV-DYJetsToLL_M-50.root'),
    'data': cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2016E-21Feb2020_UL2016_HIPM-AOD.root'),
}

filesAOD_UL2016postVFP = {
    'mc':   cms.untracked.vstring(''),
    'data': cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2016F-21Feb2020_UL2016-postVFP-AOD.root'),
}

filesAOD_UL2018 = {
    'mc' :   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIISummer19UL18RECO-DYToEE_M-50.root'),
    'data' : cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/Egamma-Run2018D-12Nov2019_UL2018-AOD.root'),
}

filesAOD_UL2017 = {
    'mc' :   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIISummer19UL17RECO-DYToEE_M-50.root'),
    'data' : cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2017F-09Aug2019_UL2017-AOD.root'),
}

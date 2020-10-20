all_tau_ids = [
    ('byCombinedIsolationDeltaBetaCorrRaw3Hits', float),
    ('byLooseCombinedIsolationDeltaBetaCorr3Hits', int),
    ('byMediumCombinedIsolationDeltaBetaCorr3Hits', int),
    ('byTightCombinedIsolationDeltaBetaCorr3Hits', int),

    ('byIsolationMVArun2v1DBoldDMwLTraw', float),
    ('byVVLooseIsolationMVArun2v1DBoldDMwLT', int),
    ('byVLooseIsolationMVArun2v1DBoldDMwLT', int),
    ('byLooseIsolationMVArun2v1DBoldDMwLT', int),
    ('byMediumIsolationMVArun2v1DBoldDMwLT', int),
    ('byTightIsolationMVArun2v1DBoldDMwLT', int),
    ('byVTightIsolationMVArun2v1DBoldDMwLT', int),
    ('byVVTightIsolationMVArun2v1DBoldDMwLT', int),

    #('byIsolationMVArun2v1PWoldDMwLTraw', float), # Gone? Not in 11_0_0_pre13
    #('byVLooseIsolationMVArun2v1PWoldDMwLT', int),
    #('byLooseIsolationMVArun2v1PWoldDMwLT', int),
    #('byMediumIsolationMVArun2v1PWoldDMwLT', int),
    #('byTightIsolationMVArun2v1PWoldDMwLT', int),
    #('byVTightIsolationMVArun2v1PWoldDMwLT', int),
    #('byVVTightIsolationMVArun2v1PWoldDMwLT', int),

    ('byIsolationMVArun2v1DBnewDMwLTraw', float),
    ('byVVLooseIsolationMVArun2v1DBnewDMwLT', int),
    ('byVLooseIsolationMVArun2v1DBnewDMwLT', int),
    ('byLooseIsolationMVArun2v1DBnewDMwLT', int),
    ('byMediumIsolationMVArun2v1DBnewDMwLT', int),
    ('byTightIsolationMVArun2v1DBnewDMwLT', int),
    ('byVTightIsolationMVArun2v1DBnewDMwLT', int),
    ('byVVTightIsolationMVArun2v1DBnewDMwLT', int),

    ('byIsolationMVArun2v1DBdR03oldDMwLTraw', float),
    ('byVVLooseIsolationMVArun2v1DBdR03oldDMwLT', int),
    ('byVLooseIsolationMVArun2v1DBdR03oldDMwLT', int),
    ('byLooseIsolationMVArun2v1DBdR03oldDMwLT', int),
    ('byMediumIsolationMVArun2v1DBdR03oldDMwLT', int),
    ('byTightIsolationMVArun2v1DBdR03oldDMwLT', int),
    ('byVTightIsolationMVArun2v1DBdR03oldDMwLT', int),
    ('byVVTightIsolationMVArun2v1DBdR03oldDMwLT', int),

    ('chargedIsoPtSum', float),
    ('neutralIsoPtSum', float),
    ('puCorrPtSum', float),
    ('neutralIsoPtSumWeight', float),
    ('footprintCorrection', float),
    ('photonPtSumOutsideSignalCone', float),
    ('decayModeFinding', int),
    ('decayModeFindingNewDMs', int),
]

ids_available = [
    ('againstElectronDeadECAL', float),

    ('decayModeFinding', float),
    ('decayModeFindingNewDMs', float),

    ('byCombinedIsolationDeltaBetaCorrRaw3Hits', float),
    ('byLooseCombinedIsolationDeltaBetaCorr3Hits', float),
    ('byMediumCombinedIsolationDeltaBetaCorr3Hits', float),
    ('byTightCombinedIsolationDeltaBetaCorr3Hits', float),

    ('byPhotonPtSumOutsideSignalCone', float),

    ('chargedIsoPtSum', float),
    ('footprintCorrection', float),
    ('neutralIsoPtSum', float),
    ('neutralIsoPtSumWeight', float),
    ('photonPtSumOutsideSignalCone', float),
    ('puCorrPtSum', float),

    ('chargedIsoPtSumdR03', float),
    ('footprintCorrectiondR03', float),
    ('neutralIsoPtSumWeightdR03', float),
    ('neutralIsoPtSumdR03', float),
    ('photonPtSumOutsideSignalConedR03', float),

    ('byIsolationMVArun2v1DBdR03oldDMwLTraw', float),
    ('byVVLooseIsolationMVArun2v1DBdR03oldDMwLT', float),
    ('byVLooseIsolationMVArun2v1DBdR03oldDMwLT', float),
    ('byLooseIsolationMVArun2v1DBdR03oldDMwLT', float),
    ('byMediumIsolationMVArun2v1DBdR03oldDMwLT', float),
    ('byTightIsolationMVArun2v1DBdR03oldDMwLT', float),
    ('byVTightIsolationMVArun2v1DBdR03oldDMwLT', float),
    ('byVVTightIsolationMVArun2v1DBdR03oldDMwLT', float),

    ('byIsolationMVArun2v1DBnewDMwLTraw', float),
    ('byVVLooseIsolationMVArun2v1DBnewDMwLT', float),
    ('byVLooseIsolationMVArun2v1DBnewDMwLT', float),
    ('byLooseIsolationMVArun2v1DBnewDMwLT', float),
    ('byMediumIsolationMVArun2v1DBnewDMwLT', float),
    ('byTightIsolationMVArun2v1DBnewDMwLT', float),
    ('byVTightIsolationMVArun2v1DBnewDMwLT', float),
    ('byVVTightIsolationMVArun2v1DBnewDMwLT', float),

    ('byIsolationMVArun2v1DBoldDMwLTraw', float),
    ('byVVLooseIsolationMVArun2v1DBoldDMwLT', float),
    ('byVLooseIsolationMVArun2v1DBoldDMwLT', float),
    ('byLooseIsolationMVArun2v1DBoldDMwLT', float),
    ('byMediumIsolationMVArun2v1DBoldDMwLT', float),
    ('byTightIsolationMVArun2v1DBoldDMwLT', float),
    ('byVTightIsolationMVArun2v1DBoldDMwLT', float),
    ('byVVTightIsolationMVArun2v1DBoldDMwLT', float),

    ('againstElectronMVA6Raw', float),
    ('againstElectronMVA6category', float),
    ('againstElectronLooseMVA6', float),
    ('againstElectronMediumMVA6', float),
    ('againstElectronTightMVA6', float),
    ('againstElectronVLooseMVA6', float),
    ('againstElectronVTightMVA6', float),

    ('againstMuonLoose3', float),
    ('againstMuonTight3', float),

    ('byDeepTau2017v2p1VSeraw', float),
    ('byVVVLooseDeepTau2017v2p1VSe', float),
    ('byVVLooseDeepTau2017v2p1VSe', float),
    ('byVLooseDeepTau2017v2p1VSe', float),
    ('byLooseDeepTau2017v2p1VSe', float),
    ('byMediumDeepTau2017v2p1VSe', float),
    ('byTightDeepTau2017v2p1VSe', float),
    ('byVTightDeepTau2017v2p1VSe', float),
    ('byVVTightDeepTau2017v2p1VSe', float),

    ('byDeepTau2017v2p1VSjetraw', float),
    ('byVVVLooseDeepTau2017v2p1VSjet', float),
    ('byVVLooseDeepTau2017v2p1VSjet', float),
    ('byVLooseDeepTau2017v2p1VSjet', float),
    ('byLooseDeepTau2017v2p1VSjet', float),
    ('byMediumDeepTau2017v2p1VSjet', float),
    ('byTightDeepTau2017v2p1VSjet', float),
    ('byVTightDeepTau2017v2p1VSjet', float),
    ('byVVTightDeepTau2017v2p1VSjet', float),

    ('byDeepTau2017v2p1VSmuraw', float),
    ('byVLooseDeepTau2017v2p1VSmu', float),
    ('byLooseDeepTau2017v2p1VSmu', float),
    ('byMediumDeepTau2017v2p1VSmu', float),
    ('byTightDeepTau2017v2p1VSmu', float),

    ('byIsolationMVArun2017v2DBnewDMwLTraw2017', float),
    ('byVVLooseIsolationMVArun2017v2DBnewDMwLT2017', float),
    ('byVLooseIsolationMVArun2017v2DBnewDMwLT2017', float),
    ('byLooseIsolationMVArun2017v2DBnewDMwLT2017', float),
    ('byMediumIsolationMVArun2017v2DBnewDMwLT2017', float),
    ('byTightIsolationMVArun2017v2DBnewDMwLT2017', float),
    ('byVTightIsolationMVArun2017v2DBnewDMwLT2017', float),
    ('byVVTightIsolationMVArun2017v2DBnewDMwLT2017', float),

    ('byIsolationMVArun2017v2DBoldDMwLTraw2017', float),
    ('byVVLooseIsolationMVArun2017v2DBoldDMwLT2017', float),
    ('byVLooseIsolationMVArun2017v2DBoldDMwLT2017', float),
    ('byLooseIsolationMVArun2017v2DBoldDMwLT2017', float),
    ('byMediumIsolationMVArun2017v2DBoldDMwLT2017', float),
    ('byTightIsolationMVArun2017v2DBoldDMwLT2017', float),
    ('byVTightIsolationMVArun2017v2DBoldDMwLT2017', float),
    ('byVVTightIsolationMVArun2017v2DBoldDMwLT2017', float),

    ('againstElectronLooseMVA62018', float),
    ('againstElectronMVA6Raw2018', float),
    ('againstElectronMVA6category2018', float),
    ('againstElectronMediumMVA62018', float),
    ('againstElectronTightMVA62018', float),
    ('againstElectronVLooseMVA62018', float),
    ('againstElectronVTightMVA62018', float),

    ('againstElectronMVA6RawPhase2v1', float),
    ('againstElectronMVA6categoryPhase2v1', float),
    ('againstElectronVLooseMVA6Phase2v1', float),
    ('againstElectronLooseMVA6Phase2v1', float),
    ('againstElectronMediumMVA6Phase2v1', float),
    ('againstElectronTightMVA6Phase2v1', float),
    ('againstElectronVTightMVA6Phase2v1', float),

    ('byIsolationMVADBnewDMwLTPhase2raw', float),
    ('byVVLooseIsolationMVADBnewDMwLTPhase2', float),
    ('byVLooseIsolationMVADBnewDMwLTPhase2', float),
    ('byLooseIsolationMVADBnewDMwLTPhase2', float),
    ('byMediumIsolationMVADBnewDMwLTPhase2', float),
    ('byTightIsolationMVADBnewDMwLTPhase2', float),
    ('byVTightIsolationMVADBnewDMwLTPhase2', float),
    ('byVVTightIsolationMVADBnewDMwLTPhase2', float),
]

lepton_tau_ids = [
    ('againstMuonLoose3', int),
    ('againstMuonTight3', int),
    ('againstElectronVLooseMVA6', int),
    ('againstElectronLooseMVA6', int),
    ('againstElectronMediumMVA6', int),
    ('againstElectronTightMVA6', int),
    ('againstElectronVTightMVA6', int),
    ('againstElectronMVA6Raw', float),
]

all_wps = ['VVLoose', 'VLoose', 'Loose', 'Medium', 'Tight', 'VTight', 'VVTight']

def create_tau_ids(name, n_wps=7):
    wps = all_wps[:]
    if n_wps == 6:
        wps = all_wps[1:]
    if n_wps == 5:
        wps = all_wps[1:6]
    if n_wps == 8:
        wps.append('VVVLoose')
    if n_wps == 4:
        wps = all_wps[1:5]
    if name[-4:-1] == "201":
      rawname = 'by' + name[:-4] + 'raw' + name[-4:]
    else:
      rawname = 'by' + name + 'raw'
    return [('by' + wp + name, int) for wp in wps] + [(rawname, float)]


tau_ids = {
    'deepTauIDv2p1VSe':create_tau_ids('DeepTau2017v2VSe2017', 4),
    'deepTauIDv2p1VSmu':create_tau_ids('DeepTau2017v2VSmu2017', 8),
    'deepTauIDv2p1VSjet':create_tau_ids('DeepTau2017v2VSjet2017', 8),
    '2017v2':create_tau_ids('IsolationMVArun2017v2DBoldDMwLT2017'),
    'newDM2017v2':create_tau_ids('IsolationMVArun2v1DBnewDMwLT2016', 6),
}

def fill_tau_ids(avd, tau, tau_id_names):
    for (tau_id, _) in tau_id_names:
        avd['tau_'+tau_id].fill(tau.tauID(tau_id))
